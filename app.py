import streamlit as st
from agent import graph
from langgraph.types import Command

st.title("📈 AI Stock Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Ask something:")

if st.button("Send"):
    state = graph.invoke(
        {"messages": [{"role": "user", "content": user_input}]},
        config={"configurable": {"thread_id": "web"}}
    )

    # Show response
    if "__interrupt__" in state:
        st.warning(state["__interrupt__"])
        decision = st.radio("Approve?", ["yes", "no"])

        if st.button("Confirm"):
            state = graph.invoke(
                Command(resume=decision),
                config={"configurable": {"thread_id": "web"}}
            )
            st.success(state["messages"][-1].content)
    else:
        st.success(state["messages"][-1].content)