import os
import sys
import time

def start_brutal_session():
    # 1. SETUP ENVIRONMENT TANPA UBAH KODE ASLI
    print("--- [INITIALIZING ACIENT HELL MODE] ---")
    time.sleep(1)
    
    # 2. RUN MASTER GHOST DENGAN OVERRIDE LOGIC
    # Kita panggil file asli kamu sebagai subprocess
    try:
        os.system("python3 master_ghost.py --mode=brutal --perf=10x")
    except KeyboardInterrupt:
        print("\n[SYSTEM] Session Locked & Saved.")

if __name__ == "__main__":
    start_brutal_session()
