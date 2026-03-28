import numpy as np

# ─── RAW PRICE DATA ────────────────────────────────────
DATES = ['Nov 17','Nov 18','Nov 19','Nov 20','Nov 21','Nov 24','Nov 25','Nov 26','Nov 28',
 'Dec 1','Dec 2','Dec 3','Dec 4','Dec 5','Dec 8','Dec 9','Dec 10','Dec 11','Dec 12',
 'Dec 15','Dec 16','Dec 17','Dec 18','Dec 19','Dec 22','Dec 23','Dec 24','Dec 26','Dec 29',
 'Dec 30','Dec 31','Jan 2','Jan 5','Jan 6','Jan 7','Jan 8','Jan 9','Jan 12','Jan 13',
 'Jan 14','Jan 15','Jan 16','Jan 20','Jan 21','Jan 22','Jan 23','Jan 26','Jan 27','Jan 28',
 'Jan 29','Jan 30','Feb 2','Feb 3','Feb 4','Feb 5','Feb 6','Feb 9','Feb 10','Feb 11',
 'Feb 12','Feb 13','Feb 17','Feb 18','Feb 19','Feb 20','Feb 23','Feb 24','Feb 25','Feb 26',
 'Feb 27','Mar 2','Mar 3','Mar 4','Mar 5','Mar 6','Mar 9','Mar 10','Mar 11','Mar 12',
 'Mar 13','Mar 16','Mar 17','Mar 18','Mar 19','Mar 20','Mar 23','Mar 24','Mar 25','Mar 26','Mar 27']

QQQ_RAW = [603.66,596.31,599.87,585.67,590.07,605.16,608.89,614.27,619.25,617.17,622,623.52,
 622.94,625.48,624.28,625.05,627.61,625.58,613.62,610.54,611.75,600.41,609.11,617.05,619.21,
 622.11,623.93,623.89,620.87,619.43,614.31,613.12,617.99,623.42,624.02,620.47,626.65,627.17,
 626.24,619.55,621.78,621.26,608.06,616.28,620.76,622.72,625.46,631.13,633.22,629.43,621.87,
 626.14,616.52,605.75,597.03,609.65,614.32,611.47,613.11,600.64,601.92,601.3,605.79,603.47,
 608.81,601.41,607.87,616.68,609.24,607.29,608.09,601.58,610.75,608.91,599.75,607.76,607.77,
 607.69,597.26,593.72,600.38,603.31,594.9,593.02,582.06,588,583.98,587.82,573.79,562.58]

SPY_RAW = [660.08,662.63,652.53,659.03,668.73,675.02,679.68,683.39,680.27,681.53,683.89,684.39,
 685.69,683.63,683.04,687.57,689.17,681.76,680.73,678.87,671.4,676.47,680.59,684.83,687.96,
 690.38,690.38,690.31,687.85,687.01,681.92,683.17,687.72,691.81,689.58,689.51,694.07,695.16,
 693.77,690.36,692.24,691.66,677.58,685.4,688.98,689.23,692.73,695.49,695.42,694.04,691.97,
 695.41,689.53,686.19,677.62,690.62,693.95,692.12,691.96,681.27,681.75,682.85,686.29,684.48,
 689.43,682.39,687.35,693.15,689.3,685.99,686.38,680.33,685.13,681.31,672.38,678.27,677.18,
 676.33,666.06,662.29,669.03,670.79,661.43,659.8,648.57,655.38,653.18,656.82,645.09,634.09]

ARKK_RAW = [75.49,74.97,74.39,71.75,73.35,76.79,77.3,78.47,79.68,77.53,78.22,80.75,82.65,81.91,
 81.96,82.53,83.16,82.06,80.39,79.21,80.14,77.7,78.69,80.3,81.49,80.51,80.65,79.7,78.61,77.87,
 76.92,78.31,81.34,81.86,81.14,80.55,80.29,82.54,83.21,83.2,81.93,81.68,79.23,80.29,82.23,80.7,
 79.92,79.77,78.94,77.64,74.87,74.36,73.44,69.99,66.33,70.41,72.44,72.26,70.87,68.45,70.25,70.3,
 71.39,72.24,71.49,70,72.07,73.54,74.61,72.91,74.22,72.26,74.93,73.99,72.4,74.29,72.89,73.07,
 70.64,70.25,72.05,73.06,71.41,71.07,69.15,70.92,69,69.9,67.39,64.63]

