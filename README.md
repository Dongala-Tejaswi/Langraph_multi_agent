# Langraph_multi_agent
# 🚀 AI Stock Assistant using LangGraph

An intelligent AI-powered stock assistant that can fetch real-time stock prices, execute stock purchase decisions with human approval, and demonstrate advanced agent workflows using LangGraph.

---

## 📌 Features

✅ Real-time stock price fetching using Yahoo Finance
✅ AI agent powered by LangChain + LangGraph
✅ Human-in-the-loop (HITL) approval before stock purchase
✅ Tool calling (function calling) support
✅ Streamlit-based interactive UI
✅ Memory-enabled conversation flow

---

## 🧠 How It Works

1. User enters a query (e.g., *"Buy 10 MSFT stocks"*)
2. AI agent processes the request using LangGraph
3. Agent calls tools like:

   * `get_stock_price`
   * `buy_stocks`
4. Before executing purchase, system asks for **human approval**
5. Based on input (**yes/no**), action is completed

---

## 🏗️ Project Structure

```
Langraph/
│
├── app.py              # Streamlit UI
├── agent.py            # LangGraph workflow logic
├── tools.py            # Tool definitions (stock + buy)
├── .env                # API keys (not pushed to GitHub)
├── .gitignore          # Ignore sensitive files
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```

---

## ⚙️ Tech Stack

* Python 🐍
* LangChain
* LangGraph
* Groq API (LLM)
* Streamlit
* yFinance

---

## 🔐 Environment Setup

Create a `.env` file in root:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ How to Run

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run the app

```bash
streamlit run app.py
```

---

## 🧪 Example Queries

* "What is the price of MSFT stock?"
* "Buy 5 AAPL stocks"
* "Buy 10 AMZN stocks at current price"

---

## ⚠️ Important Notes

* API keys are secured using environment variables
* `.env` file is excluded using `.gitignore`
* Do NOT expose API keys in public repositories

---

## 🚀 Future Improvements

* 📊 Multi-stock portfolio calculation
* 🤖 Multi-agent system
* 🌐 Deployment (Streamlit Cloud / AWS)
* 📈 Real-time dashboards
* 🧠 RAG integration for financial insights

---

## 👨‍💻 Author

**Tejaswi Dongala**
Aspiring AI/ML Engineer

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!

---
