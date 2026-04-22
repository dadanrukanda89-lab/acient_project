import datetime

def record_learning(tier, lot, balance, status, reason):
    """
    Mencatat 'jalan pikiran' Acient Ghost ke dalam file log permanen.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = (
        f"[{timestamp}] TIER:{tier} | LOT:{lot} | BAL:Rp{balance:,} | "
        f"STATUS:{status} | REASON: {reason}\n"
    )
    
    # Simpan ke file agar laporan tidak hilang
    with open("acient_learning_report.log", "a") as f:
        f.write(log_entry)

# --- SIMULASI PENCATATAN ---
# Contoh jika sistem sedang belajar transisi
record_learning(
    tier=7, 
    lot=0.01, 
    balance=1000000000, 
    status="SIMULATION_LEARNING", 
    reason="Testing stability at Atto-Speed before real deployment."
)
