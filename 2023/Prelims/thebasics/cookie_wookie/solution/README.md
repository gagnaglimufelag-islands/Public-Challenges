# Cookie Wookie
When routing to the website you can see that you can register a user and login. Once you are logged in you can see that the session cookie is called `blog_auth` is base64 encoded content. When base64 decoding the cookie you will find that the cookie includes a JSON object that looks something like this `{"user":"username","is_admin":false}`.

Now if you try to change the contents to `{"user":"admin","is_admin":true}` and base64 encode it and set the `blog_auth` cookie to this and refresh you will see that you suddenly have access to a hidden blog post which contains the flag.
