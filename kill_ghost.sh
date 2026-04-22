#!/bin/bash
# Mematikan semua aktivitas bot dan sesi gaib seketika
pkill -9 screen
pkill -9 python
pkill -9 python3
termux-wake-release
echo "=========================================="
echo " [!] EMERGENCY: GHOST SYSTEM TERMINATED"
echo " [!] SEMUA KONEKSI & ENGINE TELAH MATI"
echo "=========================================="
