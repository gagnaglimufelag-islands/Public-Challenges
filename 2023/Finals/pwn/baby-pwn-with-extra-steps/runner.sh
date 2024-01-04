isolate -b $SOCAT_PID --silent --init > /dev/null && \
isolate -b $SOCAT_PID --processes=30 --wall-time=300 --share-net --dir=/lib32 --dir=/etc=/inner-etc --dir=/src -c /src --env=PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin --tty-hack --run -- ./chall && \
isolate -b $SOCAT_PID --cleanup
