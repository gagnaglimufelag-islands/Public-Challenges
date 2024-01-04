# Hear Ye Hear Ye
You are given a pcap file which you can open using Wireshark. Immediately you see a large number of
DNS queries being made to `gamna.cher.is`.

Clearly there is a wildcard domain on `*.gamna.cher.is`. Each subdomain contains a number of hex characters.

The steps to solve are:
1. Extract all subdomains
2. Hex decode subdomains
3. Grep for flag format `gg{`

```bash
tshark -r data.pcapng -T fields -e ip.src -e dns.qry.name | rg '[a-f0-9]{50,}\.gamna.cher.is' -o | rg '[a-f0-9]{50,}' -o | tr -d '\n' | xxd -r -p | rg 'gg\{[^}]*\}' -o
```
