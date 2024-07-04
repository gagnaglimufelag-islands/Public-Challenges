# Badvertisement
This challenge requires a laptop/smartphone. There exist many apps for both android and IOS which can be used to scan for bluetooth devices.

This can also be solved using `bluetoothctl` with the following commands:

```
bluetoothctl
menu scan
transport le
back
scan on
devices
```

Where the flag should be visible as the name of one of the captured device names.