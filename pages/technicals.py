import streamlit as st
import plotly.graph_objects as go

def render(data, C, plot_layout, line_trace):
    st.markdown('<div class="page-h1">Technical Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">Price charts · Moving averages · RSI · Returns distribution</div>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["  📈 PRICE + MA  ","  📊 RSI MOMENTUM  ","  📉 DISTRIBUTION  "])

    with tab1:
        c1,c2 = st.columns(2)
        with c1:
            st.markdown('<div class="dash-card-title">QQQ + MA-20 / MA-50</div>', unsafe_allow_html=True)
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=data["DATES"],y=data["QQQ"],name="QQQ",
                line=dict(color="#4F9EFF",width=2),fill="tozeroy",fillcolor="rgba(79,158,255,0.08)"))
            fig.add_trace(go.Scatter(x=data["DATES"],y=data["QQQ_ma20"],name="MA-20",
                line=dict(color="#F0C040",width=1.5,dash="dot")))
            fig.add_trace(go.Scatter(x=data["DATES"],y=data["QQQ_ma50"],name="MA-50",
                line=dict(color="#A78BFF",width=1.5,dash="dash")))
            fig.update_layout(**plot_layout(h=280))
            st.plotly_chart(fig,use_container_width=True)

        with c2:
            st.markdown('<div class="dash-card-title">SPY + MA-20 / MA-50</div>', unsafe_allow_html=True)
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=data["DATES"],y=data["SPY"],name="SPY",
                line=dict(color="#00D4AA",width=2),fill="tozeroy",fillcolor="rgba(0,212,170,0.07)"))
            fig.add_trace(go.Scatter(x=data["DATES"],y=data["SPY_ma20"],name="MA-20",
                line=dict(color="#F0C040",width=1.5,dash="dot")))
            fig.add_trace(go.Scatter(x=data["DATES"],y=data["SPY_ma50"],name="MA-50",
                line=dict(color="#A78BFF",width=1.5,dash="dash")))
            fig.update_layout(**plot_layout(h=280))
            st.plotly_chart(fig,use_container_width=True)

        st.markdown('<div class="dash-card-title">ARKK — Structural Decline</div>', unsafe_allow_html=True)
        fig = go.Figure(go.Scatter(x=data["DATES"],y=data["ARKK"],name="ARKK",
            line=dict(color="#FF5E7D",width=2),fill="tozeroy",fillcolor="rgba(255,94,125,0.08)"))
        fig.update_layout(**plot_layout(h=220))
        st.plotly_chart(fig,use_container_width=True)

    with tab2:
        st.markdown('<div class="dash-card-title">RSI-14 — QQQ Momentum</div>', unsafe_allow_html=True)
        rsi = data["QQQ_rsi"]
        fig = go.Figure()
        fig.add_hrect(y0=70,y1=100,fillcolor="rgba(255,94,125,0.06)",line_width=0)
        fig.add_hrect(y0=0,y1=30,fillcolor="rgba(0,212,170,0.06)",line_width=0)
        fig.add_hline(y=70,line_dash="dash",line_color="rgba(255,94,125,0.4)",line_width=1)
        fig.add_hline(y=30,line_dash="dash",line_color="rgba(0,212,170,0.4)",line_width=1)
        fig.add_trace(go.Scatter(x=data["DATES"],y=rsi,name="RSI-14",
            line=dict(color="#FFB547",width=2),fill="tozeroy",fillcolor="rgba(255,181,71,0.06)"))
        fig.update_layout(**plot_layout(h=280))
        fig.update_yaxes(range=[0,100])
        st.plotly_chart(fig,use_container_width=True)
        st.markdown("""
        <div class="callout">RSI analysis: QQQ RSI trending below 45 in March 2026 — approaching oversold territory
        but not yet at extreme levels. A RSI dip below 30 historically signals near-term bounce potential.
        Current reading confirms bearish momentum without extreme capitulation.</div>""", unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="dash-card-title">Daily Returns Distribution</div>', unsafe_allow_html=True)
        rets_q = [round((data["QQQ"][i]/data["QQQ"][i-1]-1)*100,3) for i in range(1,len(data["QQQ"]))]
        rets_s = [round((data["SPY"][i]/data["SPY"][i-1]-1)*100,3) for i in range(1,len(data["SPY"]))]
        rets_a = [round((data["ARKK"][i]/data["ARKK"][i-1]-1)*100,3) for i in range(1,len(data["ARKK"]))]
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=rets_q,name="QQQ",nbinsx=20,
            marker_color="rgba(79,158,255,0.6)",marker_line_color="rgb(79,158,255)",marker_line_width=1))
        fig.add_trace(go.Histogram(x=rets_s,name="SPY",nbinsx=20,
            marker_color="rgba(0,212,170,0.5)",marker_line_color="rgb(0,212,170)",marker_line_width=1))
        fig.add_trace(go.Histogram(x=rets_a,name="ARKK",nbinsx=20,
            marker_color="rgba(255,94,125,0.5)",marker_line_color="rgb(255,94,125)",marker_line_width=1))
        fig.update_layout(**plot_layout(h=280), barmode="overlay")
        fig.update_traces(opacity=0.75)
        st.plotly_chart(fig,use_container_width=True)
