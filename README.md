## 🛡️ Project Sentinel
Sistem Deteksi Intrusi Jaringan Sederhana Berbasis Aturan (Simple Rule-Based NIDS) dengan Python

Project Sentinel adalah sebuah sistem deteksi intrusi jaringan (NIDS) sederhana yang ditulis dengan Python. Tujuannya adalah untuk memonitor lalu lintas jaringan secara real-time dan mendeteksi aktivitas mencurigakan berdasarkan seperangkat aturan yang dapat disesuaikan. Proyek ini sangat cocok untuk tujuan edukasi, yaitu untuk mempelajari konsep dasar keamanan siber dan pemrograman jaringan.

## ✨Fitur Utama
1. Packet Sniffing Real-Time: Menangkap dan menganalisis paket jaringan secara langsung.
2. Rule-Based Detection Engine: Mesin deteksi yang fleksibel berdasarkan aturan yang Anda tentukan.
3. Kustomisasi Aturan dengan JSON: Mudah menambah, mengubah, dan menghapus aturan deteksi melalui file config/rules.json.
4. Logging Peringatan: Semua peringatan akan ditampilkan di konsol dan dicatat ke dalam file logs/alerts.log untuk analisis di kemudian hari.

## ⚙️ Cara Kerja
Sentinel bekerja dengan menangkap setiap paket yang melewati antarmuka jaringan. Untuk setiap paket, Sentinel akan:
* Membaca Aturan: Memuat semua aturan yang didefinisikan di config/rules.json.
* Menganalisis Paket: Membandingkan karakteristik paket (seperti protokol, alamat IP, port, dll.) dengan setiap aturan yang ada.
* Memicu Peringatan: Jika sebuah paket cocok dengan kriteria sebuah aturan, Sentinel akan menghasilkan sebuah peringatan (alert) yang berisi detail dari ancaman yang terdeteksi.

## 🚀 Memulai Proyek
Berikut adalah panduan untuk menyiapkan dan menjalankan Project Sentinel di komputer Anda.
### Prasyarat:
- Python 3.8+
- pip & venv
- Git
### (Penting untuk Windows) Npcap: Sentinel membutuhkan Npcap untuk menangkap paket di Windows. Unduh dan install dari situs resmi Npcap. Saat instalasi, pastikan Anda mencentang opsi "Install Npcap in WinPcap API-compatible Mode".

## Instalasi
- Clone repository ini (atau buat folder proyek Anda):
- Bash
- git clone [URL_REPOSITORY_ANDA]
- cd project-sentinel
- Buat dan aktifkan virtual environment:
- Bash

# Membuat venv
```python -m venv venv```

# Mengaktifkan di Windows (PowerShell)
```.\venv\Scripts\Activate.ps1```

# Mengaktifkan di macOS/Linux
```source venv/bin/activate```
Install semua dependensi:
Pastikan Anda memiliki file ```requirements.txt``` yang berisi scapy. Jika belum, buat dengan perintah: ```pip freeze > requirements.txt``` setelah menginstall scapy.

Bash

```pip install -r requirements.txt```

### Menjalankan Sentinel
Untuk menjalankan program, Anda mungkin memerlukan hak akses administrator untuk mengizinkan penangkapan paket jaringan.

Di Windows: Buka PowerShell sebagai Administrator.

Di macOS/Linux: Gunakan ```sudo```
Bash

# Untuk macOS/Linux
``` sudo python -m sentinel.main  ```

# Untuk Windows (di PowerShell Administrator)
```python -m sentinel.main ```
Sentinel akan mulai memonitor jaringan. Untuk menghentikannya, tekan CTRL + C.

룰 Konfigurasi Aturan (rules.json)
Anda bisa mendefinisikan aturan deteksi Anda sendiri di dalam file config/rules.json.

Contoh isi file config/rules.json:

``` JSON

[
  {
    "rule_id": 1001,
    "name": "TCP SYN Scan (Stealth Scan)",
    "protocol": "TCP",
    "match": {
      "flags": "S"
    },
    "message": "ALERT: Terdeteksi percobaan TCP SYN Scan dari IP sumber"
  },
  {
    "rule_id": 1002,
    "name": "FTP Login Attempt",
    "protocol": "TCP",
    "match": {
      "dport": 21
    },
    "message": "ALERT: Terdeteksi percobaan koneksi ke port FTP (21) dari IP sumber"
  },
  {
    "rule_id": 2001,
    "name": "ICMP Echo Request (Ping)",
    "protocol": "ICMP",
    "match": {
      "type": 8
    },
    "message": "INFO: Terdeteksi ICMP Echo Request (Ping) dari IP sumber"
  }
]
```

## 📁 Struktur Proyek
``` project-sentinel/
├── config/
│   └── rules.json
├── logs/
│   └── alerts.log
├── sentinel/
│   ├── __init__.py
│   ├── main.py
│   ├── analyzer.py
│   ├── rules_manager.py
│   └── alerting.py
├── tests/
├── .gitignore
├── README.md
└── requirements.txt
```

Jika ada kritik dan saran, silahkan!
