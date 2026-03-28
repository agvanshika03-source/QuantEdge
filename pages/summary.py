import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def render(data, C, plot_layout, line_trace):
    st.markdown('<div class="page-h1">Decision Summary</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">AI-synthesised institutional conclusion · Strategic posture · Action items · Final recommendation</div>', unsafe_allow_html=True)

    # ── CONCLUSION CARDS ─────────────────────────────────
    cols = st.columns(6)
    cards = [
        ("📉","Market State","Transitional\nRisk-Increasing","#FF5E7D"),
        ("🤖","AI Confidence","Low · 55%\n+3pp edge","#FFB547"),
        ("⚡","Vol. Trajectory","Rising\nVIX: 31 → ?","#FF5E7D"),
        ("🌐","Tech Sentiment","Weakening\nAI capex doubt","#FFB547"),
        ("🔄","ARKK Signal","Rotation\nStress evident","#FF5E7D"),
        ("🛡️","Posture","Defensive\n+ Hedged","#00D4AA"),
    ]
    for i,(icon,lbl,val,col) in enumerate(cards):
        cols[i].markdown(f"""
        <div style="background:#111B33;border:1px solid #1C2D50;border-radius:8px;
        padding:14px;text-align:center;height:100%">
          <div style="font-size:22px;margin-bottom:6px">{icon}</div>
          <div style="font-family:JetBrains Mono;font-size:8px;letter-spacing:2px;
          color:#2E4270;text-transform:uppercase;margin-bottom:4px">{lbl}</div>
          <div style="font-family:Playfair Display;font-size:13px;color:{col};
          line-height:1.3;white-space:pre-line">{val}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")
    c1, c2 = st.columns(2)

    # ── ACTION MATRIX ────────────────────────────────────
    with c1:
        st.markdown('<div class="dash-card-title">Strategic Action Matrix</div>', unsafe_allow_html=True)
        df = pd.DataFrame([
            {"Action":"REDUCE",   "Asset":"ARKK, High-Beta Tech",     "Rationale":"Structural downtrend, −14.4% 90D",        "Priority":"HIGH"},
            {"Action":"ADD",      "Asset":"GLD, TLT",                 "Rationale":"Safe-haven; gold +18.4% 1Y",              "Priority":"HIGH"},
            {"Action":"MAINTAIN", "Asset":"SPY Core",                 "Rationale":"Defensive; lower beta than QQQ",          "Priority":"MEDIUM"},
            {"Action":"HEDGE",    "Asset":"VIX Calls / Put Spreads",  "Rationale":"VIX >30; tail risk at $35",               "Priority":"HIGH"},
            {"Action":"WATCH",    "Asset":"QQQ $555 Support",         "Rationale":"Break = cascade trigger",                 "Priority":"MONITOR"},
            {"Action":"WATCH",    "Asset":"Fed Communications",       "Rationale":"'Fog' signal — pivot timing key",         "Priority":"MONITOR"},
        ])
        st.dataframe(df, use_container_width=True, hide_index=True)

    # ── RISK / RETURN SCATTER ────────────────────────────
    with c2:
        st.markdown('<div class="dash-card-title">Risk / Return Scatter — 90 Days</div>', unsafe_allow_html=True)
        instruments = ["SPY","QQQ","ARKK","GLD","TLT"]
        vols   = [1.19, 1.42, 2.67, 0.78, 0.62]
        ret_1y = [14.11,16.81,27.27,18.4,4.1]
        colors = ["#00D4AA","#4F9EFF","#FF5E7D","#F0C040","#A78BFF"]

        fig = go.Figure()
        for sym,vol,ret,col in zip(instruments,vols,ret_1y,colors):
            fig.add_trace(go.Scatter(
                x=[vol], y=[ret], mode="markers+text",
                name=sym, text=[sym],
                textposition="top center",
                textfont=dict(family="JetBrains Mono",size=9,color=col),
                marker=dict(color=col,size=14,line=dict(color="#0D1425",width=2)),
            ))
        fig.update_layout(**plot_layout(h=300))
        fig.update_xaxes(title_text="Volatility (σ)", range=[0,3.2])
        fig.update_yaxes(title_text="1Y Return (%)")
        st.plotly_chart(fig, use_container_width=True)

    # ── FINAL AI SYNTHESIS ───────────────────────────────
    st.markdown("---")
    st.markdown('<div class="dash-card-title">Final AI Synthesis <span class="badge badge-pur">NEXUS AI · EVIDENCE-BACKED</span></div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="background:linear-gradient(135deg,rgba(79,158,255,.06),rgba(0,212,170,.04));
    border:1px solid rgba(79,158,255,.2);border-radius:8px;padding:20px;margin-top:10px">
      <div style="font-family:JetBrains Mono;font-size:8px;letter-spacing:3px;color:#4F9EFF;margin-bottom:12px">◆  NEXUS AI · FINAL SYNTHESIS — MARCH 2026</div>
      <p style="font-size:13px;color:#A8C0E0;line-height:1.8;margin:0">
        As of March 2026, the evidence is unambiguous: <strong style="color:#EEF6FF">AI in financial markets acts as a force
        multiplier — not a stabiliser.</strong> The synchronized decline across SPY (−7%), QQQ (−9.8%), and
        ARKK (−14.4%) against VIX spiking to 31, combined with the self-reinforcing negative narrative
        cycle around AI capex ($630B questioned), validates systemic fragility at scale. The Random Forest
        model provides only <strong style="color:#EEF6FF">marginal signal enhancement (~55%)</strong> — confirming AI delivers
        incremental edge, not dominance. Without robust governance frameworks (SEBI leads globally),
        AI transforms markets into systems that are faster, smarter, and
        <strong style="color:#FF5E7D">significantly more fragile.</strong>
        <br><br>
        <strong style="color:#EEF6FF">Iran war + Fed "fog" + AI bubble skepticism</strong> = triple macro uncertainty.
        Recommended immediate posture:
        <span style="color:#FFB547;font-weight:600">defensive allocation · elevated hedging ·
        VIX trigger watch at $35 · rotate into gold and quality bonds.</span>
        This regime is transitional, not terminal — the next catalyst (Fed pivot or geopolitical
        resolution) will define the next leg decisively.
      </p>
    </div>""", unsafe_allow_html=True)

    # ── RISK BARS SUMMARY ────────────────────────────────
    st.markdown("---")
    st.markdown('<div class="dash-card-title">Risk Factor Summary</div>', unsafe_allow_html=True)
    risk_items = [
        ("Algorithmic Herding","Active — all ETFs declining simultaneously",90,"#FF5E7D"),
        ("VIX Regime Stress","31.05 · +82% in 1 month · Stressed threshold crossed",84,"#FF5E7D"),
        ("Flash Crash Probability","QQQ near $562 · Watch $555 trigger",72,"#FFB547"),
        ("AI Narrative Feedback","$630B capex doubt · software rout · media amplification",75,"#A78BFF"),
        ("Geo-political Risk","Iran war escalation · Middle East supply chain",65,"#FFB547"),
        ("AI Model Confidence","RF at 55% · Low confidence · Bear regime outperforms",45,"#4F9EFF"),
    ]
    for lbl, desc, pct, col in risk_items:
        st.markdown(f"""
        <div style="margin-bottom:12px">
          <div style="display:flex;justify-content:space-between;margin-bottom:4px">
            <div style="font-size:12px;color:#D0E4FF;font-weight:500">{lbl}</div>
            <div style="font-family:JetBrains Mono;font-size:10px;color:{col};font-weight:700">{pct}%</div>
          </div>
          <div style="height:5px;background:rgba(255,255,255,.05);border-radius:3px;overflow:hidden;margin-bottom:3px">
            <div style="width:{pct}%;height:100%;background:{col};border-radius:3px"></div>
          </div>
          <div style="font-size:10px;color:#2E4270;font-family:JetBrains Mono">{desc}</div>
        </div>""", unsafe_allow_html=True)
