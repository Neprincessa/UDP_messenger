from common import safe_input
import socket 
import struct

UDP_IP_SENDER = ''
MULTICAST = 'multicast'
BROADCAST = 'broadcast'
UNICAST = 'unicast'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

def recieve(mode):
    if mode == BROADCAST:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        UDP_IP_SENDER = ''
    elif mode == MULTICAST:
        UDP_IP_SENDER = "224.1.1.1"
        req = struct.pack("4sl", socket.inet_aton(UDP_IP_SENDER), socket.INADDR_ANY)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, req)
    elif mode == UNICAST:
        UDP_IP_SENDER = str(input('Enter sender ip: '))
    else:
        raise ValueError("Invalid mode:(")
    sock.bind((UDP_IP_SENDER, UDP_SENDER_PORT))
    while True:
        data, addr = sock.recvfrom(1024) 
        print("message: ", str(data, encoding='utf-8'))

if __name__ == "__main__":
    UDP_SENDER_PORT = safe_input(input('Enter sender port: '))
    print("Choose unicast, multicast or broadcast.")
    mode = str(input("Enter mode: ")).lower()
    recieve(mode)
