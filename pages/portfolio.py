import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from data import HOLDINGS

def render(data, C, plot_layout, line_trace):
    st.markdown('<div class="page-h1">Portfolio Analytics</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">Allocation · P&L · Risk exposure · Holdings</div>', unsafe_allow_html=True)

    k1,k2,k3,k4 = st.columns(4)
    k1.metric("Total Value",  "$2.48M",  "+2.4% today")
    k2.metric("Day P&L",      "−$12.4K", "−0.5% vs open", delta_color="inverse")
    k3.metric("Portfolio Beta","1.24",    "vs S&P 500")
    k4.metric("Sharpe Ratio", "1.38",    "▲ vs 1.12 benchmark")
    st.markdown("---")

    c1, c2 = st.columns([3,2])
    with c1:
        st.markdown('<div class="dash-card-title">P&L Attribution — 90 Days</div>', unsafe_allow_html=True)
        import numpy as np
        pnl=[0,0.8,1.2,0.5,1.8,2.4,1.9,2.1,3.0,2.8,3.5,4.2,3.8,4.5,5.1,4.8,4.2,3.9,3.5,2.8,2.4,1.9,1.5,2.2,2.8,3.4,4.0,3.6,3.0,2.4,1.8,2.5,3.2,3.9,4.6,5.2,4.8,5.4,5.0,4.4,3.8,3.2,2.6,3.2,3.8,4.4,5.0,5.8,6.2,5.6,5.0,5.6,4.8,4.2,3.4,4.0,4.6,4.2,3.8,3.2,3.8,3.4,3.0,3.6,3.2,2.8,3.4,4.0,3.6,3.2,3.8,3.2,3.8,3.4,2.8,3.4,3.4,3.0,2.4,2.0,2.6,3.2,2.6,2.2,1.6,2.2,1.8,2.2,1.6,2.4]
        fig = go.Figure(go.Scatter(x=data["DATES"], y=pnl, mode="lines", name="P&L %",
            line=dict(color="#00D4AA",width=2), fill="tozeroy", fillcolor="rgba(0,212,170,0.08)"))
        fig.update_layout(**plot_layout(h=250))
        fig.update_yaxes(title_text="P&L (%)")
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        st.markdown('<div class="dash-card-title">Asset Allocation</div>', unsafe_allow_html=True)
        labels=["US Equities","Fixed Income","AI/Tech Growth","Gold/Commodities","Cash"]
        values=[42,25,18,10,5]
        colors=["#4F9EFF","#00D4AA","#A78BFF","#F0C040","#FFB547"]
        fig = go.Figure(go.Pie(labels=labels,values=values,hole=0.62,
            marker=dict(colors=colors,line=dict(color="#0D1425",width=2))))
        fig.update_layout(height=180,paper_bgcolor="rgba(0,0,0,0)",
            showlegend=False,margin=dict(l=10,r=10,t=10,b=10))
        st.plotly_chart(fig, use_container_width=True)
        for i,(lbl,val,col) in enumerate(zip(labels,values,colors)):
            st.markdown(f"""
            <div style="display:flex;align-items:center;gap:8px;margin-bottom:5px">
              <div style="width:10px;height:10px;border-radius:50%;background:{col};flex-shrink:0"></div>
              <div style="font-size:11px;color:#A8C0E0;flex:1">{lbl}</div>
              <div style="font-family:JetBrains Mono;font-size:10px;color:#7090C0;font-weight:600">{val}%</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<div class="dash-card-title">Holdings Breakdown</div>', unsafe_allow_html=True)
    rows = []
    for h in HOLDINGS:
        pl = round((h["curr"]-h["cost"])*h["shares"],0)
        pl_pct = round((h["curr"]/h["cost"]-1)*100,1)
        rows.append({"Symbol":h["sym"],"Name":h["name"],"Shares":h["shares"],
                     "Avg Cost":f"${h['cost']:.2f}","Current":f"${h['curr']:.2f}",
                     "Value":f"${h['val']:,}","P&L":f"${pl:+,.0f}","P&L %":f"{pl_pct:+.1f}%"})
    df = pd.DataFrame(rows)
    st.dataframe(df, use_container_width=True, hide_index=True)
