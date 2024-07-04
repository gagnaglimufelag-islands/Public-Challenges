import socket
import random
from time import sleep

def main():
    interfaces = socket.getaddrinfo(host=socket.gethostname(), port=None, family=socket.AF_INET)
    bc_ip = "10.0.0.255"
    cli_ip_list = ["10.0.0.125"]
    ports = [5000, 5555, 7007, 8091, 3331]
    wait_times = [0.1, 0.2, 0.3, 0.4, 2, 3, 5]
    print(f'sending noise')

    msg = 'abcdfEGttgsGFDSR452-+XYQWx[]|"!%$'
    while True:
        for i in msg:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.bind((random.choice(cli_ip_list),0))
            sock.sendto(bytes(i, "ascii"), (bc_ip, random.choice(ports)))
            sock.close()

            sleep(random.choice(wait_times))

main()