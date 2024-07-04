# Generalized-architecture-for-transmitting-technology
This challenge build on the first bluetooth challenge, Badvertisement so the first steps is essentially the same.

```
bluetoothctl
menu scan
transport le
back
scan on
devices
``` 

Nex step would be to find the MAC of the device and try to connect to it. Bluetooth can be a little flaky and sometimes requires retrying this connection step if you are unlucky.

```
connect XX:XX:XX:XX:XX:XX
```

The flag is hidden in one of the attributes this service proved. We need to identify the correct one which provides the flag when read.
A small hint relating to the correct attribute is that it has a quite strange UUID containing the readable string `deedbeef`
Otherwise there are not many descriptors available so they can quite easily be brute forced if needed.

```
menu gatt
list-attributes
select-attribute <ATTR_UUID>
read
```

Which results in the flag.