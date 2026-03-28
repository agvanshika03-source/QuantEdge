import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def render(data, C, plot_layout, line_trace):
    st.markdown('<div class="page-h1">Executive Overview</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">Cross-market intelligence · AI signal · Regime classification · Global context</div>', unsafe_allow_html=True)

    # ── KPI ROW ──────────────────────────────────────────
    k1, k2, k3, k4, k5 = st.columns(5)
    k1.metric("VIX — Fear Index",   "31.05",   "+13.16% today",  delta_color="inverse")
    k2.metric("QQQ — Nasdaq 100",   "$562.58", "−1.95% today",   delta_color="inverse")
    k3.metric("SPY — S&P 500",      "$634.09", "−1.71% today",   delta_color="inverse")
    k4.metric("ARKK — Innovation",  "$64.63",  "−4.10% today",   delta_color="inverse")
    k5.metric("AI Signal (Nifty)",  "55%",     "+3pp vs baseline")

    st.markdown("---")

    col1, col2 = st.columns([3, 2])

    # ── NORMALIZED CHART ─────────────────────────────────
    with col1:
        st.markdown('<div class="dash-card-title">Normalized Returns — 90 Days</div>', unsafe_allow_html=True)
        st.markdown('<div class="dash-card-sub">ALL INSTRUMENTS · BASE = NOV 17, 2025</div>', unsafe_allow_html=True)

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            name="SPY", x=data["DATES"], y=data["SPY_norm"],
            mode="lines", line=dict(color="#00D4AA", width=2),
            fill="tozeroy", fillcolor="rgba(0,212,170,0.08)",
            hovertemplate="<b>SPY</b><br>%{x}<br>%{y:.2f}%<extra></extra>"
        ))
        fig.add_trace(go.Scatter(
            name="QQQ", x=data["DATES"], y=data["QQQ_norm"],
            mode="lines", line=dict(color="#4F9EFF", width=2),
            hovertemplate="<b>QQQ</b><br>%{x}<br>%{y:.2f}%<extra></extra>"
        ))
        fig.add_trace(go.Scatter(
            name="ARKK", x=data["DATES"], y=data["ARKK_norm"],
            mode="lines", line=dict(color="#FF5E7D", width=2),
            hovertemplate="<b>ARKK</b><br>%{x}<br>%{y:.2f}%<extra></extra>"
        ))
        fig.update_layout(**plot_layout(h=280))
        fig.update_yaxes(title_text="Return vs Base (%)", title_font=dict(size=9, color="#2E4270"))
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
        <div class="ai-block">
          <p>All three instruments show <strong>synchronized deterioration since late Jan 2026</strong>.
          ARKK leads (−14.4%) confirming <strong>algorithmic herding</strong>. SPY's relative resilience (−3.9%)
          signals slow rotation toward defensives — not full capitulation yet.</p>
        </div>""", unsafe_allow_html=True)

    # ── REGIME + SIGNAL ──────────────────────────────────
    with col2:
        st.markdown('<div class="dash-card-title">Composite Risk Score</div>', unsafe_allow_html=True)
        st.markdown('<span class="badge badge-red">STRESSED REGIME</span>', unsafe_allow_html=True)

        # Gauge
        fig_g = go.Figure(go.Indicator(
            mode="gauge+number",
            value=7.8,
            domain={"x":[0,1],"y":[0,1]},
            number={"font":{"color":"#FF5E7D","family":"Playfair Display","size":52}, "suffix":"/10"},
            gauge={
                "axis":{"range":[0,10],"tickcolor":"#2E4270","tickfont":{"size":9,"color":"#2E4270"}},
                "bar":{"color":"#FF5E7D"},
                "bgcolor":"#111B33",
                "bordercolor":"#1C2D50",
                "steps":[
                    {"range":[0,3],"color":"rgba(0,212,170,0.2)"},
                    {"range":[3,6],"color":"rgba(255,181,71,0.2)"},
                    {"range":[6,10],"color":"rgba(255,94,125,0.15)"},
                ],
                "threshold":{"line":{"color":"#F0C040","width":3},"thickness":0.8,"value":7.8}
            }
        ))
        fig_g.update_layout(
            height=200, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=20,r=20,t=10,b=10), font=dict(family="JetBrains Mono")
        )
        st.plotly_chart(fig_g, use_container_width=True)

        # Risk bars
        risks = [
            ("VIX Spike", 84, "#FF5E7D"),
            ("Drawdown", 72, "#FFB547"),
            ("Algo Sync", 78, "#A78BFF"),
            ("Geo-political", 65, "#FFB547"),
        ]
        for lbl, pct, col in risks:
            st.markdown(f"""
            <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px">
              <div style="font-size:11px;color:#7090C0;width:130px;flex-shrink:0">{lbl}</div>
              <div style="flex:1;height:5px;background:rgba(255,255,255,.05);border-radius:3px;overflow:hidden">
                <div style="width:{pct}%;height:100%;background:{col};border-radius:3px"></div>
              </div>
              <div style="font-family:JetBrains Mono;font-size:10px;color:{col};width:36px;text-align:right">{pct/10:.1f}</div>
            </div>""", unsafe_allow_html=True)

        st.markdown("""
        <div style="display:flex;align-items:center;gap:10px;margin-top:12px;padding:10px;
        background:rgba(255,94,125,.07);border:1px solid rgba(255,94,125,.25);border-radius:6px">
          <span style="width:8px;height:8px;border-radius:50%;background:#FF5E7D;
          animation:pulse 1.5s infinite;flex-shrink:0;display:inline-block"></span>
          <span style="font-family:JetBrains Mono;font-size:10px;color:#FF5E7D;letter-spacing:1.5px;font-weight:700">
          RISK-OFF REGIME ACTIVE</span>
        </div>""", unsafe_allow_html=True)

    # ── PERFORMANCE TABLE ─────────────────────────────────
    st.markdown("---")
    st.markdown('<div class="dash-card-title">Cross-Asset Performance Matrix</div>', unsafe_allow_html=True)

    df = pd.DataFrame([
        {"Instrument":"SPY — S&P 500 ETF","Price":"$634.09","1D":"-1.71%","1W":"-2.87%","1M":"-7.0%","3M":"-3.94%","1Y":"+14.11%","Vol":"1.19σ","Signal":"BEARISH"},
        {"Instrument":"QQQ — Nasdaq 100", "Price":"$562.58","1D":"-1.95%","1W":"-3.35%","1M":"-7.36%","3M":"-6.81%","1Y":"+16.81%","Vol":"1.42σ","Signal":"BEARISH"},
        {"Instrument":"ARKK — Innovation","Price":"$64.63", "1D":"-4.10%","1W":"-5.48%","1M":"-10.7%","3M":"-14.4%","1Y":"+27.27%","Vol":"2.67σ","Signal":"STRESS"},
        {"Instrument":"VIX — CBOE Vol",   "Price":"31.05",  "1D":"+13.16%","1W":"+30%","1M":"+82%","3M":"+90%","1Y":"—","Vol":"—","Signal":"ELEVATED"},
        {"Instrument":"GLD — Gold ETF",   "Price":"$218.40","1D":"+0.92%","1W":"+2.1%","1M":"+4.8%","3M":"+7.2%","1Y":"+18.4%","Vol":"0.78σ","Signal":"BULLISH"},
        {"Instrument":"DXY — Dollar",     "Price":"104.2",  "1D":"+0.34%","1W":"+0.8%","1M":"-1.2%","3M":"-2.4%","1Y":"+3.1%","Vol":"0.61σ","Signal":"NEUTRAL"},
    ])
    st.dataframe(df, use_container_width=True, hide_index=True)
