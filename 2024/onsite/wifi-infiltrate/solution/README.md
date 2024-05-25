# G00d-Homemade-S3mcur1ty
By port scanning the network with for an example Nmap, a webserver can be found running a python application. By querying the application we are given a feew paths, some open and some requiring authentication.

By navigating to `/users?username='SELECT` reveals an error from the db indicating that this is a field we can manipulate to our advantage. By utilising the error messages, we can try a union query such as this one `/users?username=' UNION SELECT 1, 'a', 'b', 1--` we can leak the name of the table we are querying

`"ERROR:  each UNION query must have the same number of columns\nLINE 1: ...rname FROM users WHERE username = '' UNION SELECT 1, 'a', 'b..."`

and then construct the following query: `/users?username=Eve'; SELECT * FROM users where 'a' = 'a` which results in the entire contents of the DB being dumped.

We see that the passords are hashed, putting them into online tools it can be identified that they are clearly MD5 hashes. Taking the hash from Eve, which is an admin and putting it into some online tools, we receive her password which we can then use to navigate to `/flag?username=Eve&password=deadb33f` which returns the flag for the challenge.