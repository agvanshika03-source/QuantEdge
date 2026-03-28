import streamlit as st
import plotly.graph_objects as go
import numpy as np

def render(data, C, plot_layout, line_trace):
    st.markdown('<div class="page-h1">Market Heatmap</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">S&P 500 constituents · Daily return color-coded · Breadth · Correlation</div>', unsafe_allow_html=True)

    stocks = ['AAPL','MSFT','NVDA','GOOGL','AMZN','META','TSLA','AVGO','ORCL','CSCO',
              'INTC','AMD','CRM','ADBE','NFLX','PYPL','SQ','COIN','PLTR','SNOW',
              'HOOD','RBLX','UBER','LYFT','ABNB','DASH','SPOT','TWLO','ZM','SHOP',
              'ETSY','W','SNAP','PINS','ROKU','MTCH','IAC','YELP','LRCX','KLAC',
              'AMAT','MCHP','TXN','QCOM','MU','STX','CDW','JNPR','CARS','GRPN']

    rng = np.random.RandomState(42)
    rets = [round(((rng.random()-0.62)*6),1) for _ in stocks]

    def ret_color(r):
        if r > 3:   return "#00A884"
        if r > 1:   return "rgba(0,212,170,0.65)"
        if r > -1:  return "rgba(46,66,112,0.9)"
        if r > -3:  return "rgba(180,50,70,0.65)"
        return "#DC2846"

    st.markdown('<div class="dash-card-title">S&P 500 — Daily Return Heatmap</div>', unsafe_allow_html=True)
    st.markdown("""<div style="display:flex;gap:16px;margin-bottom:12px;flex-wrap:wrap">
      <span style="font-family:JetBrains Mono;font-size:9px;color:#00A884">■ &gt;+3%</span>
      <span style="font-family:JetBrains Mono;font-size:9px;color:#00D4AA">■ +1% to +3%</span>
      <span style="font-family:JetBrains Mono;font-size:9px;color:#4D6A9A">■ Flat</span>
      <span style="font-family:JetBrains Mono;font-size:9px;color:#B43246">■ −3% to −1%</span>
      <span style="font-family:JetBrains Mono;font-size:9px;color:#DC2846">■ &lt;−3%</span>
    </div>""", unsafe_allow_html=True)

    cols = st.columns(10)
    for i,(sym,ret) in enumerate(zip(stocks,rets)):
        bg = ret_color(ret)
        tc = "#fff" if abs(ret)>2 else ("#00D4AA" if ret>0 else "#FF5E7D")
        cols[i%10].markdown(f"""
        <div style="background:{bg};border-radius:4px;text-align:center;padding:8px 4px;
        margin-bottom:5px;cursor:default" title="{sym}: {ret}%">
          <div style="font-family:JetBrains Mono;font-size:8px;color:{tc};font-weight:600">{sym}</div>
          <div style="font-family:JetBrains Mono;font-size:8px;color:{tc}">{ret:+.1f}%</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")
    c1,c2 = st.columns(2)
    with c1:
        st.markdown('<div class="dash-card-title">Market Breadth — Advancing vs Declining</div>', unsafe_allow_html=True)
        months=["Nov","Dec","Jan","Feb","Mar"]
        fig = go.Figure()
        fig.add_trace(go.Bar(name="Advancing",x=months,y=[310,285,290,180,120],
            marker_color="rgba(0,212,170,0.65)",marker_line_color="rgb(0,212,170)",marker_line_width=1))
        fig.add_trace(go.Bar(name="Declining",x=months,y=[190,215,210,320,380],
            marker_color="rgba(255,94,125,0.6)",marker_line_color="rgb(255,94,125)",marker_line_width=1))
        fig.update_layout(**plot_layout(h=240))
        st.plotly_chart(fig,use_container_width=True)

    with c2:
        st.markdown('<div class="dash-card-title">Correlation Matrix — Rolling 30D</div>', unsafe_allow_html=True)
        pairs=["SPY–QQQ","SPY–VIX","QQQ–ARKK","SPY–GLD","QQQ–VIX"]
        vals=[0.94,-0.82,0.88,0.12,-0.79]
        cols2=["rgba(0,212,170,0.65)" if v>=0 else "rgba(255,94,125,0.65)" for v in vals]
        fig2 = go.Figure(go.Bar(x=pairs,y=vals,marker_color=cols2,marker_line_width=0))
        fig2.update_layout(**plot_layout(h=240))
        fig2.update_yaxes(range=[-1,1],title_text="Correlation")
        st.plotly_chart(fig2,use_container_width=True)
