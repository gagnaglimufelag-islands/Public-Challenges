# Pattern Matched
In this challenge we get a link and some code.

Looking at the code we can immediately see that it is vulnerable to SQLi in `/patterns` through the `token` parameter.

```python
@app.route("/patterns", methods=["GET"])
def patterns():
    free = request.args.get("free", default=False, type=lambda x: x.lower() == 'true')
    token = request.args.get("token")

    if free:
        return render_template("free.html")

    if not token:
        flash("Missing token!", "error")
        return redirect(url_for("index"))

    if not TOKEN_VALIDATION.fullmatch(token):
        flash("Invalid token!", "error")
        return redirect(url_for("index"))

    cur = CONN.cursor()
    res = cur.execute(
        CHECK_TOKEN_QUERY.replace("%token", f"AND token LIKE '{token}'")
    ).fetchone()

    if not res:
        flash("Invalid token!", "error")
        return redirect(url_for("index"))

    patterns = cur.execute(GET_PATTERNS_QUERY).fetchall()
    return render_template("patterns.html", patterns=patterns)
```

However when we try to do a simple SQLi exploit it fails, looking at the code again we see that there is some validation in place:

```python
TOKEN_VALIDATION = re.compile(r"^[\[A-Za-z0-9\]+(_)?\[A-Za-z0-9\]+]{32,128}$")
```

The regex validates that the token is between 32 and 128 characters consists of alphanumerics and can have a single underscore somewhere in the middle. 

However it looks like the person that made this regex rule made a small mistake and used a character grouping instead of set, which means that tokens consist of only underscores are considered valid. 

Another interesting thing to note is that the SQL query to check the validity of the token is using `LIKE` instead of a simple equals operator. This allows us to use wildcards. Luckily for us, underscore is a wildcard which means "any character" so it is a wildcard match for exactly one character.

This means if we know the length of the token we can simply enter that many underscores and we should be considered authenticated. From the regex rule it looks like a valid token is going to be between 32 and 128 characters in length. This means we can simply send a `GET` request with the `token` parameter set to nothing but underscores for all possible lengths. One of the requests is bound to succeed and we should get the list of patterns and the flag.
