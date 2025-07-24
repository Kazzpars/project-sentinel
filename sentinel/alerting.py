from datetime import datetime
# Tambahkan import untuk IPv6
from scapy.all import IP, IPv6

# Path ke file log
LOG_FILE_PATH = 'logs/alerts.log'

def trigger_alert(rule, packet):
    """
    Mencatat peringatan ke konsol dan file log.
    Kini mendukung IPv4 dan IPv6.
    """
    src_ip = 'N/A'
    dst_ip = 'N/A'

    # --- BAGIAN YANG DIPERBAIKI ---
    # Cek apakah paket memiliki layer IPv4 atau IPv6 untuk mendapatkan IP
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
    elif packet.haslayer(IPv6):
        src_ip = packet[IPv6].src
        dst_ip = packet[IPv6].dst
    # -----------------------------
    
    # Membuat pesan peringatan
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    alert_message = rule['message'].replace('IP sumber', str(src_ip))
    
    log_entry = f"[{timestamp}] - [Rule: {rule['name']}] - {alert_message} -> (Source: {src_ip}, Dest: {dst_ip})"
    
    # 1. Cetak ke konsol
    print(f"\033[91m{log_entry}\033[0m") # Mencetak dengan warna merah

    # 2. Tulis ke file log
    try:
        with open(LOG_FILE_PATH, 'a') as log_file:
            log_file.write(log_entry + '\n')
    except IOError as e:
        print(f"[!] Gagal menulis ke file log: {e}")

# Path ke file log
LOG_FILE_PATH = 'logs/alerts.log'

def trigger_alert(rule, packet):
    """
    Mencatat peringatan ke konsol dan file log.
    """
    # Mendapatkan informasi dasar dari paket
    src_ip = packet[0][1].src if packet.haslayer('IP') else 'N/A'
    dst_ip = packet[0][1].dst if packet.haslayer('IP') else 'N/A'
    
    # Membuat pesan peringatan
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    alert_message = rule['message'].replace('IP sumber', src_ip)
    
    log_entry = f"[{timestamp}] - [Rule: {rule['name']}] - {alert_message} -> (Source: {src_ip}, Dest: {dst_ip})"
    
    # 1. Cetak ke konsol
    print(f"\033[91m{log_entry}\033[0m") # Mencetak dengan warna merah

    # 2. Tulis ke file log
    try:
        with open(LOG_FILE_PATH, 'a') as log_file:
            log_file.write(log_entry + '\n')
    except IOError as e:
        print(f"[!] Gagal menulis ke file log: {e}")