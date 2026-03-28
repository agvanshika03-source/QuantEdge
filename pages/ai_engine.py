import streamlit as st
import plotly.graph_objects as go
import numpy as np

def render(data, C, plot_layout, line_trace):
    st.markdown('<div class="page-h1">AI Prediction Engine</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">Random Forest · LSTM · Feature importance · Accuracy diagnostics · Nifty signal gauge</div>', unsafe_allow_html=True)

    k1,k2,k3,k4 = st.columns(4)
    k1.metric("RF Accuracy",       "55%",  "+3pp vs baseline")
    k2.metric("Baseline (Naive)",  "52%",  "— Reference")
    k3.metric("LSTM Accuracy",     "51%",  "−1pp deficit",   delta_color="inverse")
    k4.metric("Sentiment Corr.",   "0.10", "Weak predictor")
    st.markdown("---")

    c1, c2 = st.columns([3,2])

    with c1:
        st.markdown('<div class="dash-card-title">Model Comparison — Radar Chart</div>', unsafe_allow_html=True)
        cats = ["Accuracy","Bear Regime","Bull Regime","Stability","Interpretability","Speed"]
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(r=[55,62,52,70,55,80],theta=cats,fill="toself",name="Random Forest",
            line_color="#A78BFF",fillcolor="rgba(167,139,255,0.12)"))
        fig.add_trace(go.Scatterpolar(r=[51,44,58,48,30,65],theta=cats,fill="toself",name="LSTM",
            line_color="#00D4AA",fillcolor="rgba(0,212,170,0.08)"))
        fig.add_trace(go.Scatterpolar(r=[52,52,52,52,100,95],theta=cats,fill="toself",name="Baseline",
            line_color="#4D6A9A",fillcolor="rgba(77,106,154,0.05)",line=dict(dash="dot")))
        fig.update_layout(height=300,paper_bgcolor="rgba(0,0,0,0)",
            polar=dict(bgcolor="rgba(0,0,0,0)",
                radialaxis=dict(visible=True,range=[0,100],gridcolor="rgba(28,45,80,.5)",
                    tickfont=dict(size=8,color="#2E4270"),tickcolor="rgba(0,0,0,0)"),
                angularaxis=dict(tickfont=dict(size=9,color="#4D6A9A"),gridcolor="rgba(28,45,80,.4)")),
            legend=dict(font=dict(size=9,color="#7090C0"),bgcolor="rgba(0,0,0,0)"),
            margin=dict(l=30,r=30,t=20,b=20))
        st.plotly_chart(fig,use_container_width=True)

        st.markdown("---")
        st.markdown('<div class="dash-card-title">Regime-Based Accuracy Comparison</div>', unsafe_allow_html=True)
        fig2 = go.Figure()
        regimes = ["Bear Market","Sideways","Bull Market"]
        fig2.add_trace(go.Bar(name="Random Forest",x=regimes,y=[62,54,52],
            marker_color="rgba(167,139,255,0.7)",marker_line_color="rgb(167,139,255)",marker_line_width=1))
        fig2.add_trace(go.Bar(name="LSTM",x=regimes,y=[44,51,58],
            marker_color="rgba(0,212,170,0.6)",marker_line_color="rgb(0,212,170)",marker_line_width=1))
        fig2.add_trace(go.Bar(name="Baseline",x=regimes,y=[52,52,52],
            marker_color="rgba(77,106,154,0.5)",marker_line_color="rgb(77,106,154)",marker_line_width=1))
        fig2.update_layout(**plot_layout(h=220))
        fig2.update_yaxes(range=[35,75],title_text="Accuracy (%)")
        st.plotly_chart(fig2,use_container_width=True)

    with c2:
        st.markdown('<div class="dash-card-title">Nifty Signal Gauge</div>', unsafe_allow_html=True)
        fig_g = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=55,
            delta={"reference":52,"increasing":{"color":"#00D4AA"},"decreasing":{"color":"#FF5E7D"}},
            number={"suffix":"%","font":{"color":"#FFB547","family":"Playfair Display","size":44}},
            gauge={
                "axis":{"range":[0,100],"tickcolor":"#2E4270","tickfont":{"size":9}},
                "bar":{"color":"#FFB547"},
                "bgcolor":"#111B33","bordercolor":"#1C2D50",
                "steps":[
                    {"range":[0,40],"color":"rgba(255,94,125,0.2)"},
                    {"range":[40,60],"color":"rgba(255,181,71,0.15)"},
                    {"range":[60,100],"color":"rgba(0,212,170,0.15)"},
                ],
                "threshold":{"line":{"color":"#4F9EFF","width":3},"thickness":0.8,"value":55}
            },
            title={"text":"UPWARD PROBABILITY","font":{"color":"#4D6A9A","size":10,"family":"JetBrains Mono"}}
        ))
        fig_g.update_layout(height=240,paper_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=20,r=20,t=30,b=10),font=dict(family="JetBrains Mono"))
        st.plotly_chart(fig_g,use_container_width=True)

        st.markdown("---")
        st.markdown('<div class="dash-card-title">Feature Importance</div>', unsafe_allow_html=True)
        feats = ["MA-30 Signal","MA-90 Signal","Momentum","Vol Regime","VIX","Sentiment"]
        vals  = [0.78,0.65,0.45,0.38,0.32,0.22]
        cols  = ["#A78BFF","#A78BFF","#00D4AA","#FFB547","#FF5E7D","#4D6A9A"]
        fig3 = go.Figure(go.Bar(x=vals,y=feats,orientation="h",
            marker_color=cols,marker_line_width=0))
        fig3.update_layout(**plot_layout(h=210))
        fig3.update_xaxes(range=[0,1])
        st.plotly_chart(fig3,use_container_width=True)

        st.markdown("""
        <div class="ai-block">
          <p>RF delivers <strong>+3pp edge</strong> — meaningful but not dominant. LSTM underperforms in bear regimes (44% accuracy), validating the thesis: AI creates false-stability signals exactly when risk is highest.</p>
        </div>""", unsafe_allow_html=True)
