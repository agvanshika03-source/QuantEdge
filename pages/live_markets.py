"""Live Markets page"""
import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from data import TICKERS

def render(data, C, plot_layout, line_trace):
    st.markdown('<div class="page-h1">Live Markets</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">Simulated intraday · Order depth · Volume by hour · Mini price cards</div>', unsafe_allow_html=True)

    # Mini ticker cards
    cols = st.columns(6)
    for i, t in enumerate(TICKERS[:6]):
        color = "#00D4AA" if t["up"] else "#FF5E7D"
        arrow = "▲" if t["up"] else "▼"
        cols[i].markdown(f"""
        <div style="background:#0D1425;border:1px solid #1C2D50;border-radius:8px;padding:10px 12px;">
          <div style="font-family:JetBrains Mono;font-size:9px;color:#4D6A9A;letter-spacing:1px">{t['sym']}</div>
          <div style="font-family:Playfair Display;font-size:18px;color:#EEF6FF;margin:3px 0">{t['price']}</div>
          <div style="font-family:JetBrains Mono;font-size:10px;color:{color};font-weight:700">{arrow} {t['chg']}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")
    c1, c2 = st.columns(2)
    prices_q, times_q = data["QQQ_intraday"]
    prices_s, times_s = data["SPY_intraday"]

    with c1:
        st.markdown('<div class="dash-card-title">QQQ Intraday (Simulated)</div>', unsafe_allow_html=True)
        fig = go.Figure(go.Scatter(x=times_q, y=prices_q, mode="lines", name="QQQ",
            line=dict(color="#4F9EFF",width=2), fill="tozeroy", fillcolor="rgba(79,158,255,0.08)"))
        fig.update_layout(**plot_layout(h=220))
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        st.markdown('<div class="dash-card-title">SPY Intraday (Simulated)</div>', unsafe_allow_html=True)
        fig = go.Figure(go.Scatter(x=times_s, y=prices_s, mode="lines", name="SPY",
            line=dict(color="#00D4AA",width=2), fill="tozeroy", fillcolor="rgba(0,212,170,0.07)"))
        fig.update_layout(**plot_layout(h=220))
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    c3, c4 = st.columns([3,2])

    with c3:
        st.markdown('<div class="dash-card-title">Volume by Hour — Today</div>', unsafe_allow_html=True)
        hours = ["9:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00"]
        vols  = [42,28,22,18,15,12,10,11,14,18,24,32,48,82]
        fig = go.Figure(go.Bar(x=hours, y=vols, marker_color="rgba(79,158,255,0.65)",
            marker_line_color="rgb(79,158,255)", marker_line_width=1))
        fig.update_layout(**plot_layout(h=220))
        st.plotly_chart(fig, use_container_width=True)

    with c4:
        st.markdown('<div class="dash-card-title">Market Depth — QQQ</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="font-family:JetBrains Mono;font-size:9px;color:#2E4270;margin-bottom:10px">
          <span style="color:#FF5E7D">■ ASK</span> &nbsp;&nbsp; <span style="color:#00D4AA">■ BID</span>
        </div>""", unsafe_allow_html=True)
        base = 562.58
        asks = [(round(base+(i+1)*0.12,2), 2000-i*300) for i in range(5)]
        bids = [(round(base-i*0.12,2), 2000+i*200) for i in range(5)]
        for price, vol in reversed(asks):
            pct = int(vol/3000*100)
            st.markdown(f"""
            <div style="display:flex;align-items:center;gap:8px;margin-bottom:3px">
              <div style="font-family:JetBrains Mono;font-size:10px;color:#FF5E7D;width:60px;text-align:right">{price}</div>
              <div style="flex:1;height:18px;background:rgba(255,94,125,0.12);border-radius:2px;display:flex;align-items:center;padding:0 6px">
                <span style="font-family:JetBrains Mono;font-size:9px;color:#FF5E7D">{vol:,}</span>
              </div>
            </div>""", unsafe_allow_html=True)
        st.markdown('<div style="text-align:center;font-family:JetBrains Mono;font-size:9px;color:#2E4270;padding:4px 0">── SPREAD: $0.12 ──</div>', unsafe_allow_html=True)
        for price, vol in bids:
            pct = int(vol/3000*100)
            st.markdown(f"""
            <div style="display:flex;align-items:center;gap:8px;margin-bottom:3px">
              <div style="font-family:JetBrains Mono;font-size:10px;color:#00D4AA;width:60px;text-align:right">{price}</div>
              <div style="flex:1;height:18px;background:rgba(0,212,170,0.1);border-radius:2px;display:flex;align-items:center;padding:0 6px;justify-content:flex-end">
                <span style="font-family:JetBrains Mono;font-size:9px;color:#00D4AA">{vol:,}</span>
              </div>
            </div>""", unsafe_allow_html=True)
