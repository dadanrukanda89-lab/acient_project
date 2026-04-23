import os
import time

# Ambil data dari Variables Railway
LOGIN = os.getenv('EXNESS_LOGIN')
PASSWORD = os.getenv('EXNESS_PASSWORD')
SERVER = os.getenv('EXNESS_SERVER')

def connect_to_exness():
    print(f"[SYSTEM] Memulai Acient Ghost...")
    print(f"[AUTH] Mencoba login ke akun: {LOGIN}")
    print(f"[AUTH] Server: {SERVER}")
    
    # Simulasi koneksi (nanti bagian ini akan diganti library MT5)
    if LOGIN and PASSWORD:
        print(f"[SUCCESS] Login Berhasil! Menghubungkan ke Saldo Demo...")
        print(f"[INFO] Monitoring Saldo: 10,000.00 USD")
        return True
    else:
        print("[ERROR] Data Login tidak ditemukan di Variables Railway!")
        return False

if __name__ == "__main__":
    if connect_to_exness():
        while True:
            print("[TRADING] Acient Ghost sedang memantau market...")
            time.sleep(60) # Cek tiap 1 menit
