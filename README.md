# QuantEdge Pro · AI Financial Intelligence Terminal

> **AI-Driven Market Signal & Risk Dashboard** — Financial Systems & Markets Research Project

A professional multi-page financial intelligence dashboard built with Streamlit and Plotly, featuring an AI chatbot (Nexus AI), live market data, 13 interactive pages, and comprehensive risk analytics.

---

## 📸 Dashboard Pages

| Page | Description |
|------|-------------|
| ⬡ Overview | Cross-market KPIs, normalized returns, regime gauge |
| 📡 Live Markets | Intraday simulation, order book depth, volume chart |
| 💼 Portfolio | P&L attribution, asset allocation donut, holdings table |
| 📈 Technicals | MA overlays, RSI-14, returns distribution |
| 🤖 AI Engine | RF vs LSTM radar, signal gauge, feature importance |
| ⚡ Volatility & Risk | VIX history, regime heatmap, rolling volatility |
| 🏛️ Sectors | S&P 500 sector grid, returns bar, rotation radar |
| 🌍 Macro & Bonds | Yield curve, global indices, central bank rates |
| 🔬 Systemic Risk | Herding/flash crash analysis, regulatory matrix |
| 📰 News & Sentiment | Scored news feed, sentiment trend, category bar |
| 🔥 Market Heatmap | Color-coded stock heatmap, breadth, correlations |
| 📋 Decision Summary | Action matrix, risk/return scatter, AI synthesis |
| 🧠 AI Chatbot | Nexus AI — intelligent financial Q&A assistant |

---

## 🚀 Deploy to Streamlit Cloud (Step-by-Step)

### Step 1 — Upload to GitHub

1. Go to [github.com](https://github.com) and sign in (or create an account)
2. Click **"New repository"**
3. Name it: `quantedge-pro`
4. Set to **Public**
5. Click **"Create repository"**
6. Upload ALL files from this folder:
   - `app.py`
   - `data.py`
   - `ai_chat.py`
   - `requirements.txt`
   - `pages/` folder (all `.py` files inside)
   - `.streamlit/config.toml`

> **Tip:** Use GitHub Desktop or drag-and-drop upload on github.com

---

### Step 2 — Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click **"New app"**
4. Fill in:
   - **Repository:** `your-username/quantedge-pro`
   - **Branch:** `main`
   - **Main file path:** `app.py`
5. Click **"Deploy!"**
6. Wait ~2 minutes — your app will be live at:
   `https://your-username-quantedge-pro-app-XXXXX.streamlit.app`

---

## 💻 Run Locally

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the app
streamlit run app.py

# 3. Open browser at http://localhost:8501
```

---

## 📁 File Structure

```
quantedge-pro/
├── app.py                  ← Main Streamlit app (entry point)
├── data.py                 ← All market data + helper functions
├── ai_chat.py              ← Nexus AI chatbot knowledge base
├── requirements.txt        ← Python dependencies
├── .streamlit/
│   └── config.toml         ← Dark theme configuration
└── pages/
    ├── __init__.py
    ├── overview.py          ← Executive Overview page
    ├── live_markets.py      ← Live Markets page
    ├── portfolio.py         ← Portfolio Analytics page
    ├── technicals.py        ← Technical Analysis page
    ├── ai_engine.py         ← AI Prediction Engine page
    ├── volatility.py        ← Volatility & Risk page
    ├── sectors.py           ← Sector Performance page
    ├── macro.py             ← Macro & Bonds page
    ├── systemic.py          ← Systemic Risk Research page
    ├── news.py              ← News & Sentiment page
    ├── heatmap.py           ← Market Heatmap page
    ├── summary.py           ← Decision Summary page
    └── chatbot.py           ← AI Chatbot page
```

---

## 🎨 Design System

- **Fonts:** Outfit (body) · Playfair Display (headings) · JetBrains Mono (data/labels)
- **Color Palette:** Deep navy background (#05070F) with electric blue (#4F9EFF), teal (#00D4AA), rose (#FF5E7D), gold (#F0C040), violet (#A78BFF) accents
- **Charts:** Plotly with custom dark theme — zero-line charts, regime-colored bars, radar overlays

---

## 📊 Data Sources

| Source | Data |
|--------|------|
| Investing.com | SPY, QQQ, ARKK daily OHLCV (Jan 2018 – Mar 2026) |
| CBOE | VIX daily history (Jan 2018 – Mar 2026) |
| Reuters/Bloomberg | News headlines (Mar 2026) |
| Nifty 50 | AI model training dataset |

---

## 🧠 AI Chatbot Topics

Ask Nexus AI about:
- **VIX** — current level, regime classification, spike analysis
- **Market regime** — stress scoring, risk factors
- **ARKK** — structural decline, ARK portfolio moves
- **AI signal** — RF model accuracy, feature importance, LSTM comparison
- **Systemic risks** — herding, flash crash probability, cascade triggers
- **Buy/sell** — strategic posture, hedging recommendations
- **Portfolio** — P&L, allocation, rebalancing signals
- **Macro** — Fed policy, yield curve, global indices, inflation

---

## 📝 Academic Context

This dashboard was built as part of the **Financial Systems & Markets (BFM-4820)** module, supporting the research report:

> *"AI in Financial Markets: Enhancing Efficiency or Amplifying Systemic Instability?"*
> Deep Research Synthesis · March 2026

**Key findings:**
- Random Forest model: ~55% accuracy (+3pp over baseline)
- VIX surged +82% in 1 month (13.38 → 31.05)
- All ETFs in synchronized decline: SPY −7%, QQQ −9.8%, ARKK −14.4%
- AI acts as **force multiplier** — not stabiliser

---

*Built with Streamlit · Plotly · Python · QuantEdge Pro*
