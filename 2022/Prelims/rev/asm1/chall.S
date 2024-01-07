chall:
	push	rbp
	mov	rbp, rsp
	mov	DWORD PTR -20[rbp], edi
	mov	DWORD PTR -24[rbp], esi
	mov	DWORD PTR -4[rbp], 0
	jmp	.L2
.L3:
	mov	eax, DWORD PTR -24[rbp]
	add	DWORD PTR -20[rbp], eax
	add	DWORD PTR -4[rbp], 1
.L2:
	cmp	DWORD PTR -4[rbp], 4
	jle	.L3
	mov	eax, DWORD PTR -20[rbp]
	pop	rbp
	ret
