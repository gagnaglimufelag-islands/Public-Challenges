import socket
from time import sleep

def main():
    interfaces = socket.getaddrinfo(host=socket.gethostname(), port=None, family=socket.AF_INET)
    bc_ip = "10.42.0.255"
    print(f'sending on {bc_ip}')

    msg = 'gg{you_only_need_to_listen}'
    while True:
        for i in msg:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.bind((bc_ip,0))
            sock.sendto(bytes(i, "ascii"), (bc_ip, 5005))
            sock.close()

            sleep(2)


main()
