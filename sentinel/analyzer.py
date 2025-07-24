from scapy.layers.inet import TCP, ICMP
from .alerting import trigger_alert # Mengimpor fungsi trigger_alert dari file alerting.py

def analyze_packet(rules):
    """
    Fungsi closure yang mengembalikan fungsi penganalisis paket.
    Ini memungkinkan kita untuk melewatkan 'rules' ke dalam callback Scapy.
    """
    def packet_callback(packet):
        """
        Fungsi ini akan dipanggil untuk setiap paket yang ditangkap oleh Scapy.
        """
        for rule in rules:
            # Pengecekan Protokol
            if rule['protocol'].upper() == 'TCP' and packet.haslayer(TCP):
                if check_match(packet[TCP], rule['match']):
                    trigger_alert(rule, packet)
            
            elif rule['protocol'].upper() == 'ICMP' and packet.haslayer(ICMP):
                if check_match(packet[ICMP], rule['match']):
                    trigger_alert(rule, packet)
                    
    return packet_callback

def check_match(layer, match_conditions):
    """
    Memeriksa apakah sebuah layer paket cocok dengan kondisi dalam aturan.
    """
    for condition, value in match_conditions.items():
        if not hasattr(layer, condition) or str(getattr(layer, condition)) != str(value):
            return False
    return True