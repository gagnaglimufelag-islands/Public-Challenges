# Dictating Director
A really simple challenge in which you just have to follow all redirects until you get the flag. 

The challenge consists of a website that redirects you to the next integer until you hit `/6767` where you get the flag.

The issue with this is that Firefox and Chrome only follow a maximum of 20 redirects before stopping and giving a redirection error and curl follows a maximum of 50 redirects before stopping and giving an error message. This means you have to do this in your hands, create a script, or overwrite the maximum amount of redirects in the aforementioned tools, which is the easiest path forward. 

So the simplest solution is to simply run `curl -L --max-redirs 10000 http://[LOCATION]` and you should get the flag after a while.

