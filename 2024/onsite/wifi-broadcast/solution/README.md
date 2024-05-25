# Whispers-in-the-air
Connect to the wifi supplied by the organisers znd open wireshark. You will immediately notice some broadcasting messages. It is simplest to try different filters, such as filterin by port. These messages are all UDP messages so it can be useful to filter on `udp.port`. Applying the filter to port 5005 will reveal the flag, one byte at a time.

The simplest solution is to capture traffic for a few minutes. Then save the capture to a file and run the following command: `tshark -r cap.pcapng -Y "udp.port == 50050" -T fields -e data | xxd -r -p` will result in the flag being printed out repeatedly.
