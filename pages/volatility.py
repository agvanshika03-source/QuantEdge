import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def render(data, C, plot_layout, line_trace):
    st.markdown('<div class="page-h1">Volatility &amp; Risk</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">VIX · Rolling volatility · Regime heatmap · Risk composite scorecard</div>', unsafe_allow_html=True)

    k1,k2,k3,k4 = st.columns(4)
    k1.metric("VIX Current",     "31.05",  "+13.16% today",    delta_color="inverse")
    k2.metric("1-Month VIX Δ",  "+82%",   "From 17 → 31",     delta_color="inverse")
    k3.metric("QQQ Drawdown",   "−9.8%",  "From $633 peak",    delta_color="inverse")
    k4.metric("ARKK Drawdown",  "−14.4%", "90-day basis",      delta_color="inverse")
    st.markdown("---")

    c1,c2 = st.columns(2)
    with c1:
        st.markdown('<div class="dash-card-title">VIX Index — 90 Day History</div>', unsafe_allow_html=True)
        fig = go.Figure()
        fig.add_hline(y=25,line_dash="dash",line_color="rgba(255,94,125,0.4)",line_width=1,
                      annotation_text="Stress (25)",annotation_font=dict(color="#FF5E7D",size=8))
        fig.add_hline(y=20,line_dash="dash",line_color="rgba(255,181,71,0.4)",line_width=1)
        fig.add_trace(go.Scatter(x=data["DATES"],y=data["VIX"],name="VIX",
            line=dict(color="#FF5E7D",width=2),fill="tozeroy",fillcolor="rgba(255,94,125,0.08)"))
        fig.update_layout(**plot_layout(h=250))
        fig.update_yaxes(range=[10,None])
        st.plotly_chart(fig,use_container_width=True)

    with c2:
        st.markdown('<div class="dash-card-title">VIX Regime-Colored Bars</div>', unsafe_allow_html=True)
        vix_colors = ["rgba(0,212,170,0.7)" if v<15 else
                      "rgba(240,192,64,0.7)" if v<20 else
                      "rgba(255,181,71,0.75)" if v<25 else
                      "rgba(255,94,125,0.75)" for v in data["VIX"]]
        fig = go.Figure(go.Bar(x=data["DATES"],y=data["VIX"],marker_color=vix_colors,
            marker_line_width=0,name="VIX"))
        fig.update_layout(**plot_layout(h=250))
        fig.update_yaxes(range=[10,None])
        st.plotly_chart(fig,use_container_width=True)

    st.markdown("---")
    c3,c4 = st.columns([3,2])
    with c3:
        st.markdown('<div class="dash-card-title">Rolling 20-Day Annualised Volatility</div>', unsafe_allow_html=True)
        fig = go.Figure()
        for key,name,col in [("QQQ_rvol","QQQ Vol","#4F9EFF"),("SPY_rvol","SPY Vol","#00D4AA"),("ARKK_rvol","ARKK Vol","#FF5E7D")]:
            fig.add_trace(go.Scatter(x=data["DATES"],y=data[key],name=name,
                line=dict(color=col,width=2),mode="lines"))
        fig.update_layout(**plot_layout(h=240))
        fig.update_yaxes(title_text="Ann. Vol (%)")
        st.plotly_chart(fig,use_container_width=True)

    with c4:
        st.markdown('<div class="dash-card-title">Risk Composite Scorecard</div>', unsafe_allow_html=True)
        risks = [("VIX Spike Severity",84,"#FF5E7D"),("Drawdown Depth",70,"#FFB547"),
                 ("Algo Sync Risk",78,"#A78BFF"),("Flash Crash Risk",72,"#FF5E7D"),
                 ("Geo-political Fog",65,"#FFB547"),("AI Bubble Risk",68,"#A78BFF")]
        for lbl,pct,col in risks:
            st.markdown(f"""
            <div style="display:flex;align-items:center;gap:10px;margin-bottom:9px">
              <div style="font-size:11px;color:#7090C0;width:150px;flex-shrink:0">{lbl}</div>
              <div style="flex:1;height:5px;background:rgba(255,255,255,.05);border-radius:3px;overflow:hidden">
                <div style="width:{pct}%;height:100%;background:{col};border-radius:3px"></div>
              </div>
              <div style="font-family:JetBrains Mono;font-size:10px;color:{col};width:36px;text-align:right;font-weight:600">{pct/10:.1f}</div>
            </div>""", unsafe_allow_html=True)
        st.markdown('<hr style="border-color:#1C2D50;margin:12px 0">', unsafe_allow_html=True)
        st.markdown("""
        <div style="display:flex;justify-content:space-between;align-items:center">
          <div style="font-family:JetBrains Mono;font-size:8px;letter-spacing:2px;color:#2E4270">COMPOSITE</div>
          <div style="font-family:Playfair Display;font-size:36px;color:#FF5E7D">7.8<span style="font-size:13px;color:#2E4270">/10</span></div>
        </div>""", unsafe_allow_html=True)
