from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

print("📡 Tarmoq trafikini kuzatish boshlanmoqda... (Ctrl + C bilan to‘xtating)")
sniff(prn=packet_callback, store=False)
