
from scapy.all import *

def forge_packet():
    print("🛠️ Forging a custom ICMP Echo Request...")
    # IP Layer: Source and Destination
    ip = IP(dst="8.8.8.8")
    # ICMP Layer: Echo Request
    icmp = ICMP()
    # Payload
    payload = "Hello SAE24 - Network Test"
    
    packet = ip/icmp/payload
    
    print(f"Packet forged: {packet.summary()}")
    print("\nDetailed Packet Structure:")
    packet.show()
    
    # In a real environment, we would use: send(packet)
    print("\n✅ Packet ready for sending.")

if __name__ == "__main__":
    forge_packet()
