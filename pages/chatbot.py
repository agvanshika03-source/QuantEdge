import streamlit as st
import datetime
from ai_chat import get_ai_response

def render(data, C, plot_layout, line_trace):
    st.markdown('<div class="page-h1">Nexus AI — Financial Intelligence Chatbot</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">Ask about VIX · Market regimes · AI signals · Systemic risk · Portfolio strategy · Macro outlook</div>', unsafe_allow_html=True)

    # ── CHAT HEADER CARD ─────────────────────────────────
    st.markdown("""
    <div style="background:linear-gradient(135deg,#111B33,#0D1425);border:1px solid #1C2D50;
    border-radius:12px;padding:16px 20px;display:flex;align-items:center;gap:14px;margin-bottom:20px">
      <div style="width:48px;height:48px;border-radius:50%;
      background:linear-gradient(135deg,#4F9EFF,#00D4AA);
      display:flex;align-items:center;justify-content:center;font-size:22px;flex-shrink:0">🧠</div>
      <div>
        <div style="font-family:Playfair Display;font-size:18px;color:#EEF6FF;font-weight:600">Nexus AI Analyst</div>
        <div style="font-family:JetBrains Mono;font-size:9px;color:#00D4AA;
        display:flex;align-items:center;gap:6px;margin-top:3px">
          <span style="width:6px;height:6px;border-radius:50%;background:#00D4AA;display:inline-block"></span>
          Online · Financial Intelligence · Mar 29, 2026
        </div>
        <div style="font-size:11px;color:#4D6A9A;margin-top:3px">
          Powered by QuantEdge Pro · Knowledge Base covers VIX, AI signals, systemic risk, portfolio strategy &amp; macro
        </div>
      </div>
    </div>""", unsafe_allow_html=True)

    # ── QUICK CHIPS ──────────────────────────────────────
    st.markdown('<div style="font-family:JetBrains Mono;font-size:8px;letter-spacing:2px;color:#2E4270;margin-bottom:8px">QUICK QUESTIONS</div>', unsafe_allow_html=True)
    quick_qs = [
        "What is the current market regime?",
        "Explain the VIX spike today",
        "Why is ARKK declining?",
        "What does the AI model signal?",
        "What are the biggest systemic risks?",
        "Should I buy or sell now?",
        "Tell me about the portfolio",
        "What is the macro outlook?",
    ]
    chip_cols = st.columns(4)
    for i, q in enumerate(quick_qs):
        if chip_cols[i % 4].button(q, key=f"chip_{i}"):
            st.session_state.chat_history.append({"role":"user","msg":q})
            response = get_ai_response(q)
            st.session_state.chat_history.append({"role":"ai","msg":response})
            st.rerun()

    st.markdown("---")

    # ── CHAT HISTORY ─────────────────────────────────────
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.chat_history:
            now_str = datetime.datetime.now().strftime("%H:%M")
            if msg["role"] == "ai":
                st.markdown(f"""
                <div style="display:flex;gap:10px;margin-bottom:12px;align-items:flex-start">
                  <div style="width:30px;height:30px;border-radius:50%;
                  background:linear-gradient(135deg,#4F9EFF,#00D4AA);
                  display:flex;align-items:center;justify-content:center;
                  font-size:14px;flex-shrink:0;margin-top:2px">🧠</div>
                  <div style="max-width:85%">
                    <div style="background:#111B33;border:1px solid #1C2D50;
                    border-radius:3px 10px 10px 10px;padding:12px 14px;
                    font-size:12px;color:#A8C0E0;line-height:1.65">
                      {msg["msg"].replace(chr(10),"<br>").replace("**","<strong>").replace("**","</strong>")}
                    </div>
                    <div style="font-family:JetBrains Mono;font-size:8px;color:#2E4270;margin-top:3px;padding-left:4px">{now_str}</div>
                  </div>
                </div>""", unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="display:flex;justify-content:flex-end;margin-bottom:12px">
                  <div style="max-width:85%">
                    <div style="background:linear-gradient(135deg,#2575E8,#7C5CE8);
                    border-radius:10px 3px 10px 10px;padding:12px 14px;
                    font-size:12px;color:#fff;line-height:1.65">{msg["msg"]}</div>
                    <div style="font-family:JetBrains Mono;font-size:8px;color:#2E4270;
                    margin-top:3px;padding-right:4px;text-align:right">{now_str}</div>
                  </div>
                </div>""", unsafe_allow_html=True)

    # ── INPUT ─────────────────────────────────────────────
    st.markdown("---")
    col_in, col_btn = st.columns([5, 1])
    with col_in:
        user_input = st.text_input(
            label="",
            placeholder="Ask about VIX, AI signals, ARKK, systemic risk, portfolio strategy…",
            key="chat_input_field",
            label_visibility="collapsed"
        )
    with col_btn:
        send_clicked = st.button("Send ➤", key="chat_send_btn", use_container_width=True)

    if send_clicked and user_input.strip():
        st.session_state.chat_history.append({"role":"user","msg":user_input.strip()})
        response = get_ai_response(user_input.strip())
        st.session_state.chat_history.append({"role":"ai","msg":response})
        st.rerun()

    # ── CLEAR BUTTON ─────────────────────────────────────
    if st.button("🗑️  Clear conversation", key="chat_clear"):
        st.session_state.chat_history = [
            {"role":"ai","msg":"👋 Hello! I'm **Nexus AI**, your financial intelligence assistant. How can I help you today?"}
        ]
        st.rerun()

    # ── CAPABILITY LIST ──────────────────────────────────
    st.markdown("---")
    st.markdown('<div style="font-family:JetBrains Mono;font-size:8px;letter-spacing:2px;color:#2E4270;margin-bottom:10px">NEXUS AI CAPABILITIES</div>', unsafe_allow_html=True)
    cap_cols = st.columns(3)
    caps = [
        ("📊","Market Analysis","VIX interpretation, regime classification, drawdown analysis, cross-asset comparisons"),
        ("🤖","AI Model Insights","Random Forest vs LSTM accuracy, feature importance, confidence levels, bear/bull regime performance"),
        ("⚡","Risk Assessment","Systemic risk scoring, flash crash probability, algorithmic herding detection, cascade triggers"),
        ("💼","Portfolio Strategy","Asset allocation, P&L attribution, rebalancing signals, hedging recommendations"),
        ("🌍","Macro Intelligence","Yield curve analysis, central bank posture, global indices, inflation indicators"),
        ("📰","Sentiment Analysis","News scoring, ARK portfolio moves, narrative feedback loops, sentiment trends"),
    ]
    for i,(icon,title,desc) in enumerate(caps):
        cap_cols[i%3].markdown(f"""
        <div style="background:#0D1425;border:1px solid #1C2D50;border-radius:8px;padding:12px;margin-bottom:10px">
          <div style="font-size:18px;margin-bottom:5px">{icon}</div>
          <div style="font-size:12px;color:#D0E4FF;font-weight:500;margin-bottom:4px">{title}</div>
          <div style="font-size:10px;color:#4D6A9A;line-height:1.5">{desc}</div>
        </div>""", unsafe_allow_html=True)
