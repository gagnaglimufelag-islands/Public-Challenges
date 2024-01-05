# Animal Generator
This is an introductory reverse engineering challenge. The player is given a linux binary named `animal_generator`, you can figure out that it is a Linux binary by running the `file` command on the binary.

On Linux you can run `chmod +x animal_generator` to make the binary executable and then execute it. When running the binary you will get output similar to the following:
```bash
❯ ./animal_generator 
Welcome to the str...     err... I mean sentence generator!
Do you want me to generate a sentence?
Enter here [y/n]> 
Haha! You think you have a choice!? Here is your sentence, like it or not!
Uh... takes a bit of time to generate...      hang on...

Long Large Human
```

Nothing too interesting here, clearly it just generates different animals.

We can get a list of all the animals it can generate by running the `strings` command on the binary.
```bash
❯ strings animal_generator
/lib64/ld-linux-x86-64.so.2
sleep
puts
__stack_chk_fail
time
__libc_start_main
srand
__cxa_finalize
printf
__isoc99_scanf
libc.so.6
GLIBC_2.7
GLIBC_2.4
GLIBC_2.2.5
GLIBC_2.34
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
PTE1
u3UH
 run strings |               <-- Middle of the flag
Daddy
Long
Forgetful
Slightly
Silly
Pleasing
Satanic
Star-nosed
NULL
Snout
Large
Small
Pink
Little
Crazy
Hellbent
Legs
Human
Elephant
Fishfingers
Lumpsucker
Fungus
Wobbegong
grep flagformat}             <-- End of the flag
Welcome to the str...     err... I mean sentence generator!
Do you want me to generate a sentence?
Enter here [y/n]> 
Haha! You think you have a choice!? Here is your sentence, like it or not!
Uh... takes a bit of time to generate...      hang on...
%s %s %s
gg{always remember to        <-- Start of the flag
;*3$"
GCC: (GNU) 12.2.1 20230201
animal_generator.c
NO_ONE
FINDS_THIS
HOPE.0
[...]
```

We not only get the animals but also the flag which is `gg{always remember to run strings | grep flagformat}`
