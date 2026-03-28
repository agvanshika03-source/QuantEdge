"""Nexus AI — Knowledge-base powered financial chatbot."""

KB = {
    "vix": """**VIX is currently at 31.05** — spiking +13.16% on Mar 27, 2026.

This puts us firmly in the **stressed regime (>25)**. The VIX climbed from a 52-week low of 13.38 (Dec 2025) to 31.05 driven by:
- Iran war escalation → geopolitical risk premium
- AI capex skepticism ($630B questioned)
- Algorithmic selling cascades amplifying moves

**Key levels to watch:**
- VIX > 35 = likely flash-crash cascade trigger
- VIX < 20 = regime normalization signal""",

    "regime": """**Current Market Regime: ELEVATED STRESS — 7.8 / 10**

All three ETFs declining simultaneously:
- SPY: −7.0% (90D) · −1.71% today
- QQQ: −9.8% (90D) · −1.95% today
- ARKK: −14.4% (90D) · −4.10% today

This synchronized decline with VIX >30 is the classic **algorithmic herding signature** — correlated sell programs overwhelming market-making capacity.

Regime classification: **Transitional / Risk-Increasing** (not full capitulation yet).""",

    "arkk": """**ARKK (ARK Innovation ETF) — Structural Decline**

Current: $64.63 | 90D: −14.4% | 1Y: +27.3%

Three drivers of the decline:
1. **AI capex skepticism** — $630B questioned by analysts
2. **High-beta rotation** — speculative tech unwound first
3. **Algorithmic synchronization** — ARKK has 2.67σ volatility vs 1.19σ for SPY

ARK is rotating internally:
- Selling: Nvidia, Roku, Airbnb
- Buying: Tempus AI, Arcturus Therapeutics, Circle Internet (healthcare AI pivot)

**52-week range:** $40.51 – $92.53""",

    "ai": """**Nifty AI Signal: 55% Upward Probability**

Random Forest model performance:
- Accuracy: **~55%** vs 52% naive baseline (+3pp edge)
- Bear regime accuracy: **62%** (best use case)
- Bull regime accuracy: **52%** (LSTM better here at 58%)
- Sentiment correlation: **~0.10** (weak — context only)

**Top features by importance:**
1. MA-30 crossover (0.78)
2. MA-90 signal (0.65)
3. 30-day momentum (0.45)

**Conclusion:** AI delivers incremental signal enhancement, not oracle-level prediction. Use with regime context — current risk-off regime reduces model reliability.""",

    "systemic": """**Top Systemic Risks — March 2026**

🔴 **Algorithmic Herding (ACTIVE)**
Models trained on identical datasets → synchronized decisions → liquidity vacuum when all sell simultaneously. Probability >70% when all ETFs decline + VIX spikes.

🔴 **Flash Crash Cascade (ELEVATED)**
Oct 2025 crypto: $9.9B wiped, 98% liquidity collapse in hours. QQQ <$555 or VIX >35 = cascade trigger.

🟡 **AI Narrative Feedback Loop (AMPLIFYING)**
Negative AI news → algo selling → decline → more negative coverage. Self-reinforcing cycle confirmed by Feb 2026 software rout ($1T wiped).

🟡 **Infrastructure Concentration**
Shared cloud/API dependencies = correlated failure risk across institutions.""",

    "buy": """**Strategic Posture: Defensive + Hedged**

Current regime (VIX >30, all ETFs declining) calls for:

✅ **ADD / MAINTAIN:**
- GLD — safe-haven, +18.4% 1Y, +0.92% today
- TLT — flight to quality as rates plateau
- SPY core — lower beta than QQQ

❌ **REDUCE:**
- ARKK — structural downtrend, 2.67σ vol
- High-beta tech positions
- Leveraged ETF exposure

⚠️ **HEDGE:**
- VIX calls / put options on QQQ or SPY
- Watch QQQ $555 support — break = cascade signal

👁️ **MONITOR:**
- Fed communications — "fog" signal suggests pivot timing uncertain
- VIX 35 trigger level
- Iran geopolitical resolution

*Note: Research analysis only — not personalised financial advice.*""",

    "portfolio": """**Portfolio Summary — Mar 27, 2026**

Total Value: **$2.48M** | Day P&L: **−$12.4K (−0.5%)**
Beta: **1.24** vs S&P 500 | Sharpe: **1.38**

Top performers (1Y):
- NVDA: +85.4% ($133.5K value)
- GLD: +18.1% ($240.2K value)
- QQQ: +4.2% ($337.5K value)

Laggards:
- ARKK: −24.1% (−$16.5K unrealised loss)

**Recommended rebalance:** Reduce ARKK by 50%, rotate into GLD and TLT given current risk regime.""",

    "macro": """**Macro Environment — March 2026**

🇺🇸 **Federal Reserve:** Rate 5.25–5.50%, on hold. Barkin cites "fog" from AI adoption + geopolitics making inflation/growth trajectory unclear.

📈 **Yield Curve:** 1M (5.21%) > 10Y (4.35%) — **inverted**, recession signal. 30Y at 4.62%.

💵 **Dollar (DXY):** 104.2, +0.34% today — geopolitical safe-haven bid.

🛢️ **Oil (WTI):** $78.40, +1.20% — Iran risk premium building.

🥇 **Gold:** $2,318/oz — +18.4% 1Y, acting as primary risk-off hedge.

🌍 **Global:** Nikkei +0.4% (diverging), Nifty −0.6%, FTSE −0.8%. EM stress building.""",

    "default": lambda q: f"""I've analysed your query: **"{q}"**

Based on QuantEdge Pro data (Mar 27, 2026):

**Current snapshot:**
- VIX: 31.05 (+13.16%) — Stressed regime
- SPY: $634.09 (−1.71%) · QQQ: $562.58 (−1.95%) · ARKK: $64.63 (−4.10%)
- AI Signal (Nifty RF): 55% upward probability — low confidence

**Market context:** All three ETFs in synchronized decline with VIX spiking — algorithmic herding pattern confirmed. Geopolitical risk (Iran) + AI capex doubts + Fed uncertainty = triple headwinds.

For deeper analysis try asking about:
- **VIX** or **volatility**
- **Market regime** or **risk**
- **ARKK** or specific ETFs
- **AI signal** or model performance
- **Systemic risks** or flash crash
- **Buy / sell** recommendations
- **Portfolio** or allocation
- **Macro** or bonds"""
}

def get_ai_response(question: str) -> str:
    q = question.lower().strip()
    if any(w in q for w in ["vix","volatil","fear index"]):
        return KB["vix"]
    if any(w in q for w in ["regime","market state","current market","stress","risk off"]):
        return KB["regime"]
    if any(w in q for w in ["arkk","cathie","ark etf","innovation etf"]):
        return KB["arkk"]
    if any(w in q for w in ["ai","signal","model","predict","random forest","lstm","nifty"]):
        return KB["ai"]
    if any(w in q for w in ["systemic","flash crash","herd","cascade","liquidity"]):
        return KB["systemic"]
    if any(w in q for w in ["buy","sell","invest","should i","position","trade","rebalance"]):
        return KB["buy"]
    if any(w in q for w in ["portfolio","holding","p&l","allocation","beta","sharpe"]):
        return KB["portfolio"]
    if any(w in q for w in ["macro","fed","rate","yield","inflation","bond","gold","oil","dollar","dxy"]):
        return KB["macro"]
    return KB["default"](question)
