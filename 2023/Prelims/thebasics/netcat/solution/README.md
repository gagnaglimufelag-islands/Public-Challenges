# Netcat
This challenge is meant to introduce novice players to connecting to ports and sending/receiving some information.
The name of the challenge is a hint to a tool used for these exact situations, netcat. We can connect to the domain
and port given in the description using netcat, we answe rwith our favorite color and get back the flag!

```bash
nc  ggc.tf 31010 
Hello there! I see you have found me.
What is your favorite color?: blue
What a coincidence, blue is also MY favorite color.
gg{netcat_is_your_friend}
```
