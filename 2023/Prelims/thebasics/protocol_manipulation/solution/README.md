# Protocol Manipulation
The challenge revolves around manipulating a myriad of different aspects
surrounding HTTP values. 

The user is presented with a simple index site which points them to `/WAT`. Once
the user navigates to `/WAT` they are prompted to make a `WAT` request.

This means that you have to edit the HTTP verb to be equal to `WAT` instead of
`GET` for example. The handiest way to do this is to use `curl` but you can also
use programming languages such as python or HTTP proxies such as Burp.

When you do a `WAT` request you get an error specifying that `WAT` is missing
from the query. So we add `?WAT` at the end of the URL. Which ends up giving
you an error that mentions that the `WAT` argument should be set to `WAT`. So
you add `?WAT=WAT` to the end of the URL. If you keep going like this, you will
eventually receive the flag. That happens when you've changed all values to be
`WAT`, the headers, cookies, queries, method, url, body.

```bash
curl -X WAT 'http://localhost:5000/WAT?WAT=WAT' -d 'WAT=WAT' -H 'Cookie: WAT=WAT' -H 'WAT: WAT' -H 'User-Agent: WAT'
```
