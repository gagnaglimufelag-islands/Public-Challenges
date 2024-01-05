import sys, time

def main():
    print(ascii_art())
    load_prompt("[+] Beacon loaded\n")
    load_prompt("[+] ShellZzZ loaded\n")
    load_prompt("[+] Connections established\n\n")
    load_prompt("[+] Locating flag.txt\n")
    time.sleep(1)
    load_prompt("[+] Obfuscating flag for detection bypass\n")
    time.sleep(2)
    load_prompt("[?] Preparing to exfil flag\n\n")
    time.sleep(3)
    load_prompt("[+] FLAG SUCCESSFULLY STOLEN\n\n")
    print("[+] FLAG: CHyw9w6uWxtabZAJ21WvykjHTpCtwwiXoYusBJDmSR8ng6RtskcUMqiP2HtG2jE")

def load_prompt(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04) 

def ascii_art():
    return r'''
   _____         .__ __________            .__                    
  /     \ _____  |  |\______   \ _______  _|__|__  __ ___________ 
 /  \ /  \\__  \ |  | |       _// __ \  \/ /  \  \/ // __ \_  __ \
/    Y    \/ __ \|  |_|    |   \  ___/\   /|  |\   /\  ___/|  | \/
\____|__  (____  /____/____|_  /\___  >\_/ |__| \_/  \___  >__|   
        \/     \/            \/     \/                   \/       


                       _________-----_____
       _____------           __      ----_
___----             ___------              \
   ----________        ----                 \
               -----__    |             _____)
                    __-                /     \
        _______-----    ___--          \    /)\
  ------_______      ---____            \__/  /
               -----__    \ --    _          /\
                      --__--__     \_____/   \_/\
                              ----|   /          |
                                  |  |___________|
                                  |  | ((_(_)| )_)
                                  |  \_((_(_)|/(_)
                                  \             (
                                   \_____________)
    
    
    
    '''



if __name__ == "__main__":
    main()