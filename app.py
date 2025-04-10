
import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import tradingeconomics as te

# Load TradingEconomics API key
api_key = st.secrets["TE_API_KEY"]
te.login(api_key)

st.set_page_config(layout="wide", page_title="Global Capital Markets Dashboard", initial_sidebar_state="expanded")

st.title("🌍 Global Capital Markets Dashboard")

# Auto-refresh every 5 minutes (300000 milliseconds)
st.markdown(
    """
    <meta http-equiv="refresh" content="300">
    """,
    unsafe_allow_html=True
)

def format_market_data(df):
    df['Changes'] = pd.to_numeric(df['Changes'], errors='coerce')
    df['PercentChange'] = pd.to_numeric(df['PercentChange'], errors='coerce')
    df['Last'] = pd.to_numeric(df['Last'], errors='coerce')
    df = df.dropna(subset=["Symbol", "Last"])
    df = df[["Symbol", "Last", "Changes", "PercentChange"]]
    df.columns = ["Symbol", "Current Price", "Change", "% Change"]
    return df.sort_values("Symbol")

# 1. Treasuries (2Y, 10Y, 30Y for US, EU, Switzerland, Japan)
treasuries = [
    "US2Y:IND", "US10Y:IND", "US30Y:IND",
    "EU2Y:IND", "EU10Y:IND", "EU30Y:IND",
    "CH2Y:IND", "CH10Y:IND", "CH30Y:IND",
    "JP2Y:IND", "JP10Y:IND", "JP30Y:IND"
]

# 2. Index Futures
indices = [
    "ES1:IND", "NQ1:IND", "YM1:IND", "RTY1:IND",  # US futures
    "Z1:IND", "SX5E:IND", "DAX:IND",             # EU
    "NK1:IND", "HSI1:IND", "SSE:IND", "GIFNIFTY:IND"  # Asia
]

# 3. Currencies
currencies = ["DXY:CUR", "EURUSD:CUR", "USDCHF:CUR", "USDJPY:CUR", "USDINR:CUR"]

# 4. VIX
vix = ["VIX:IND"]

# 5. Equities (examples)
us_equities = ["AAPL:US", "MSFT:US", "NVDA:US"]
eu_equities = ["SIE:GR", "SAP:GR"]
jp_equities = ["6758:JP", "9984:JP"]
cn_equities = ["600519:CH", "601318:CH"]
in_equities = ["RELIANCE:NS", "INFY:NS"]

# Get data from TE
def get_data(symbols):
    data = te.getMarkets(symbols=symbols)
    df = pd.DataFrame(data)
    return format_market_data(df)

# Show tables
st.subheader("📈 Treasury Yields")
st.dataframe(get_data(treasuries), use_container_width=True)

st.subheader("📊 Index Futures")
st.dataframe(get_data(indices), use_container_width=True)

st.subheader("💱 Currencies")
st.dataframe(get_data(currencies), use_container_width=True)

st.subheader("⚠️ VIX")
st.dataframe(get_data(vix), use_container_width=True)

st.subheader("🇺🇸 US Equities")
st.dataframe(get_data(us_equities), use_container_width=True)

st.subheader("🇪🇺 EU Equities")
st.dataframe(get_data(eu_equities), use_container_width=True)

st.subheader("🇯🇵 Japan Equities")
st.dataframe(get_data(jp_equities), use_container_width=True)

st.subheader("🇨🇳 China Equities")
st.dataframe(get_data(cn_equities), use_container_width=True)

st.subheader("🇮🇳 India Equities")
st.dataframe(get_data(in_equities), use_container_width=True)
