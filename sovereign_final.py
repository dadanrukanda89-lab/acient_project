# =========================================================
# ACIENT GHOST ULTIMATE
# v1011 NEUTRINO ATTO BOX ENGINE
# =========================================================

import time
import random
import os
from datetime import datetime

class AcientGhostSovereign:

    def __init__(self):
        # ================================
        # IDENTITAS
        # ================================
        self.version = "v1011_NEUTRINO_ATTO_BOX"
        self.identity = "ACIENT GHOST"

        self.vault_usd = 405273.85
        self.kurs_idr = 15500
        self.tier = 3

        # ================================
        # ENGINE CORE
        # ================================
        self.base_filter = 0.35
        self.risk_percent = 0.02
        self.anti_news_spike = 0.2

        # ================================
        # NEUTRINO + ATTO
        # ================================
        self.neutrino = 1e-12
        self.attodetik = 1e-18
        self.balance_speed = self.neutrino / self.attodetik

        # ================================
        # STATS
        # ================================
        self.stats = {
            "BUY": 0,
            "SELL": 0,
            "LOSS": 0
        }

        self.total_orders = 0
        self.session_profit = 0
        self.session_loss_count = 0

        self.min_lot = 0.01
        self.max_lot = 1.50

    # ================================
    # ATTO TIMER
    # ================================
    def atto_time(self):
        return time.perf_counter_ns() * self.attodetik

    # ================================
    # LOT OTOMATIS
    # ================================
    def calculate_lot(self):
        lot = round(self.vault_usd * 0.000002, 2)
        if lot < self.min_lot:
            lot = self.min_lot
        if lot > self.max_lot:
            lot = self.max_lot
        return lot

    # ================================
    # AUTO UPGRADE
    # ================================
    def auto_upgrade(self):
        self.tier += 1
        self.base_filter = max(0.05, self.base_filter - 0.01)
        self.anti_news_spike = min(0.5, self.anti_news_spike + 0.01)

    # ================================
    # BOTTOM STATUS BOX
    # ================================
    def bottom_box(self):
        print(
            f"\033[s\033[999;1H\033[44;37m "
            f"[ACIENT] "
            f"P:{self.session_profit:.2f} "
            f"L:{self.session_loss_count} "
            f"B:{self.stats['BUY']} "
            f"S:{self.stats['SELL']} "
            f"LOT:{self.calculate_lot()} "
            f"ORD:{self.total_orders} "
            f"TIER:{self.tier} "
            f"VAULT:${self.vault_usd:,.2f} "
            f"\033[0m\033[u",
            end="",
            flush=True
        )

    # ================================
    # HEADER
    # ================================
    def header(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        print("===================================================")
        print(f"ACIENT GHOST NEUTRINO ATTO ENGINE {self.version}")
        print(f"START VAULT: ${self.vault_usd:,.2f}")
        print("===================================================")

    # ================================
    # ENGINE RUNNER
    # ================================
    def run_engine(self, cycles=1000):
        self.header()

        for i in range(cycles):
            start = self.atto_time()
            now = datetime.now().strftime("%H:%M:%S")

            market = {
                "rsi": random.randint(0, 100),
                "sentiment": random.uniform(0, 1),
                "volatility": random.uniform(0, 1)
            }

            self.bottom_box()

            try:
                if market["sentiment"] < self.anti_news_spike:
                    continue

                if 35 < market["rsi"] < 65:
                    # LOSS SIMULATION (1% Chance)
                    if random.random() < 0.01:
                        loss_amount = self.vault_usd * 0.01
                        self.vault_usd -= loss_amount
                        self.session_loss_count += 1
                        self.stats["LOSS"] += 1
                        
                        self.auto_upgrade()
                        print(f"[{now}] \033[91mLOSS\033[0m -> AUTO UPGRADE TIER {self.tier}")
                        continue

                    # PROFIT SIMULATION
                    lot = self.calculate_lot()
                    side = "BUY" if market["rsi"] < 50 else "SELL"
                    
                    profit_usd = self.vault_usd * self.risk_percent
                    self.vault_usd += profit_usd
                    self.session_profit += profit_usd
                    
                    self.stats[side] += 1
                    self.total_orders += 1

                    print(f"[{now}] {side} | LOT {lot} | \033[92mSUCCESS\033[0m")

            except Exception as e:
                self.auto_upgrade()
                print(f"[{now}] CRASH ({e}) -> AUTO UPGRADE")

            end = self.atto_time()
            # Sinkronisasi kecepatan Atto
            time.sleep(0.01)

        self.final_report()

    # ================================
    # FINAL REPORT
    # ================================
    def final_report(self):
        profit_idr = self.session_profit * self.kurs_idr
        # Estimasi kerugian total berdasarkan hitungan loss
        loss_idr = self.stats["LOSS"] * (self.vault_usd * 0.01) * self.kurs_idr
        
        avg_profit_val = (self.vault_usd * self.risk_percent)
        total_buy_idr = self.stats["BUY"] * avg_profit_val * self.kurs_idr
        total_sell_idr = self.stats["SELL"] * avg_profit_val * self.kurs_idr

        print("\n\n")
        print("===================================================")
        print(f" FINAL REPORT - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("===================================================")
        
        print(f"Buy.......... : {self.stats['BUY']} | Rp{total_buy_idr:,.0f}")
        print(f"Sell......... : {self.stats['SELL']} | Rp{total_sell_idr:,.0f}")
        print(f"Sl (Loss).... : {self.stats['LOSS']}")
        print(f"Lot.......... : {self.calculate_lot()}")
        print(f"Order........ : {self.total_orders}")
        print(f"Tier......... : {self.tier}")
        
        print("---------------------------------------------------")
        print(f"Jumlah Profit Total.. : Rp{profit_idr:,.0f}")
        print(f"Jumlah Loss Total.... : Rp{loss_idr:,.0f}")
        print(f"Timeframe............ : NEUTRINO-ATTO SPEED")
        print(f"Upgrade.............. : LEVEL {self.tier} SUCCESSFUL")
        print("===================================================")
        print("➜  asient_project git:(main) ✗")

if __name__ == "__main__":
    bot = AcientGhostSovereign()
    # Menjalankan 1000 siklus trading
    bot.run_engine(1000)


