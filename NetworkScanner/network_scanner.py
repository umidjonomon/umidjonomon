import socket
import threading
import os

# ✅ IP-ga ping tashlash funksiyasi
def ping_ip(ip):
    response = os.system(f"ping -n 1 {ip} > nul")
    return response == 0  # Agar 0 qaytsa, IP aktiv

# ✅ IP dagi ochiq portlarni tekshirish funksiyasi
def scan_ports(ip, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        if sock.connect_ex((ip, port)) == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

# ✅ Barcha IP-larni skanerlash funksiyasi
def scan_network(ip_base):
    print(f"🔍 {ip_base}.X tarmog‘idagi barcha aktiv IP-larni aniqlash...")
    
    active_ips = []
    threads = []

    def thread_ping(ip):
        if ping_ip(ip):
            print(f"✅ Aktiv IP topildi: {ip}")
            active_ips.append(ip)

    # 1-254 oralig‘idagi barcha IP-larni tekshiramiz
    for i in range(1, 255):
        ip = f"{ip_base}.{i}"
        t = threading.Thread(target=thread_ping, args=(ip,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n✅ Aktiv IP-larni tekshirish tugadi. Portlarni skanerlash boshlandi...\n")

    # Ochiq portlarni tekshirish
    ports = [22, 23, 80, 443, 3389]  # Eng ko‘p ishlatiladigan portlar
    for ip in active_ips:
        open_ports = scan_ports(ip, ports)
        if open_ports:
            print(f"🔥 {ip} dagi ochiq portlar: {', '.join(map(str, open_ports))}")
        else:
            print(f"❌ {ip} da ochiq port topilmadi.")

if __name__ == "__main__":
    ip_base = input("Tarmoqning IP bazasini kiriting (masalan, 192.168.1 yoki 172.16.15): ")
    scan_network(ip_base)
