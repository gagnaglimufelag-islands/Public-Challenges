# dbg

The binary prints out to the terminal a prompt telling the user to have fun playing the ctf and some song lyrics. When looking at the binary further with a dissasembler/decompiler one can see that the binary hides some functionality, the binary assembles a flag and just never prints it to `stdout`.


## Reversing


We are given a 32-bit ELF binary which seems to just print out some text and that's about it. Let's have a look at the binary with any dissasembler/decompiler/debugger e.g *IDA,Ghidra,gdb* etc


```asm
<...>
mov     dword ptr [eax], '{gg'
sub     esp, 8
lea     eax, [ebp+s]
push    eax             ; src
push    [ebp+dest]      ; dest
call    _strcat
add     esp, 10h
sub     esp, 0Ch
push    [ebp+dest]      ; s
call    _strlen
add     esp, 10h
mov     edx, eax
mov     eax, [ebp+dest]
add     eax, edx
mov     word ptr [eax], 7Dh ; '}'
mov     eax, esi
lea     edx, [eax-1]
mov     eax, [ebp+dest]
mov     byte ptr [eax+edx], 0
<...>
```



Here we can see something interesting, the binary seems to be assembling something and by seeing glimpse of the flag prefix `gg{` we can pretty confidently say that it's assembling our flag. The problem here is that the flag is just never printed out.
Here we can either spend some time reversing the flag assembling routine or just simply check what the output would be after all the operations by using a debugger e.g `gdb`
We know from the disassembled `main()` function that after the call to `strcat()` a null-terminator gets added to the buffer, we can just place a breakpoint where the null-terminator is being appended then inspect our registers specifically our `EAX` register.


```asm
gef➤  b *main+1092
Breakpoint 1 at 0x1641: file main.c, line 76.
gef➤  r
Starting program: <program>
[*] Failed to find objfile or not a valid file format: [Errno 2] No such file or directory: 'system-supplied DSO at 0xf7fc4000'
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Breakpoint 1, 0x56556641 in main () at main.c:76
76	    flag[sizeof(flag)-1] = '\0';
[ Legend: Modified register | Code | Heap | Stack | String ]
──────────────────────────────────────────────────────────────────────── registers ─────────────────────────────────────────────────────────
$eax   : 0xffffcae0  →  "gg{hidden_in_plain_sight}"
$ebx   : 0x56558fc0  →  <_GLOBAL_OFFSET_TABLE_+0> enter 0x3e, 0x0
$ecx   : 0x20      
$edx   : 0x1b      
$esp   : 0xffffcae0  →  "gg{hidden_in_plain_sight}"
$ebp   : 0xffffd098  →  0xf7ffd020  →  0xf7ffda40  →  0x56555000  →   jg 0x56555047
$esi   : 0x1c      
$edi   : 0x10      
$eip   : 0x56556641  →  <main+1092> mov BYTE PTR [eax+edx*1], 0x0
$eflags: [zero carry parity adjust SIGN trap INTERRUPT direction overflow resume virtualx86 identification]
$cs: 0x23 $ss: 0x2b $ds: 0x2b $es: 0x2b $fs: 0x00 $gs: 0x63 
───────────────────────────────────────────────────────────────────────── stack ────────────────────────────────────────────────────────────
0xffffcae0│+0x0000: "gg{hidden_in_plain_sight}"	 ← $esp
0xffffcae4│+0x0004: "idden_in_plain_sight}"
0xffffcae8│+0x0008: "n_in_plain_sight}"
0xffffcaec│+0x000c: "_plain_sight}"
0xffffcaf0│+0x0010: "in_sight}"
0xffffcaf4│+0x0014: "ight}"
0xffffcaf8│+0x0018: 0x00007d ("}"?)
0xffffcafc│+0x001c: 0x56556219  →  <main+28> add ebx, 0x2da7
────────────────────────────────────────────────────────────────────── code:x86:32 ─────────────────────────────────────────────────────────
   0x56556636 <main+1081>      mov    eax, esi
   0x56556638 <main+1083>      lea    edx, [eax-0x1]
   0x5655663b <main+1086>      mov    eax, DWORD PTR [ebp-0x570]
 → 0x56556641 <main+1092>      mov    BYTE PTR [eax+edx*1], 0x0
   0x56556645 <main+1096>      sub    esp, 0xc
   0x56556648 <main+1099>      lea    eax, [ebx-0x1fb8]
   0x5655664e <main+1105>      push   eax
   0x5655664f <main+1106>      call   0x56556090 <puts@plt>
   0x56556654 <main+1111>      add    esp, 0x10
─────────────────────────────────────────────────────────────────── source:main.c+76 ───────────────────────────────────────────────────────
     71	     memset(flag, 0x0, result_len+7);
     72	 
     73	     strcpy(flag, "gg{");
     74	     strcat(flag, result);
     75	     strcat(flag, "}");
             // flag=0xffffcae0  →  "gg{hidden_in_plain_sight}"
 →   76	     flag[sizeof(flag)-1] = '\0';
     77	 
     78	     // Print out the song lyrics
     79	     printf("\n========================[ GG - 2023 ]==============================\n\nWelcome to GagnaGliman 2023, hope you have a blast and learn a ton\nHere Have a ChatGPT generated song:\n\n");
     80	     printf("Verse 1:\n%s", verse1);
     81	     printf("Chorus:\n%s", chorus);
──────────────────────────────────────────────────────────────────────── threads ───────────────────────────────────────────────────────────
[#0] Id 1, Name: "dbg", stopped 0x56556641 in main (), reason: BREAKPOINT
────────────────────────────────────────────────────────────────────────── trace ───────────────────────────────────────────────────────────
[#0] 0x56556641 → main()
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
gef➤  x/s $eax
0xffffcae0:	"gg{hidden_in_plain_sight}"
gef➤
```
