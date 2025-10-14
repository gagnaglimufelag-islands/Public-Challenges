# se7en

By scanning the 10.13.37.0/24 network, we discover something interesting on 10.13.37.39. We can use `nmap` to find all open ports

```
PORT      STATE SERVICE
23/tcp    open  telnet
80/tcp    open  http
554/tcp   open  rtsp
8899/tcp  open  ospf-lite
9527/tcp  open  unknown
34561/tcp open  unknown
34567/tcp open  dhanalakshmi
```

We see an HTTP server running on port 80. Visiting the IP with a browser we see a login screen. Multiple passwords work, e.g.

* admin: (no password)
* default:tluafed
* default:(any password)

The HTTP interface of the camera requires ActiveX which modern browsers don't really use any more, but we can use some of these passwords to stream over RTSP (real-time streaming protocol) on port 554.

```
mpv 'rtsp://10.13.37.38:554/user=admin&password=&channel=1&stream=0?'
mpv 'rtsp://10.13.37.38:554/user=default&password=tluafed&channel=1&stream=0?'
```

The camera is pointed to a piece of paper which has the flag written on it.

Special thanks to Steinar Hugi for lending us the camera.
