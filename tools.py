from langchain_core.tools import tool
import yfinance as yf
from langgraph.types import interrupt

@tool
def get_stock_price(symbol: str) -> float:
    """Get real-time stock price"""
    stock = yf.Ticker(symbol)
    data = stock.history(period="1d")
    return float(data["Close"].iloc[-1])

@tool
def buy_stocks(symbol: str, quantity: int, total_price: float) -> str:
    """Buy stocks with human approval"""

    decision = interrupt(
        f"Approve buying {quantity} {symbol} stocks for ${total_price:.2f}? (yes/no)"
    )

    if decision.lower() == "yes":
        return f"✅ Bought {quantity} shares of {symbol}"
    else:
        return "❌ Buying cancelled"