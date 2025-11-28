from scapy.all import *
import random
import string

REAL_FLAG = "ISC2CTF{S51jhgkok0sd4q6sd2f4Efy6j3k5h3g7}"
REAL_PACKET_NUMBER = len(REAL_FLAG)  # this means: packet whose number = flag length has the real flag

NUM_PACKETS = 80
packets = []

def random_fake_flag():
    length = random.randint(6, 35)  # random length not matching i
    inside = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return f"ISC2CTF{{{inside}}}"

for i in range(1, NUM_PACKETS + 1):

    if i == REAL_PACKET_NUMBER:
        payload = REAL_FLAG
    else:
        payload = random_fake_flag()

    pkt = IP(dst="192.168.1.10") / TCP(sport=1234, dport=80) / payload
    packets.append(pkt)

wrpcap("flag.pcap", packets)

print("PCAP created!")
print(f"Real flag packet index: {REAL_PACKET_NUMBER}")
print(f"Real flag length: {len(REAL_FLAG)}")
print(f"Real flag: {REAL_FLAG}")
