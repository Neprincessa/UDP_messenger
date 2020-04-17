import socket

UDP_IP_DST = "224.1.1.1"
MULTICAST_TTL = 2 
MULTICAST = 'multicast'
BROADCAST = 'broadcast'
UNICAST = 'unicast'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

def safe_input(number, functype='port'):
    if functype == 'loop_back':
        while not number.isdigit() or int(number) < 0 or int(number) > 1:
            number = input("Enter number once again:")
    else:
        while not number.isdigit() or int(number) < 0:
            number = input("Enter number once again: ")
    return int(number)


def send(mode):
    if mode == BROADCAST:
        UDP_IP_DST = '255.255.255.255'
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    elif mode == MULTICAST:
        UDP_IP_DST = "224.1.1.1"
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
        loop_back = safe_input(input("Enter 1 if you want to turn on loopback, else enter 0: "), 'loop_back')
        if loop_back == 1:
            sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)
        else:
            sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 0)
    elif mode == UNICAST:
        UDP_IP_DST = str(input('Enter distination ip: '))
    else:
        raise ValueError("Invalid mode type:(")
    print("Datagram size: ", sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF))
    while (True):
        msg = str(input('Enter message: '))
        sock.sendto(bytes(msg, "utf-8"), (UDP_IP_DST, UDP_DST_PORT))

if __name__ == "__main__":
    UDP_DST_PORT = safe_input(input('Enter distination port: '))
    print("Choose unicast, multicast or broadcast.")
    mode = str(input("Enter mode: ")).lower()
    send(mode)

