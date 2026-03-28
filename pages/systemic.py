import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def render(data, C, plot_layout, line_trace):
    st.markdown('<div class="page-h1">Systemic Risk Research</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">Algorithmic herding · Flash crash · AI bubble · Regulatory posture</div>', unsafe_allow_html=True)

    c1,c2,c3 = st.columns(3)
    def ib(color_class, title, body):
        return f'<div class="ib {color_class}"><div class="ib-title">{title}</div><div class="ib-body">{body}</div></div>'

    with c1:
        st.markdown('<div class="dash-card-title">Algorithmic Herding <span class="badge badge-red">ACTIVE</span></div>', unsafe_allow_html=True)
        st.markdown(ib("ib-r","Mechanism","AI models trained on identical datasets create <strong>homogenous decisions</strong>. Sell orders cluster — liquidity vanishes in milliseconds."), unsafe_allow_html=True)
        st.markdown(ib("ib-y","Evidence","ARKK −4.1% + VIX +13.16% on Mar 27. Software sector lost <strong>~$1T</strong> Feb 2026 — no dip-buyers."), unsafe_allow_html=True)
        st.markdown(ib("ib-b","Trigger","All ETFs declining + VIX spike = <strong>herding probability &gt;70%</strong>."), unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="dash-card-title">Flash Crash Cascade <span class="badge badge-red">ELEVATED</span></div>', unsafe_allow_html=True)
        st.markdown(ib("ib-r","Oct 2025 Precedent","Crypto: $9.9B wiped. Algorithms accelerated crash. <strong>Liquidity collapsed 98%</strong> in hours."), unsafe_allow_html=True)
        st.markdown(ib("ib-y","Trigger Zones","QQQ &lt;<strong>$555</strong> or VIX &gt;<strong>35</strong> = stop-loss cascade. Leveraged ETF rebalancing amplifies 3–5×."), unsafe_allow_html=True)
        st.markdown(ib("ib-p","Infrastructure","Shared cloud/API = <strong>correlated failure risk</strong> across institutions simultaneously."), unsafe_allow_html=True)

    with c3:
        st.markdown('<div class="dash-card-title">Narrative Volatility <span class="badge badge-gld" style="color:#FFB547;border-color:rgba(255,181,71,.3);background:rgba(255,181,71,.07)">AMPLIFYING</span></div>', unsafe_allow_html=True)
        st.markdown(ib("ib-r","Feedback Loop","Negative AI news → algo selling → decline → more negative coverage. <strong>Self-reinforcing cycle</strong>."), unsafe_allow_html=True)
        st.markdown(ib("ib-y","2026 Evidence","$630B AI capex doubts → software repricing. Fed cites AI as <strong>'economic fog'</strong> variable."), unsafe_allow_html=True)
        st.markdown(ib("ib-g","Long-Term","ECB: AI boosts productivity +4% over 10Y. BlackRock warns of <strong>wealth inequality</strong> risk."), unsafe_allow_html=True)

    st.markdown("---")
    c4,c5 = st.columns(2)
    with c4:
        st.markdown('<div class="dash-card-title">AI Benefits vs Systemic Risks</div>', unsafe_allow_html=True)
        cats = ["Execution","Risk Mgmt","Pattern Rec.","Data Process.","Efficiency","Liquidity"]
        fig = go.Figure()
        fig.add_trace(go.Bar(name="Benefit",x=cats,y=[90,75,80,88,70,65],
            marker_color="rgba(0,212,170,0.6)",marker_line_color="rgb(0,212,170)",marker_line_width=1))
        fig.add_trace(go.Bar(name="Systemic Risk",x=cats,y=[85,72,68,80,60,78],
            marker_color="rgba(255,94,125,0.55)",marker_line_color="rgb(255,94,125)",marker_line_width=1))
        fig.update_layout(**plot_layout(h=260))
        fig.update_yaxes(range=[0,100])
        st.plotly_chart(fig,use_container_width=True)

    with c5:
        st.markdown('<div class="dash-card-title">Regulatory Response Matrix</div>', unsafe_allow_html=True)
        df = pd.DataFrame([
            {"Regulator":"SEBI","Country":"India","Action":"Algo registration + AI audit IDs","Status":"PROACTIVE"},
            {"Regulator":"FCA","Country":"UK","Action":"Principle-based AI governance","Status":"ACTIVE"},
            {"Regulator":"SEC","Country":"US","Action":"AI disclosure requirements","Status":"DEVELOPING"},
            {"Regulator":"IOSCO","Country":"Global","Action":"AI supervisory toolkits","Status":"ACTIVE"},
            {"Regulator":"ECB/SSM","Country":"EU","Action":"Model validation + stress tests","Status":"ADVANCED"},
            {"Regulator":"RBI","Country":"India","Action":"Fintech AI sandbox","Status":"PILOT"},
        ])
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.markdown("""
        <div class="callout">SEBI leads globally with the most comprehensive AI governance framework for financial markets —
        mandatory registration, unique audit IDs, human oversight requirements, and explicit flash crash prevention protocols.</div>
        """, unsafe_allow_html=True)
