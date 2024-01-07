chall:
	push	rbp
	mov	rbp, rsp
	sub	rsp, 32
	mov	QWORD PTR -24[rbp], rdi
	mov	edi, 9
	call	malloc@PLT
	mov	QWORD PTR -8[rbp], rax
	mov	DWORD PTR -12[rbp], 0
	jmp	.L2
.L3:
	mov	eax, DWORD PTR -12[rbp]
	sal	eax, 3
	mov	rdx, QWORD PTR -24[rbp]
	mov	ecx, eax
	shr	rdx, cl
	mov	rcx, rdx
	mov	eax, 7
	sub	eax, DWORD PTR -12[rbp]
	movsx	rdx, eax
	mov	rax, QWORD PTR -8[rbp]
	add	rax, rdx
	mov	edx, ecx
	mov	BYTE PTR [rax], dl
	add	DWORD PTR -12[rbp], 1
.L2:
	cmp	DWORD PTR -12[rbp], 7
	jle	.L3
	mov	rax, QWORD PTR -8[rbp]
	add	rax, 8
	mov	BYTE PTR [rax], 0
	mov	rax, QWORD PTR -8[rbp]
	leave
	ret
