import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import datetime
from data import get_all_data, SECTOR_DATA, TICKERS, HOLDINGS, NEWS_ITEMS
from ai_chat import get_ai_response

# ─── PAGE CONFIG ───────────────────────────────────────
st.set_page_config(
    page_title="QuantEdge Pro · AI Financial Intelligence Terminal",
    page_icon="⬡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── LOAD DATA ─────────────────────────────────────────
data = get_all_data()
QQQ = data["QQQ"]
SPY = data["SPY"]
ARKK = data["ARKK"]
VIX = data["VIX"]
DATES = data["DATES"]

# ─── COLOUR PALETTE ────────────────────────────────────
C = {
    "bg0": "#05070F", "bg1": "#080C18", "bg2": "#0D1425",
    "bg3": "#111B33", "bg4": "#162240", "border": "#1C2D50",
    "muted": "#2E4270", "sub": "#4D6A9A", "dim": "#7090C0",
    "body": "#A8C0E0", "title": "#D0E4FF", "white": "#EEF6FF",
    "c1": "#4F9EFF", "c2": "#00D4AA", "c3": "#FF5E7D",
    "c4": "#FFB547", "c5": "#A78BFF", "c6": "#00E5FF",
    "gold": "#F0C040", "gold2": "#FFE080",
}

# ─── GLOBAL CSS ────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=JetBrains+Mono:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif !important;
    background-color: #05070F !important;
    color: #A8C0E0 !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #080C18 0%, #0D1425 100%) !important;
    border-right: 1px solid #1C2D50 !important;
}
[data-testid="stSidebar"] .stMarkdown p { color: #7090C0 !important; }
[data-testid="stSidebar"] hr { border-color: #1C2D50 !important; }

/* Main background */
.main .block-container { background: #05070F !important; padding-top: 1rem !important; }
.stApp { background: #05070F !important; }

/* Metric cards */
[data-testid="stMetric"] {
    background: #0D1425 !important;
    border: 1px solid #1C2D50 !important;
    border-radius: 10px !important;
    padding: 16px !important;
}
[data-testid="stMetricLabel"] { color: #4D6A9A !important; font-family: 'JetBrains Mono' !important; font-size: 11px !important; letter-spacing: 1px !important; }
[data-testid="stMetricValue"] { color: #EEF6FF !important; font-family: 'Playfair Display' !important; font-size: 28px !important; }
[data-testid="stMetricDelta"] { font-family: 'JetBrains Mono' !important; font-size: 11px !important; }

/* Buttons in sidebar */
.stButton > button {
    background: transparent !important;
    border: 1px solid #1C2D50 !important;
    color: #7090C0 !important;
    border-radius: 6px !important;
    font-family: 'JetBrains Mono' !important;
    font-size: 11px !important;
    width: 100% !important;
    text-align: left !important;
    padding: 8px 14px !important;
    transition: all 0.15s !important;
    margin-bottom: 2px !important;
}
.stButton > button:hover {
    border-color: #4F9EFF !important;
    color: #D0E4FF !important;
    background: rgba(79,158,255,0.08) !important;
}

/* Active nav button */
.nav-active > button {
    border-left: 3px solid #F0C040 !important;
    color: #EEF6FF !important;
    background: linear-gradient(90deg,rgba(79,158,255,0.1),transparent) !important;
}

/* Cards */
.dash-card {
    background: #0D1425;
    border: 1px solid #1C2D50;
    border-radius: 10px;
    padding: 18px 20px;
    margin-bottom: 16px;
}
.dash-card-title {
    font-family: 'Playfair Display', serif;
    font-size: 16px;
    color: #D0E4FF;
    margin-bottom: 4px;
}
.dash-card-sub {
    font-family: 'JetBrains Mono', monospace;
    font-size: 9px;
    color: #4D6A9A;
    letter-spacing: 1px;
    margin-bottom: 14px;
}

/* Ticker strip */
.ticker-strip {
    background: #080C18;
    border-bottom: 1px solid #1C2D50;
    padding: 8px 0;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    white-space: nowrap;
    overflow: hidden;
}

/* Badge */
.badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 8px;
    letter-spacing: 1.5px;
    padding: 3px 8px;
    border-radius: 3px;
    border: 1px solid;
    text-transform: uppercase;
    display: inline-block;
    margin-left: 8px;
}
.badge-red  { color:#FF5E7D; border-color:rgba(255,94,125,.35); background:rgba(255,94,125,.08); }
.badge-grn  { color:#00D4AA; border-color:rgba(0,212,170,.3);   background:rgba(0,212,170,.07);  }
.badge-blu  { color:#4F9EFF; border-color:rgba(79,158,255,.35); background:rgba(79,158,255,.08); }
.badge-gld  { color:#F0C040; border-color:rgba(240,192,64,.3);  background:rgba(240,192,64,.07); }
.badge-muted{ color:#4D6A9A; border-color:#1C2D50;              background:#111B33; }
.badge-pur  { color:#A78BFF; border-color:rgba(167,139,255,.3); background:rgba(167,139,255,.07);}

/* AI synthesis block */
.ai-block {
    background: linear-gradient(135deg,rgba(79,158,255,.06),rgba(0,212,170,.04));
    border: 1px solid rgba(79,158,255,.2);
    border-radius: 8px;
    padding: 14px 16px;
    margin-top: 12px;
}
.ai-block::before {
    content: "◆  NEXUS AI SYNTHESIS";
    font-family: 'JetBrains Mono', monospace;
    font-size: 8px;
    letter-spacing: 3px;
    color: #4F9EFF;
    display: block;
    margin-bottom: 7px;
}
.ai-block p { font-size: 12px; color: #7090C0; line-height: 1.7; margin: 0; }

/* Insight block */
.ib { background: #111B33; border: 1px solid #1C2D50; border-left: 3px solid; border-radius: 0 8px 8px 0; padding: 11px 13px; margin-bottom: 9px; }
.ib-r { border-left-color: #FF5E7D; }
.ib-g { border-left-color: #00D4AA; }
.ib-b { border-left-color: #4F9EFF; }
.ib-y { border-left-color: #FFB547; }
.ib-p { border-left-color: #A78BFF; }
.ib-title { font-family: 'JetBrains Mono'; font-size: 9px; letter-spacing: 2px; text-transform: uppercase; color: #D0E4FF; margin-bottom: 4px; font-weight: 600; }
.ib-body  { font-size: 12px; color: #4D6A9A; line-height: 1.6; }

/* News items */
.news-item { padding: 9px 0 9px 14px; border-left: 2px solid #1C2D50; margin-bottom: 4px; position: relative; }
.news-hl   { font-size: 12px; color: #D0E4FF; line-height: 1.4; margin-bottom: 4px; }
.news-meta { font-family: 'JetBrains Mono'; font-size: 9px; color: #2E4270; }

/* Callout box */
.callout {
    background: #111B33;
    border-left: 4px solid #F0C040;
    border-radius: 0 8px 8px 0;
    padding: 14px 16px;
    margin: 14px 0;
    font-size: 13px;
    color: #7090C0;
    font-style: italic;
    line-height: 1.65;
}

/* Divider */
.hdiv { border: none; border-top: 1px solid #1C2D50; margin: 14px 0; opacity: 0.6; }

/* Page heading */
.page-h1 { font-family: 'Playfair Display', serif; font-size: 28px; color: #EEF6FF; font-weight: 400; line-height: 1.1; }
.page-sub { font-size: 12px; color: #4D6A9A; margin-top: 4px; margin-bottom: 20px; }

/* Section label */
.sec-lbl { font-family: 'JetBrains Mono'; font-size: 9px; letter-spacing: 3px; color: #4F9EFF; text-transform: uppercase; margin-bottom: 10px; opacity: 0.8; }

/* Risk bar row */
.rb-wrap { display: flex; align-items: center; gap: 10px; margin-bottom: 10px; }

/* Chat bubble */
.chat-ai   { background: #111B33; border: 1px solid #1C2D50; border-radius: 3px 10px 10px 10px; padding: 10px 13px; margin-bottom: 8px; font-size: 12px; color: #A8C0E0; line-height: 1.6; max-width: 90%; }
.chat-user { background: linear-gradient(135deg,#2575E8,#7C5CE8); border-radius: 10px 3px 10px 10px; padding: 10px 13px; margin-bottom: 8px; font-size: 12px; color: #fff; line-height: 1.6; max-width: 90%; margin-left: auto; }
.chat-time { font-family: 'JetBrains Mono'; font-size: 8px; color: #2E4270; }

/* Dataframe */
[data-testid="stDataFrame"] { background: #0D1425 !important; border: 1px solid #1C2D50 !important; border-radius: 8px !important; }

/* Tabs */
.stTabs [data-baseweb="tab-list"] { background: #080C18 !important; border-bottom: 1px solid #1C2D50 !important; gap: 2px !important; }
.stTabs [data-baseweb="tab"]       { background: transparent !important; color: #4D6A9A !important; font-family: 'JetBrains Mono' !important; font-size: 10px !important; letter-spacing: 1px !important; }
.stTabs [aria-selected="true"]     { color: #F0C040 !important; border-bottom: 2px solid #F0C040 !important; }
.stTabs [data-baseweb="tab-panel"] { background: transparent !important; padding: 14px 0 0 0 !important; }

/* Selectbox */
.stSelectbox select { background: #0D1425 !important; color: #A8C0E0 !important; border: 1px solid #1C2D50 !important; }

/* Text input */
.stTextInput input { background: #0D1425 !important; color: #A8C0E0 !important; border: 1px solid #1C2D50 !important; border-radius: 20px !important; font-family: 'JetBrains Mono' !important; font-size: 12px !important; }

/* Expander */
details { background: #0D1425 !important; border: 1px solid #1C2D50 !important; border-radius: 8px !important; }
summary { color: #D0E4FF !important; font-family: 'Playfair Display' !important; }

/* Radio */
.stRadio label { color: #7090C0 !important; font-family: 'JetBrains Mono' !important; font-size: 11px !important; }

/* Hide streamlit branding */
#MainMenu {visibility: hidden;}
footer     {visibility: hidden;}
header     {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ─── HELPER: PLOTLY LAYOUT ─────────────────────────────
def plot_layout(title="", h=300):
    return dict(
        height=h, title=title,
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="JetBrains Mono", size=10, color="#4D6A9A"),
        margin=dict(l=10, r=10, t=30 if title else 10, b=30),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1,
                    bgcolor="rgba(0,0,0,0)", font=dict(size=9)),
        xaxis=dict(showgrid=True, gridcolor="rgba(28,45,80,.35)", gridwidth=1,
                   tickfont=dict(size=8, color="#2E4270"), showline=False, zeroline=False),
        yaxis=dict(showgrid=True, gridcolor="rgba(28,45,80,.35)", gridwidth=1,
                   tickfont=dict(size=8, color="#2E4270"), showline=False, zeroline=False),
    )

def line_trace(name, x, y, color, fill=False, dash=None):
    return go.Scatter(
        name=name, x=x, y=y, mode="lines",
        line=dict(color=color, width=2, dash=dash),
        fill="tozeroy" if fill else "none",
        fillcolor=color.replace("rgb","rgba").replace(")",",0.07)") if fill and "rgb" in color else None,
        hovertemplate=f"<b>{name}</b><br>%{{x}}<br>%{{y:.2f}}<extra></extra>",
    )

# ─── SESSION STATE ─────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "Overview"
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "ai", "msg": "👋 Hello! I'm **Nexus AI**, your financial intelligence assistant. I can help you analyse VIX signals, interpret AI model outputs, discuss systemic risk, portfolio allocation, and more. What would you like to explore?"}
    ]

# ─── SIDEBAR ───────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='display:flex;align-items:center;gap:10px;padding:4px 0 16px'>
      <div style='width:36px;height:36px;border-radius:8px;background:linear-gradient(135deg,#4F9EFF,#00D4AA);display:flex;align-items:center;justify-content:center;font-family:JetBrains Mono;font-size:12px;font-weight:700;color:#fff;flex-shrink:0'>QE</div>
      <div>
        <div style='font-family:Playfair Display,serif;font-size:16px;color:#EEF6FF;font-weight:600'>QuantEdge</div>
        <div style='font-family:JetBrains Mono;font-size:8px;color:#2E4270;letter-spacing:2px'>PRO · AI TERMINAL</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    now = datetime.datetime.now()
    st.markdown(f"""
    <div style='font-family:JetBrains Mono;font-size:9px;color:#2E4270;margin-bottom:4px'>
      🟢 &nbsp;{now.strftime("%H:%M:%S")} EST &nbsp;|&nbsp; Mar 29, 2026
    </div>
    <div style='display:flex;align-items:center;gap:8px;margin-bottom:14px'>
      <span style='background:rgba(255,94,125,.1);border:1px solid rgba(255,94,125,.3);color:#FF5E7D;font-family:JetBrains Mono;font-size:8px;padding:3px 8px;border-radius:3px;letter-spacing:1.5px'>⚠ RISK-OFF ACTIVE</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='font-family:JetBrains Mono;font-size:8px;letter-spacing:2px;color:#2E4270;text-transform:uppercase;padding:6px 0 4px'>CORE</div>", unsafe_allow_html=True)

    NAV_PAGES = [
        ("⬡", "Overview"),
        ("📡", "Live Markets"),
        ("💼", "Portfolio"),
        ("📈", "Technicals"),
    ]
    ANALYTICS_PAGES = [
        ("🤖", "AI Engine"),
        ("⚡", "Volatility & Risk"),
        ("🏛️", "Sectors"),
        ("🌍", "Macro & Bonds"),
    ]
    RESEARCH_PAGES = [
        ("🔬", "Systemic Risk"),
        ("📰", "News & Sentiment"),
        ("🔥", "Market Heatmap"),
        ("📋", "Decision Summary"),
        ("🧠", "AI Chatbot"),
    ]

    for icon, label in NAV_PAGES:
        active = st.session_state.page == label
        container = st.container()
        if active:
            container.markdown('<div class="nav-active">', unsafe_allow_html=True)
        if container.button(f"{icon}  {label}", key=f"nav_{label}"):
            st.session_state.page = label
            st.rerun()
        if active:
            container.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1C2D50;margin:8px 0'><div style='font-family:JetBrains Mono;font-size:8px;letter-spacing:2px;color:#2E4270;text-transform:uppercase;padding:6px 0 4px'>ANALYTICS</div>", unsafe_allow_html=True)

    for icon, label in ANALYTICS_PAGES:
        active = st.session_state.page == label
        if active:
            st.markdown('<div class="nav-active">', unsafe_allow_html=True)
        if st.button(f"{icon}  {label}", key=f"nav_{label}"):
            st.session_state.page = label
            st.rerun()
        if active:
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<hr style='border-color:#1C2D50;margin:8px 0'><div style='font-family:JetBrains Mono;font-size:8px;letter-spacing:2px;color:#2E4270;text-transform:uppercase;padding:6px 0 4px'>RESEARCH</div>", unsafe_allow_html=True)

    for icon, label in RESEARCH_PAGES:
        active = st.session_state.page == label
        if active:
            st.markdown('<div class="nav-active">', unsafe_allow_html=True)
        if st.button(f"{icon}  {label}", key=f"nav_{label}"):
            st.session_state.page = label
            st.rerun()
        if active:
            st.markdown("</div>", unsafe_allow_html=True)

# ─── TOPBAR TICKER ─────────────────────────────────────
tick_items = " &nbsp;|&nbsp; ".join(
    [f'<span style="color:#D0E4FF;font-weight:600">{t["sym"]}</span> '
     f'<span style="color:#EEF6FF">{t["price"]}</span> '
     f'<span style="color:{"#00D4AA" if t["up"] else "#FF5E7D"}">{t["chg"]}</span>'
     for t in TICKERS]
)
st.markdown(f"""
<div style='background:#080C18;border-bottom:1px solid #1C2D50;padding:7px 0 7px 14px;
font-family:JetBrains Mono;font-size:10px;white-space:nowrap;overflow:hidden;
margin-bottom:16px;border-radius:6px'>
<span style='color:#4F9EFF;letter-spacing:2px;margin-right:14px'>◈ LIVE</span>
{tick_items}
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════
# PAGE IMPORTS
# ════════════════════════════════════════════════════════
from pages.overview      import render as p_overview
from pages.live_markets  import render as p_live
from pages.portfolio     import render as p_portfolio
from pages.technicals    import render as p_tech
from pages.ai_engine     import render as p_ai
from pages.volatility    import render as p_vol
from pages.sectors       import render as p_sectors
from pages.macro         import render as p_macro
from pages.systemic      import render as p_systemic
from pages.news          import render as p_news
from pages.heatmap       import render as p_heatmap
from pages.summary       import render as p_summary
from pages.chatbot       import render as p_chatbot

PAGE_MAP = {
    "Overview":        p_overview,
    "Live Markets":    p_live,
    "Portfolio":       p_portfolio,
    "Technicals":      p_tech,
    "AI Engine":       p_ai,
    "Volatility & Risk": p_vol,
    "Sectors":         p_sectors,
    "Macro & Bonds":   p_macro,
    "Systemic Risk":   p_systemic,
    "News & Sentiment": p_news,
    "Market Heatmap":  p_heatmap,
    "Decision Summary": p_summary,
    "AI Chatbot":      p_chatbot,
}

# ─── RENDER CURRENT PAGE ───────────────────────────────
current_page = st.session_state.page
render_fn = PAGE_MAP.get(current_page, p_overview)
render_fn(data, C, plot_layout, line_trace)
