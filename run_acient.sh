#!/bin/bash
while true
do
    # 1. Jalankan Master Engine menggunakan PyPy3
    # Kita arahkan output ke file sementara agar terminal tidak hang
    pypy3 master_ghost.py > session_temp.log 2>&1
    
    # 2. Bersihkan layar terminal (Kunci Anti-Lag)
    clear
    
    # 3. Tampilkan identitas dan laporan terakhir
    echo "==========================================="
    echo "   [ ACIENT GHOST ] - MASTER ENGINE ACTIVE"
    echo "   Operator: drukanda | Device: ThinkPad/HP"
    echo "   Waktu: $(date)"
    echo "==========================================="
    
    # Tampilkan 15 baris terakhir dari laporan master
    tail -n 15 session_temp.log
    
    # 4. Amankan laporan ke log utama
    cat session_temp.log >> acient_learning_report.log
    
    # 5. Hapus sampah sesi agar disk tetap lega
    rm session_temp.log
    
    # Jeda 1 detik agar laporan sempat terbaca sebelum layar dibersihkan lagi
    sleep 1
done
