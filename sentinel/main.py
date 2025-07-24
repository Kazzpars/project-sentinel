from scapy.all import sniff
from sentinel.rules_manager import load_rules
from sentinel.analyzer import analyze_packet

def start_sentinel():
    """
    Fungsi utama untuk memulai Project Sentinel.
    """
    print("==========================================")
    print("🚀 Project Sentinel Dimulai...")
    print("==========================================")
    
    # 1. Muat semua aturan dari file config
    active_rules = load_rules()
    
    if not active_rules:
        print("[!] Tidak ada aturan yang aktif, Sentinel berhenti.")
        return
        
    # 2. Buat fungsi callback analyzer dengan aturan yang sudah dimuat
    packet_analyzer_callback = analyze_packet(active_rules)

    # 3. Mulai menangkap paket dan serahkan ke analyzer
    print("\n[*] Memulai penangkapan paket. Tekan CTRL+C untuk berhenti.")
    try:
        # sniff() akan menangkap paket tanpa batas
        # prn adalah fungsi callback yang akan dijalankan untuk setiap paket
        # store=0 berarti kita tidak menyimpan paket dalam memori
        sniff(prn=packet_analyzer_callback, store=0)
    except KeyboardInterrupt:
        print("\n[!] Penangkapan paket dihentikan oleh pengguna.")
    except Exception as e:
        print(f"\n[!] Terjadi error: {e}")
    finally:
        print("==========================================")
        print("👋 Project Sentinel Berhenti.")
        print("==========================================")

if __name__ == "__main__":
    # Kode ini hanya akan berjalan jika file main.py dieksekusi secara langsung
    start_sentinel()