VIX_RAW = [23.43,20.52,18.56,17.19,17.21,16.35,17.24,16.59,16.08,15.78,15.41,16.66,16.93,15.77,
 14.85,15.74,16.5,16.48,17.62,16.87,14.91,14.08,14,13.47,13.6,14.2,14.33,14.95,14.95,14.51,14.9,
 14.75,15.38,15.45,14.49,15.12,15.98,16.75,15.84,15.86,18.84,20.09,16.9,15.64,16.09,16.15,16.35,
 16.35,16.88,17.44,16.34,18,18.64,21.77,17.76,17.36,17.79,17.65,20.82,20.6,21.2,20.29,19.62,20.23,
 19.09,21.01,19.55,17.93,18.63,19.86,21.44,23.57,21.15,23.75,29.49,25.5,24.93,24.23,27.29,27.19,
 23.51,22.37,25.09,24.06,26.78,26.15,26.95,25.33,27.44,31.05]

# ─── DERIVED DATA ──────────────────────────────────────
def compute_norm(arr):
    base = arr[0]
    return [round((v / base - 1) * 100, 2) for v in arr]

def compute_ma(arr, n):
    result = []
    for i in range(len(arr)):
        if i < n - 1:
            result.append(None)
        else:
            result.append(round(sum(arr[i-n+1:i+1]) / n, 2))
    return result

def compute_rolling_vol(arr, n=20):
    result = []
    for i in range(len(arr)):
        if i < n:
            result.append(None)
        else:
            sl = arr[i-n:i]
            rets = [(sl[j]/sl[j-1]-1)*100 for j in range(1,len(sl))]
            mean = sum(rets)/len(rets)
            var  = sum((r-mean)**2 for r in rets)/len(rets)
            result.append(round(var**0.5 * (252**0.5), 2))
    return result

def compute_rsi(arr, n=14):
    result = [None]*len(arr)
    if len(arr) <= n:
        return result
    gains, losses = 0, 0
    for i in range(1, n+1):
        d = arr[i] - arr[i-1]
        if d >= 0: gains += d
        else:      losses -= d
    avg_g, avg_l = gains/n, losses/n
    result[n] = round(100 - 100/(1 + avg_g/avg_l) if avg_l != 0 else 100, 1)
    for i in range(n+1, len(arr)):
        d = arr[i] - arr[i-1]
        g = d if d > 0 else 0
        l = -d if d < 0 else 0
        avg_g = (avg_g*(n-1) + g) / n
        avg_l = (avg_l*(n-1) + l) / n
        result[i] = round(100 - 100/(1 + avg_g/avg_l) if avg_l != 0 else 100, 1)
    return result

def simulate_intraday(base, vol=0.003, n=78):
    np.random.seed(42)
    prices, times = [], []
    p = base * (1 + (np.random.random()-0.52)*0.008)
    for i in range(n):
        p += p * (np.random.random()-0.505) * vol
        prices.append(round(p, 2))
        h  = int(9.5 + i*6.5/n)
        m  = round((9.5 + i*6.5/n - h)*60)
        times.append(f"{h}:{m:02d}")
    return prices, times

def get_all_data():
    return {
        "DATES":    DATES,
        "QQQ":      QQQ_RAW,
        "SPY":      SPY_RAW,
        "ARKK":     ARKK_RAW,
        "VIX":      VIX_RAW,
        "QQQ_norm": compute_norm(QQQ_RAW),
        "SPY_norm": compute_norm(SPY_RAW),
        "ARKK_norm":compute_norm(ARKK_RAW),
        "QQQ_ma20": compute_ma(QQQ_RAW, 20),
        "QQQ_ma50": compute_ma(QQQ_RAW, 50),
        "SPY_ma20": compute_ma(SPY_RAW, 20),
        "SPY_ma50": compute_ma(SPY_RAW, 50),
        "QQQ_rvol": compute_rolling_vol(QQQ_RAW),
        "SPY_rvol": compute_rolling_vol(SPY_RAW),
        "ARKK_rvol":compute_rolling_vol(ARKK_RAW),
        "QQQ_rsi":  compute_rsi(QQQ_RAW),
        "QQQ_intraday": simulate_intraday(562.58, 0.003),
        "SPY_intraday": simulate_intraday(634.09, 0.0025),
    }

