tshark -r cap.pcapng -Y "udp.port == 5005" -T fields -e data | xxd -r -p
