# 🌍 Global Capital Markets Dashboard

A real-time dashboard built with Streamlit to track global markets for investment analysis.

## 📊 Features

- Treasury yields (2Y, 10Y, 30Y) for US, EU, Switzerland, Japan
- Index futures like S&P 500, Nasdaq 100, FTSE 100, Nikkei 225, etc.
- Major currencies: DXY, EURUSD, USDCHF, USDJPY, USDINR
- VIX tracker
- Equities segregated by region (US, EU, Japan, China, India)
- OHLC + volume charts
- Auto-refresh every 5 minutes

## 🚀 Run Locally

1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/global-markets-dashboard.git
cd global-markets-dashboard
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Add your TradingEconomics API key in `.streamlit/secrets.toml`

```toml
TE_API_KEY = "your_api_key_here"
```

4. Run the app

```bash
streamlit run app.py
```

## 🌐 Deployment

You can deploy this on [Streamlit Cloud](https://streamlit.io/cloud) for free!

## 📄 License

MIT

