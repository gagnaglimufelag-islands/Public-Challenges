# It's just strings
Using `objdump -d chall` you will find functions named `base64decode` and `decryptAESCBC256`

Using `strings chall` you will find:
```
sixteenbyteivheh
supersecretkeythatshouldnotleak!
oLsxPguNeX6oVxBiUwAZSJau6P2ruxYo/WaoDhIN1LGa9hurV1yuu7DwJfLmV9rcX/he1HuKZ6yI2t4e5CP3zw==
```

Looks like an IV, a secret key and some base64 encoded data. If we put all of this into cyberchef we get the following:
![https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)AES_Decrypt(%7B'option':'UTF8','string':'supersecretkeythatshouldnotleak!'%7D,%7B'option':'UTF8','string':'sixteenbyteivheh'%7D,'CBC','Raw','Raw',%7B'option':'Hex','string':''%7D,%7B'option':'Hex','string':''%7D)&input=b0xzeFBndU5lWDZvVnhCaVV3QVpTSmF1NlAycnV4WW8vV2FvRGhJTjFMR2E5aHVyVjF5dXU3RHdKZkxtVjlyY1gvaGUxSHVLWjZ5STJ0NGU1Q1Azenc9PQ](./sol.png)
