import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from data import NEWS_ITEMS

def render(data, C, plot_layout, line_trace):
    st.markdown('<div class="page-h1">News &amp; Sentiment Intelligence</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">Macro headlines · ARK moves · Sentiment scoring · Category analysis</div>', unsafe_allow_html=True)

    k1,k2,k3,k4 = st.columns(4)
    k1.metric("Macro Sentiment",  "−0.65", "Bearish · geopolitics", delta_color="inverse")
    k2.metric("AI Narrative",     "−0.45", "Capex skepticism",       delta_color="inverse")
    k3.metric("Long-Term AI",     "+0.40", "ECB +4% productivity")
    k4.metric("Sent.–Ret. Corr.", "0.10",  "Weak predictor")
    st.markdown("---")

    c1,c2 = st.columns([3,2])
    with c1:
        st.markdown('<div class="dash-card-title">Sentiment by Category</div>', unsafe_allow_html=True)
        cats   = ["Macro","AI Capex","Tech Sector","ARKK/Innov.","Long-Term AI","Regulatory"]
        scores = [-0.65,-0.45,-0.55,-0.20,0.40,-0.10]
        colors = ["rgba(255,94,125,0.7)","rgba(255,94,125,0.55)","rgba(255,94,125,0.6)",
                  "rgba(255,181,71,0.6)","rgba(0,212,170,0.6)","rgba(77,106,154,0.5)"]
        fig = go.Figure(go.Bar(x=cats,y=scores,marker_color=colors,marker_line_width=0))
        fig.update_layout(**plot_layout(h=200))
        fig.update_yaxes(range=[-1,1],title_text="Score (−1 to +1)")
        st.plotly_chart(fig,use_container_width=True)

        st.markdown("---")
        st.markdown('<div class="dash-card-title">30-Day Sentiment Trend</div>', unsafe_allow_html=True)
        trend = [round(-0.1 - i*0.019 + np.random.RandomState(i).uniform(-0.02,0.02),2) for i in range(30)]
        days  = [f"D-{30-i}" for i in range(30)]
        fig2 = go.Figure(go.Scatter(x=days,y=trend,mode="lines",name="Macro Sentiment",
            line=dict(color="#FF5E7D",width=1.8),fill="tozeroy",fillcolor="rgba(255,94,125,0.07)"))
        fig2.update_layout(**plot_layout(h=150))
        fig2.update_yaxes(range=[-1,0.2])
        st.plotly_chart(fig2,use_container_width=True)

    with c2:
        st.markdown('<div class="dash-card-title">News Feed <span class="badge badge-red">MAR 2026</span></div>', unsafe_allow_html=True)
        for item in NEWS_ITEMS:
            tag_color = "#FF5E7D" if item["bear"] is True else "#00D4AA" if item["bear"] is False else "#FFB547"
            tag_bg    = "rgba(255,94,125,0.08)" if item["bear"] is True else "rgba(0,212,170,0.07)" if item["bear"] is False else "rgba(255,181,71,0.07)"
            dot_color = "#FF5E7D" if item["bear"] is True else "#00D4AA" if item["bear"] is False else "#FFB547"
            st.markdown(f"""
            <div style="padding:8px 0 8px 14px;border-left:2px solid #1C2D50;margin-bottom:4px;position:relative">
              <div style="position:absolute;left:-5px;top:13px;width:8px;height:8px;border-radius:50%;background:{dot_color};border:2px solid #0D1425"></div>
              <div style="font-size:11px;color:#D0E4FF;line-height:1.4;margin-bottom:4px">{item['hl']}</div>
              <div style="display:flex;align-items:center;gap:8px">
                <span style="font-family:JetBrains Mono;font-size:8px;color:#2E4270">{item['src']}</span>
                <span style="font-family:JetBrains Mono;font-size:7px;padding:2px 6px;border-radius:2px;letter-spacing:1px;
                border:1px solid {tag_color};color:{tag_color};background:{tag_bg}">{item['tag']}</span>
              </div>
            </div>""", unsafe_allow_html=True)
