tshark -r data.pcapng -T fields -e ip.src -e dns.qry.name | rg '[a-f0-9]{50,}\.gamna.cher.is' -o | rg '[a-f0-9]{50,}' -o | tr -d '\n' | xxd -r -p | rg 'gg\{[^}]*\}' -o
