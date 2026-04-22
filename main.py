import time
import importlib
from sub_acient import quantum_core

class AcientEngine:
    def __init__(self):
        print("\n" + "="*30)
        print("   ACIENT CORE SYSTEM ACTIVE")
        print("="*30)
        self.brain = quantum_core.QuantumBrain()
        self.running = True

    def check_upgrade(self):
        """Fungsi reload otomatis"""
        try:
            importlib.reload(quantum_core)
            self.brain = quantum_core.QuantumBrain()
            print(f"🔄 [AUTO-UPGRADE] Versi Brain: {self.brain.version}")
        except Exception as e:
            print(f"⚠️ Gagal upgrade: {e}")

    def start(self):
        count = 0
        while self.running:
            if count % 5 == 0: # Cek upgrade tiap 5 cycle
                self.check_upgrade()

            signal = self.brain.get_signal()
            print(f"[{time.strftime('%H:%M:%S')}] Cycle: {count} | Signal: {signal}")
            
            count += 1
            time.sleep(2)

if __name__ == "__main__":
    engine = AcientEngine()
    engine.start()
