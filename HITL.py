# =========================
# IMPORTS
# =========================
from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import interrupt, Command

from langchain_core.tools import tool
from langchain_groq import ChatGroq
import os


# =========================
# STATE
# =========================
class State(TypedDict):
    messages: Annotated[list, add_messages]


# =========================
# TOOLS
# =========================
@tool
def get_stock_price(symbol: str) -> float:
    """Return the current price of a stock given the stock symbol"""
    return {
        "MSFT": 200.3,
        "AAPL": 100.4,
        "AMZN": 150.0,
        "RIL": 87.6
    }.get(symbol, 0.0)


@tool
def buy_stocks(symbol: str, quantity: int, total_price: float) -> str:
    """Buy stocks given the stock symbol and quantity"""

    decision = interrupt(
        f"Approve buying {quantity} {symbol} stocks for ${total_price:.2f}? (yes/no)"
    )

    if decision.lower() == "yes":
        return f"✅ You bought {quantity} shares of {symbol} for ${total_price:.2f}"
    else:
        return "❌ Buying declined."


tools = [get_stock_price, buy_stocks]


# =========================
# LLM (Groq)
# =========================
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant"
)

llm_with_tools = llm.bind_tools(tools)


# =========================
# CHATBOT NODE
# =========================
def chatbot_node(state: State):
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}


# =========================
# GRAPH BUILD
# =========================
memory = MemorySaver()

builder = StateGraph(State)

builder.add_node("chatbot", chatbot_node)
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "chatbot")

builder.add_conditional_edges("chatbot", tools_condition)

builder.add_edge("tools", "chatbot")
builder.add_edge("chatbot", END)

graph = builder.compile(checkpointer=memory)


# =========================
# CONFIG (THREAD MEMORY)
# =========================
config = {"configurable": {"thread_id": "stock_agent"}}


# =========================
# RUN FLOW
# =========================

# Step 1: Ask price
state = graph.invoke(
    {"messages": [{"role": "user", "content": "What is the price of MSFT stock?"}]},
    config=config
)
print("\n🤖:", state["messages"][-1].content)


# Step 2: Ask to buy
state = graph.invoke(
    {"messages": [{"role": "user", "content": "Buy 10 MSFT stocks at current price"}]},
    config=config
)

# HITL trigger
if "__interrupt__" in state:
    print("\n⚠️ HUMAN APPROVAL NEEDED:")
    print(state["__interrupt__"])

    decision = input("\nApprove (yes/no): ")

    state = graph.invoke(Command(resume=decision), config=config)
    print("\n🤖:", state["messages"][-1].content)