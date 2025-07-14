# 📈 Stock Analyst & Trader AI

This project is an intelligent stock analysis system powered by [CrewAI](https://github.com/joaomdmoura/crewai), [Streamlit](https://streamlit.io), and real-time stock data via Yahoo Finance. It simulates the collaboration of two expert agents — a **Financial Analyst** and a **Strategic Trader** — to provide comprehensive analysis and trade recommendations for publicly traded stocks.

---

## 🚀 Features

- 🔍 Real-time stock analysis using `yfinance`
- 🧠 AI-powered Financial Analyst Agent
- 💼 AI-powered Strategic Trader Agent
- 📊 Clear stock performance reports and actionable trading decisions
- 🌐 Intuitive Streamlit web interface

---

## 🗂️ Project Structure

stock-ai-app/
│
├── agents/
|
│ ├── analyst_agent.py # Defines the Financial Analyst Agent
| |
│ └── trader_agent.py # Defines the Strategic Trader Agent
│
|
├── tasks/
|
│ ├── analyse_task.py # Task assigned to the analyst agent
| |
│ └── trade_task.py # Task assigned to the trader agent
│
| 
├── tools/
|
│ └── stock_research_tool.py # Real-time stock data retrieval using yfinance
|
│
├── crew.py # CrewAI task-agent orchestration
|
├── main.py # CLI runner for testing without UI
|
├── app.py # Streamlit Web App interface
|\\\\\\\\\\\\\\\\\\\\
├── .env # Environment variables (API keys if needed)
|
|
└── README.md # Project documentation


---

## 🧠 Agents Overview

### 1. **Financial Market Analyst**
- Role: Analyzes real-time market data
- Tools: `get_stock_price()` (uses Yahoo Finance)
- Output: Price, change %, volume, trends

### 2. **Strategic Stock Trader**
- Role: Recommends Buy / Sell / Hold
- Inputs: Analyst report + real-time price action
- Output: Actionable trade decision

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/stock-ai-app.git
cd stock-ai-app
```

### 2. Create Virtual Environment (optional but recommended)

```
python -m venv venv
source venv/bin/activate    # On Windows: venv\\Scripts\\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Create .env File
Create a .env file in the root directory to load environment variables.
To store the GROQ_API_KEY

### 5.🧪 How to Run

```
streamlit run app.py

```

## 📌 Notes
The agents use groq/llama-3.3-70b-versatile as the backend model — ensure it is available via your CrewAI configuration or Groq API.

All logic uses real-time market data — results will vary based on market conditions.

The tools/ folder is easily extendable to support more financial APIs or custom indicators.

## 🙌 Acknowledgements
CrewAI

Streamlit

Yahoo Finance API

Groq for LLMs
## Output

![alt text](https://github.com/ratnesh134/Stock-Trading-Agent/blob/master/result-image/Screenshot%20from%202025-07-14%2014-53-38.png)


![alt text](https://github.com/ratnesh134/Stock-Trading-Agent/blob/master/result-image/Screenshot%20from%202025-07-14%2014-54-23.png)



## 📬 Contact
Built by [Ratnesh Kumar] — feel free to reach out at [Email][ratnesh134@gmail.com) or connect on [LinkedIn](https://www.linkedin.com/in/ratnesh-kumar-10b60587/)
