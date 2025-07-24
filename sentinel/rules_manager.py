import json
import sys

# Path ke file rules.json relatif terhadap folder root proyek
RULES_FILE_PATH = 'config/rules.json'

def load_rules():
    """
    Membaca dan mem-parse file rules.json.
    Mengembalikan daftar aturan (list of dictionaries).
    """
    try:
        with open(RULES_FILE_PATH, 'r') as f:
            print(f"[*] Memuat aturan dari {RULES_FILE_PATH}...")
            rules = json.load(f)
            print(f"[+] {len(rules)} aturan berhasil dimuat.")
            return rules
    except FileNotFoundError:
        print(f"[!] Error: File aturan tidak ditemukan di '{RULES_FILE_PATH}'")
        sys.exit(1) # Keluar dari program jika file aturan tidak ada
    except json.JSONDecodeError:
        print(f"[!] Error: Format JSON dalam '{RULES_FILE_PATH}' tidak valid.")
        sys.exit(1)