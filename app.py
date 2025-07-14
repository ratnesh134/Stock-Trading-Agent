import streamlit as st
from dotenv import load_dotenv
from crew import stock_crew
import io
import sys

# Load .env
load_dotenv()

# Page setup
st.set_page_config(page_title="Stock Analyst & Trader AI", layout="centered")

# Custom CSS for larger code blocks
st.markdown("""
    <style>
        .big-output-box {
            background-color: #1e1e1e; /* Dark background */
            color: #f1f1f1;            /* Light text */
            padding: 1.5rem;
            border-radius: 12px;
            font-size: 1.1rem;
            line-height: 1.6;
            white-space: pre-wrap;
            border: 1px solid #444;
            overflow-x: auto;
        }
        .section-header {
            font-size: 1.3rem;
            font-weight: bold;
            margin-top: 2rem;
            margin-bottom: 0.5rem;
            color: #f1f1f1;
        }
    </style>
""", unsafe_allow_html=True)


# Title
st.markdown("<h1 style='text-align: center;'>📈 Stock Analyst & Trader AI</h1>", unsafe_allow_html=True)

st.markdown("""
Use this AI tool to analyze any publicly traded stock in real time.

**Agents involved:**
- 🧠 *Financial Analyst*: Reviews the live stock data
- 💼 *Trader*: Gives a trade recommendation (Buy / Sell / Hold)
""")

# Input
stock_symbol = st.text_input("🔍 Enter Stock Symbol (e.g., AAPL, TSLA):", value="AAPL")

if st.button("🚀 Analyze & Recommend"):
    if not stock_symbol.strip():
        st.warning("Please enter a stock ticker.")
    else:
        with st.spinner("Running agents... Please wait ⏳"):
            buffer = io.StringIO()
            sys_stdout = sys.stdout
            sys.stdout = buffer

            try:
                result = stock_crew.kickoff(inputs={"stock": stock_symbol.upper()})
            except Exception as e:
                sys.stdout = sys_stdout
                st.error(f"❌ Error: {str(e)}")
            else:
                sys.stdout = sys_stdout
                logs = buffer.getvalue()

                st.success("✅ Analysis Complete!")

                if isinstance(result, dict):
                    analyst_output = result.get("get_stock_analysis", "No output from analyst.")
                    trader_output = result.get("trade_decision", "No output from trader.")

                    # Analyst output
                    st.markdown("<div class='section-header'>🧠 Financial Analyst's Report</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='big-output-box'>{analyst_output}</div>", unsafe_allow_html=True)

                    # Trader output
                    st.markdown("<div class='section-header'>💼 Trader's Recommendation</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='big-output-box'>{trader_output}</div>", unsafe_allow_html=True)

                else:
                    # Fallback output
                    st.markdown("<div class='section-header'>📊 Agent Output</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='big-output-box'>{result}</div>", unsafe_allow_html=True)

                # Logs (optional)
                with st.expander("📜 Raw Logs"):
                    st.markdown(f"```markdown\n{logs}\n```")
