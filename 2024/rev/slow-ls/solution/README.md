# SLOW-LS
Start by finding out what kind of binary is provided by e.g. using the `file` command. That will show that the binary is an `ELF 64-bit LSB pie executable, x86-64`. This file can be opened by most rev tools. A free one would for an example be Ghidra.

Once the files has been opened in your tool of choice, the correct function can be identified in the function menu as it is the only function with any meaningful code in it. Looking at the decompiled code, it can be seen that there is a large block of pre defined values which can be read from the location of `&DAT_*****` in memory. We will copy those and save for later. The code then asks for some input before entering a loop which is run untill a counter reaches the value `0x79` (int 121). The loop cotains the logic we need to reverse engineer. In there, there are three different code blocks which can be executed each iteration. The logic that controls which one is entered is at the top of the loop: `i%3`.

The first block of logic is indexing into the input value and the large block of predefined values and checking if the input is `0x17` greater than the corresponding value in the predefined values. If this does not match, the value in the if statement is set to true which means that the output is incorrect and incorrect will be printed at the end.

The second block is indexing the same way into the input and predefined values but checks if the input is equal to `input * 2 - 0x2a` or `input * 2 - 42`

The third block is in the same way as before indexing into both lists of values but this time checks if the input equals `((input * 2 + 0x100) / 2 + -0x32` or `((input * 2 + 256) / 2 - 42)`

So all we essentially need in order to get the flag is to create a small script that goes through the array of predefined numbers and does the opposite to them as we expect from the input:

1. input + 0x17
2. (input + 42)/2
3. ((input + 50) * 2 - 256) / 2