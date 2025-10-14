# Next level auth
This challenge requires competitors to exploit [CVE-2025-29927](https://zhero-web-sec.github.io/research-and-things/nextjs-and-the-corrupt-middleware). 

Taking a look at `package-lock.json` we can see that the next.js version is 15.2.1 which is 
vulnerable to the aforementioned CVE. We can see that `/flag` endpoint gives us the flag but is 
protected by the middleware and redirects us to `/worthy` if we aren't properly authenticated.

However, if we do as is mentioned in the blog post we can send a requst with the following header
and get the flag. 

```
x-middleware-subrequest: middleware:middleware:middleware:middleware:middleware
```
