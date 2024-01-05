# Good Client Bad Client
The player is presented with an incredibly boring corporate intranet website. Perhaps the single most boring website you could find. On the website there is a single link that points to `/intranet` when you click that button you are presented with a HTTP basic auth window.

Now if you look at the source of the index page, by clicking inspect element, F12, or CTRL+U you will find the following HTML comments:
```
<!-- Remove on prod: -->
<!-- jane:bGl2ZXJwb29s -->
<!-- john:U2lsbHlHb29zZTQy -->
<!-- admin:YW5leHRyZW1lbHlsb25nY29tbWFjMG1wbDN4YW5kZGlmZmljdWx0dG9ndWVzc3Bhc3N3b3Jk  -->
```

These look to be usernames and passwords which are base64 encoded. When you base64 decode the password of the admin you get `anextremelylongcommac0mpl3xanddifficulttoguesspassword`. Now if you go back to `/intranet` and login as admin with that password you can see that you can log in and are presented with a flag.