# ─── STATIC DATA ───────────────────────────────────────
TICKERS = [
    {"sym":"SPY",   "price":"634.09","chg":"-1.71%","up":False},
    {"sym":"QQQ",   "price":"562.58","chg":"-1.95%","up":False},
    {"sym":"ARKK",  "price":"64.63", "chg":"-4.10%","up":False},
    {"sym":"VIX",   "price":"31.05", "chg":"+13.16%","up":False},
    {"sym":"AAPL",  "price":"178.20","chg":"+0.34%","up":True},
    {"sym":"MSFT",  "price":"392.50","chg":"-0.82%","up":False},
    {"sym":"NVDA",  "price":"890.00","chg":"-2.10%","up":False},
    {"sym":"GLD",   "price":"218.40","chg":"+0.92%","up":True},
    {"sym":"DXY",   "price":"104.2", "chg":"+0.34%","up":True},
    {"sym":"BTC",   "price":"68,420","chg":"-2.80%","up":False},
    {"sym":"10Y",   "price":"4.35%", "chg":"-2bp",  "up":True},
    {"sym":"WTI",   "price":"78.40", "chg":"+1.20%","up":True},
    {"sym":"NIFTY", "price":"22,140","chg":"-0.6%", "up":False},
]

SECTOR_DATA = [
    {"name":"Technology",  "ret":-8.2},{"name":"Healthcare",  "ret":1.4},
    {"name":"Financials",  "ret":-3.8},{"name":"Energy",      "ret":4.2},
    {"name":"Consumer",    "ret":-5.1},{"name":"Utilities",   "ret":2.8},
    {"name":"Materials",   "ret":-1.2},{"name":"Industrials", "ret":-0.4},
    {"name":"Real Estate", "ret":-6.8},{"name":"Telecom",     "ret":-2.1},
    {"name":"Staples",     "ret":0.8}, {"name":"AI / Tech",   "ret":-11.4},
]

HOLDINGS = [
    {"sym":"AAPL","name":"Apple Inc",         "shares":420, "cost":162.40,"curr":178.20,"val":74844},
    {"sym":"MSFT","name":"Microsoft",          "shares":280, "cost":310.00,"curr":392.50,"val":109900},
    {"sym":"NVDA","name":"NVIDIA Corp",        "shares":150, "cost":480.00,"curr":890.00,"val":133500},
    {"sym":"ARKK","name":"ARK Innovation ETF", "shares":800, "cost":85.20, "curr":64.63, "val":51704},
    {"sym":"QQQ", "name":"Invesco QQQ",        "shares":600, "cost":540.00,"curr":562.58,"val":337548},
    {"sym":"GLD", "name":"Gold ETF",           "shares":1100,"cost":185.00,"curr":218.40,"val":240240},
    {"sym":"TLT", "name":"20Y Treasury Bond",  "shares":900, "cost":88.50, "curr":92.10, "val":82890},
]

NEWS_ITEMS = [
    {"hl":"Investors cling to shock-absorber trades as Iran war brings economic visibility to zero",            "src":"Reuters · Mar 27","tag":"BEARISH","bear":True},
    {"hl":"JPMorgan trims S&P 500 year-end estimate on Middle East supply risks",                              "src":"Bloomberg · Mar 27","tag":"DOWNGRADE","bear":True},
    {"hl":"US equity funds post biggest outflows in 8 weeks on geopolitical worries",                          "src":"Reuters · Mar 27","tag":"OUTFLOWS","bear":True},
    {"hl":"Cathie Wood's ARK sells Nvidia, buys Arcturus Therapeutics — healthcare AI pivot",                  "src":"Investing.com · Mar 27","tag":"ROTATION","bear":None},
    {"hl":"ARK trims Roku, buys Tempus AI — AI-health convergence bet",                                        "src":"Investing.com · Mar 25","tag":"ROTATION","bear":None},
    {"hl":"Big Tech's $630B AI splurge projected to fall short of return expectations",                        "src":"Reuters · Mar 26","tag":"AI MACRO","bear":True},
    {"hl":"Fed's Barkin: 'Fog' obscures outlook — AI + geopolitics compound uncertainty",                      "src":"Reuters · Mar 27","tag":"FED","bear":True},
    {"hl":"ECB: AI may boost euro area productivity by 4% over 10 years",                                      "src":"Reuters · Mar 23","tag":"BULLISH LT","bear":False},
    {"hl":"Dip-buyers go missing as software selloff slams stocks — $1T value wiped",                          "src":"Reuters · Feb 4","tag":"SECTOR RISK","bear":True},
    {"hl":"BlackRock's Fink warns AI could widen wealth divide without broad participation",                    "src":"Reuters · Mar 23","tag":"STRUCTURAL","bear":None},
]
