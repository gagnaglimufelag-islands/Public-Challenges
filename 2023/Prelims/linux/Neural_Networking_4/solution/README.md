## Neural Network 4
This challenge had a small oversight, the `flag4.txt` file was readable by everyone. So a number of 
players were able to guess that the flag was in the home directory of the `gpt` user and were able to
guess the name of the file.

```bash
dalle@21f1622aa404:~$ ls /home
dalle  gpt
dalle@21f1622aa404:~$ ls /home/gpt
ls: cannot open directory '/home/gpt': Permission denied
dalle@21f1622aa404:~$ cat /home/gpt/flag4.txt
gg{GPT_Raiders_of_the_Lost_Vault}
dalle@21f1622aa404:~$ 
```
