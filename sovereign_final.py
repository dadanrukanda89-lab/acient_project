import numpy as np
import matplotlib.pyplot as plt
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# =====================================
# ACIENT GHOST & PHYSICS ENGINE (ORIGINAL)
# =====================================
class AcientGhost:
    def __init__(self, num_events=1000):
        self.detector_size = 6000
        self.sources = ["dark", "cosmic", "solar", "quantum", "anti_neutrino"]
        self.eop_x = 0.5 * np.sin(np.linspace(0, 10, num_events)) + np.random.normal(0, 0.05, num_events)
        self.eop_y = 0.5 * np.cos(np.linspace(0, 10, num_events)) + np.random.normal(0, 0.05, num_events)
        self.events = []
        self.types = []

    def simulate_physics(self):
        # Logika Anti-Neutrino & EOP
        source = np.random.choice(self.sources)
        ex = self.eop_x[random.randint(0, 999)]
        energy = np.random.exponential(100) if source == "anti_neutrino" else np.abs(np.random.normal(300, 100))
        return source, energy, ex

# =====================================
# FUNDAMENTAL TRADING ENGINE v4 (ORIGINAL)
# =====================================
class FundAI:
    def __init__(self):
        self.balance = 10000
        self.risk = 0.01
        self.win = 0
        self.loss = 0
        self.evolution = 1
        self.risk_mode = "NORMAL"
        self.ghost = AcientGhost()

    def rsi(self): return np.random.randint(20, 80)

    def bollinger(self):
        price = np.random.normal(1.2000, 0.01)
        return price, price + 0.002, price - 0.002

    def trend(self): return random.choice(["UP", "DOWN", "SIDEWAYS"])

    def news_sentiment(self):
        news = ["positive_economy", "interest_rate_hike", "war_risk", "inflation_drop", 
                "political_stable", "crisis", "growth", "recession_fear"]
        return random.choice(news)

    def sentiment_score(self, news):
        mapping = {"positive_economy": 0.8, "interest_rate_hike": -0.6, "war_risk": -0.9,
                   "inflation_drop": 0.7, "political_stable": 0.6, "crisis": -1.0, 
                   "growth": 0.9, "recession_fear": -0.8}
        return mapping.get(news, 0)

    def lot_size(self):
        base = self.balance * self.risk
        scale = 1 + (self.evolution * 0.05)
        lot = base * scale
        return min(lot, self.balance * 0.03)

    def auto_repair(self):
        # Protokol ONE STRIKE OUT
        print("\n[!] ONE STRIKE OUT ACTIVATED: REPAIRING SYSTEM...")
        self.evolution = 1
        self.risk_mode = "SAFE"

    def decision(self):
        # FUSION BRAIN: Technical + Fundamental + Physics
        rsi_val = self.rsi()
        price, upper, lower = self.bollinger()
        trnd = self.trend()
        news = self.news_sentiment()
        sentiment = self.sentiment_score(news)
        
        # Physics Filter (Acient Ghost)
        source, energy, eop_val = self.ghost.simulate_physics()
        
        score = 0
        if rsi_val < 30: score += 1
        if rsi_val > 70: score -= 1
        if price < lower: score += 1
        if price > upper: score -= 1
        if trnd == "UP": score += 0.5
        elif trnd == "DOWN": score -= 0.5
        
        score += sentiment
        
        # Anti-Neutrino Filter: Jika energi terlalu liar, kurangi skor (Market Noise)
        if source == "anti_neutrino" and energy > 150:
            score *= 0.5 
            
        if score > 1: return "BUY", score, eop_val
        elif score < -1: return "SELL", score, eop_val
        else: return "WAIT", score, eop_val

    def trade(self, i):
        signal, score, eop_val = self.decision()
        if signal == "WAIT": return None

        lot = self.lot_size()
        result = np.random.normal(0, 1)

        print(f"\n--- TRADE EVENT {i} ---")
        print(f"Signal: {signal} | Score: {round(score,2)} | EOP: {round(eop_val,3)}")
        
        if result > 0:
            profit = lot * 0.02
            self.balance += profit
            self.win += 1
            print(f"WIN +{round(profit,2)}")
        else:
            loss = lot * 0.01
            self.balance -= loss
            self.loss += 1
            print(f"LOSS -{round(loss,2)}")
            self.auto_repair()
            self.evolution += 1

        print(f"Balance: {round(self.balance,2)} | Mode: {self.risk_mode}")
        return eop_val

# =====================================
# RUN & VISUALIZATION (EOP CHART)
# =====================================
ai = FundAI()
plt.ion()
fig, ax = plt.subplots(figsize=(7, 6))
eop_history_x = []
eop_history_y = []

for i in range(60):
    eop_val = ai.trade(i)
    
    # Update Chart EOP agar tidak berantakan
    if eop_val is not None:
        eop_history_x.append(eop_val)
        eop_history_y.append(0.5 * np.cos(i * 0.1)) # Simulasi Y axis
        
        ax.clear()
        ax.set_title("ACIENT GHOST MONITOR - EOP PHYSICS")
        ax.plot(eop_history_x, eop_history_y, color='lime', alpha=0.4, label="Earth Orientation Path")
        ax.scatter(eop_history_x[-1], eop_history_y[-1], color='red', s=100, label="Current Position")
        ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5)
        ax.legend()
        plt.pause(0.05)

plt.ioff()
print("\n" + "="*30)
print(f"FINAL BALANCE: {round(ai.balance, 2)}")
print(f"TOTAL WIN: {ai.win} | LOSS: {ai.loss}")
print("="*30)
plt.show()
