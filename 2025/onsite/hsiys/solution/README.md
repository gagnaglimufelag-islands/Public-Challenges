# how-secret-is-your-secret

After logging into admin interface of camera (admin:, or some other way) we discover its firmware version (System: V4.02.R12.00006510.10010.1403)

After googling that we can first find the name of the camera: hisilicon

https://www.unifore.net/ip-video-surveillance/v4-02-r12-ip-camera-firmware-download.html

Googling hisilicon along with the firmware version, gets us to a known CVE which includes a known default password for the telnet interface on port 23:

* https://www.cvedetails.com/cve/CVE-2021-41506/
* https://habr.com/ru/articles/486856/

`nc 10.10.42.146 23`

User: `root`
Pass: `xmhdipc`

Flag is the password for the hidden WiFi `sup3rsecret` located in `/mnt/mtd/Config/WLan`.
