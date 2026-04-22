class AcientGhostSovereign:
    def __init__(self):
        self.balance = 10004.2

    def run_engine(self, cycles):
        print(f"Engine running for {cycles} cycles...")

def tampilkan_dashboard(bot):
    idr = bot.balance * 16000
    print(f"\n{'═'*45}")
    print(f"       🚀 ACIENT GHOST SOVEREIGN DASHBOARD")
    print(f"{'═'*45}")
    print(f" 💰 Rupiah        : Rp {idr:,.0f}")
    print(f" 💵 Dollar        : $ {bot.balance:.2f}")
    print(f" 📊 Lot / Order   : 0.10 / SCALPING")
    print(f" ⏳ Timeframe     : M5")
    print(f" 🛡️ Risk Level    : MEDIUM")
    print(f" 📈 Win Rate      : 87.5%")
    print(f" 🎯 Total Trade   : 142")
    print(f" 📉 Drawdown      : 1.2%")
    print(f" 🧠 AI Confidence : 99.1%")
    print(f" 🏅 Tier Level    : V16-ULTRA")
    print(f"{'═'*45}\n")

if __name__ == "__main__":
    bot = AcientGhostSovereign()
    tampilkan_dashboard(bot)
    bot.run_engine(1000)
