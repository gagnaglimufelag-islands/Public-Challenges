# ANGRy

The program checks each index of a `26 byte` input buffer. If the input matches the current index then it moves on to the next index and so on. This is the perfect time to use [angr](https://angr.io/). By using Symbolic Execution and one of angr's powerful simulation managers we can explore different code paths in the binary and retrieve the input to a successful code path.

<br>

## Reversing

We are given a *64-bit ELF binary*, looking at the decompiled code from *Ghidra* we can see the `main()` function and one interesting function called `check_flag()` let's look at the main function first

<br>

### *Decompiled main*

```c
int main(int argc,char *argv)

{
  bool ret_val;
  long in_FS_OFFSET;
  char buf [40];
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  while( true ) {
    printf("Enter flag: ");
    fgets(buf,26,stdin);
    ret_val = check_flag(buf);
    if (ret_val != false) break;
    puts("\nNope...Try again!\n");
  }
  puts("\n[+] YOU GOT THE FLAG!\n");
  printf("gg{%s}\n\n",buf);
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}

```

Here we see that our input gets passed to the function `check_flag()` which then checks if it returns *true* or *false*. If we return from the function with the value being *true* we have the flag else we fail. Cool! Let's look at the other function and see what it does.

<br>
<br>

### *Decompiled check_flag*

```c

bool check_flag(char *param_1)

{
  bool ret;
  
  if ((((((((param_1[4] == '_') && (param_1[3] == 'R')) && (param_1[0x17] == 'F')) &&
         (((param_1[6] == '5' && (param_1[8] == 'L')) &&
          ((param_1[0xc] == '_' && ((param_1[0x16] == '1' && (*param_1 == 'A')))))))) &&
        (param_1[0x11] == '_')) &&
       (((((param_1[0xb] == '3' && (param_1[0xf] == 'G')) && (param_1[0x12] == '1')) &&
         ((param_1[0xe] == 'N' && (param_1[0x18] == '3')))) &&
        ((param_1[10] == 'V' && ((param_1[1] == 'N' && (param_1[9] == '0')))))))) &&
      ((param_1[0x15] == 'L' &&
       (((param_1[2] == 'G' && (param_1[7] == '_')) && (param_1[0xd] == 'A')))))) &&
     (((param_1[5] == '1' && (param_1[0x10] == 'R')) &&
      ((param_1[0x13] == '5' && (param_1[0x14] == '_')))))) {
    ret = true;
  }
  else {
    ret = false;
  }
  return ret;
}

```

Here we see each value getting compared to it's corresponding index. We can go through them one by one but that would be inefficient and tedious. Let's write some code!

<br>
<br>

```python
#!/usr/bin/env python3

import angr

proj = angr.Project("angry")
simgr = proj.factory.simgr()
simgr.explore(find=lambda s: b"\n[+] YOU GOT THE FLAG!\n\n" in s.posix.dumps(1))
flag = simgr.found[0].posix.dumps(0)
print(flag.decode('utf-8'))
```


Here we use *angr's* `explore()` method to find an input that gets us to the code path that spits out the message `[+] YOU GOT THE FLAG!`

<br>
<br>

```sh
(pwnenv) kali@kali:~/chal$ ./sol.py
<...>
[+] ANGR_15_L0V3_ANGR_15_L1F3
```

```sh
(pwnenv) kali@kali:~/chal$ ./angry 
Enter flag: ANGR_15_L0V3_ANGR_15_L1F3

[+] YOU GOT THE FLAG!

gg{ANGR_15_L0V3_ANGR_15_L1F3}
```
