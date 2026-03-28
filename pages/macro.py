import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def render(data, C, plot_layout, line_trace):
    st.markdown('<div class="page-h1">Macro &amp; Bonds</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">Yield curve · Central bank rates · Global indices · Macro indicators</div>', unsafe_allow_html=True)

    # Yield curve
    st.markdown('<div class="dash-card-title">US Treasury Yield Curve — Mar 27, 2026</div>', unsafe_allow_html=True)
    mats   = ["1M","3M","6M","1Y","5Y","10Y","30Y"]
    yields = [5.21,5.18,4.96,4.72,4.18,4.35,4.62]
    chgs   = ["+2bp","+1bp","−1bp","−3bp","−4bp","−2bp","flat"]
    chg_c  = ["#FF5E7D","#FF5E7D","#00D4AA","#00D4AA","#00D4AA","#00D4AA","#7090C0"]
    yield_cols = st.columns(7)
    for i,(m,y,ch,cc) in enumerate(zip(mats,yields,chgs,chg_c)):
        ycolor = "#FF5E7D" if y>4.5 else "#FFB547" if y>4.3 else "#4F9EFF"
        yield_cols[i].markdown(f"""
        <div style="text-align:center;background:#0D1425;border:1px solid #1C2D50;border-radius:6px;padding:10px 6px">
          <div style="font-family:JetBrains Mono;font-size:9px;color:#2E4270;margin-bottom:4px">{m}</div>
          <div style="font-family:JetBrains Mono;font-size:13px;font-weight:600;color:{ycolor}">{y:.2f}%</div>
          <div style="font-family:JetBrains Mono;font-size:9px;color:{cc};margin-top:2px">{ch}</div>
        </div>""", unsafe_allow_html=True)

    fig = go.Figure(go.Scatter(x=mats,y=yields,mode="lines+markers",name="Yield Curve",
        line=dict(color="#4F9EFF",width=2.5),
        marker=dict(color="#4F9EFF",size=8,line=dict(color="#0D1425",width=2)),
        fill="tozeroy",fillcolor="rgba(79,158,255,0.07)"))
    fig.update_layout(**plot_layout(h=200))
    fig.update_yaxes(range=[3.5,5.8],title_text="Yield (%)")
    st.plotly_chart(fig,use_container_width=True)

    st.markdown("---")
    c1,c2,c3 = st.columns(3)
    with c1:
        st.markdown('<div class="dash-card-title">Global Indices</div>', unsafe_allow_html=True)
        df_idx = pd.DataFrame([
            {"Index":"S&P 500","Price":"5,035","1D":"-1.71%","1M":"-7.0%"},
            {"Index":"NASDAQ", "Price":"17,460","1D":"-1.95%","1M":"-9.8%"},
            {"Index":"Dow Jones","Price":"38,210","1D":"-0.95%","1M":"-5.2%"},
            {"Index":"FTSE 100","Price":"7,890","1D":"-0.8%","1M":"-3.4%"},
            {"Index":"Nikkei","Price":"34,580","1D":"+0.4%","1M":"-8.1%"},
            {"Index":"Nifty 50","Price":"22,140","1D":"-0.6%","1M":"-4.2%"},
        ])
        st.dataframe(df_idx,use_container_width=True,hide_index=True)

    with c2:
        st.markdown('<div class="dash-card-title">Central Bank Rates</div>', unsafe_allow_html=True)
        df_cb = pd.DataFrame([
            {"Bank":"Federal Reserve","Rate":"5.25–5.50%","Trend":"Hold"},
            {"Bank":"ECB","Rate":"4.50%","Trend":"Cutting"},
            {"Bank":"Bank of England","Rate":"5.25%","Trend":"Hold"},
            {"Bank":"RBI India","Rate":"6.50%","Trend":"Hold"},
            {"Bank":"Bank of Japan","Rate":"0.10%","Trend":"Rising"},
            {"Bank":"PBoC China","Rate":"3.45%","Trend":"Easing"},
        ])
        st.dataframe(df_cb,use_container_width=True,hide_index=True)

    with c3:
        st.markdown('<div class="dash-card-title">Macro Indicators</div>', unsafe_allow_html=True)
        macros = [("US CPI YoY","3.2%","#FF5E7D"),("Core PCE","3.8%","#FFB547"),
                  ("Unemployment","3.9%","#00D4AA"),("DXY Index","104.2","#4F9EFF"),
                  ("Gold / oz","$2,318","#F0C040"),("WTI Crude","$78.40","#FFB547")]
        for lbl,val,col in macros:
            st.markdown(f"""
            <div style="display:flex;justify-content:space-between;align-items:center;
            background:#111B33;border:1px solid #1C2D50;border-radius:6px;
            padding:8px 12px;margin-bottom:6px">
              <div style="font-family:JetBrains Mono;font-size:9px;letter-spacing:1px;color:#4D6A9A">{lbl}</div>
              <div style="font-family:Playfair Display;font-size:18px;color:{col}">{val}</div>
            </div>""", unsafe_allow_html=True)
