import streamlit as st
import plotly.graph_objects as go
from data import SECTOR_DATA

def render(data, C, plot_layout, line_trace):
    st.markdown('<div class="page-h1">Sector Performance</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">S&P 500 sector returns · Rotation map · Leader vs laggard</div>', unsafe_allow_html=True)

    cols = st.columns(4)
    for i, s in enumerate(SECTOR_DATA):
        color = "#00D4AA" if s["ret"] >= 0 else "#FF5E7D"
        arrow = "▲" if s["ret"] >= 0 else "▼"
        cols[i % 4].markdown(f"""
        <div style="background:#0D1425;border:1px solid #1C2D50;border-radius:8px;padding:10px 12px;margin-bottom:10px;cursor:pointer">
          <div style="font-family:JetBrains Mono;font-size:8px;color:#4D6A9A;letter-spacing:1px;text-transform:uppercase;margin-bottom:4px">{s['name']}</div>
          <div style="font-family:JetBrains Mono;font-size:16px;font-weight:700;color:{color}">{arrow} {s['ret']:+.1f}%</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")
    c1,c2 = st.columns(2)
    with c1:
        st.markdown('<div class="dash-card-title">Sector Returns — 1 Month</div>', unsafe_allow_html=True)
        names = [s["name"] for s in SECTOR_DATA]
        rets  = [s["ret"]  for s in SECTOR_DATA]
        colors= ["rgba(0,212,170,0.65)" if r>=0 else "rgba(255,94,125,0.65)" for r in rets]
        fig = go.Figure(go.Bar(x=rets,y=names,orientation="h",
            marker_color=colors,marker_line_width=0))
        fig.update_layout(**plot_layout(h=340))
        fig.update_xaxes(title_text="Return (%)")
        st.plotly_chart(fig,use_container_width=True)

    with c2:
        st.markdown('<div class="dash-card-title">Sector Rotation Radar</div>', unsafe_allow_html=True)
        cats = ["Technology","Healthcare","Financials","Energy","Consumer","Utilities","Materials"]
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(r=[-8.2,1.4,-3.8,4.2,-5.1,2.8,-1.2],theta=cats,
            fill="toself",name="1-Month",line_color="#4F9EFF",fillcolor="rgba(79,158,255,0.1)"))
        fig.add_trace(go.Scatterpolar(r=[-12,2.8,-5.2,6.8,-7.4,4.2,-2.8],theta=cats,
            fill="toself",name="3-Month",line_color="#00D4AA",fillcolor="rgba(0,212,170,0.08)"))
        fig.update_layout(height=340,paper_bgcolor="rgba(0,0,0,0)",
            polar=dict(bgcolor="rgba(0,0,0,0)",
                radialaxis=dict(visible=True,range=[-15,10],gridcolor="rgba(28,45,80,.5)",
                    tickfont=dict(size=8,color="#2E4270")),
                angularaxis=dict(tickfont=dict(size=9,color="#4D6A9A"),gridcolor="rgba(28,45,80,.4)")),
            legend=dict(font=dict(size=9,color="#7090C0"),bgcolor="rgba(0,0,0,0)"),
            margin=dict(l=30,r=30,t=20,b=20))
        st.plotly_chart(fig,use_container_width=True)
