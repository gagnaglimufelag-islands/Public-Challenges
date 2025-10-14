# Nightmare
Looking at the `app.py` file we see that there is not a lot going on but we immediately notice that we have file read under `/debug`:
```python
@app.route("/debug")
def debug():
    filename = request.args.get("filename", "")
    if (
        filename == ""
        or not filename.startswith("/pro")
        or re.match(r"/pro./\d+", filename) is None
    ):
        return render_template("error.html")

    try:
        with open(filename, "r") as f:
            return str(eval(f.read()))
    except:
        return render_template("error.html")
```

Not only file read, but arbitrary code execution if we are able to read a file which we control. Going 
through the function line by line. We can see that we can pass in a name of a file to be read and evaluated
with the `filename` query parameter. The `filename` parameter needs to start with `/pro` and match 
the `/pro./\d+` regex.

Looking at a Linux system we can figure out that this is allowing us to only read files under ProcFS, 
specifically only folders which are linked to a process. So for example `/proc/1/*`. However we do not
control the contents of any of the files which match that filepath.

When we look at the Dockerfile, we can see that nginx is in front of the Flask server. Nginx has a special
functionality in that, it sometimes saves the request body into a temporary file via [client body buffering](https://nginx.org/en/docs/http/ngx_http_core_module.html#client_body_buffer_size).
By default, Nginx does this if the request body size is greater than 8KB in size. Nginx does this and then 
removes the file immediately. However, nginx still has a file descriptor pointed to it which means that the
file is still accessible via ProcFS through `/proc/9/fd/11` as an example. If the process ID of nginx is `9` and
the ID of the file descriptor pointing to the temporary file is `11`. Still, nginx closes the file descriptor 
once it is done processing the request, which is prety much immediate. 

To ensure that nginx keeps the file descriptor pointing at the temporary file open we can send a request with the
`Content-Length` header set to a value that is larger than the actual size of the request. This results in nginx
waiting for the rest of the content and thus keeping the file descriptor open for longer. 

Now that we essentially are able to write arbitrary python code to ProcFS we can send a request with 
```python
str(__import__('subprocess').run('/win', shell=True, capture_output=True, text=True).stdout)
```

as a payload and then fill the request body with 8KB worth of python comments. We then send the request with a 
a spoofed `Content-Length` header. Now we need to bruteforce the process ID and file descriptor ID, which is 
simple enough. We can create a double for loop in python which sends all possible combinations of 
`/proc/{proc_id}/fd/{fd_id}` to `/debug` through the `filename` parameter.

Once we find the correct combination we should be presented with the flag.

