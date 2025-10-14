# Man Down
This challenge is based on [CVE-2024-21644](https://github.com/pyload/pyload/security/advisories/GHSA-mqpq-2p68-46fv) discovered by @PinkDraconian.

Looking at the `setup_db.py` file we can see that the flag is being inserted into the database as a
row in the downloads table. Now, taking a look at the `app.py` file, we can see that all rows within
the downloads table is shown under `/downloads`:
```python
@app.route("/downloads")
@requires_admin
def downloads():
    downloads = get_downloads()
    return render_template("downloads.html", title="Downloads", downloads=downloads)
```

However, it requires that we have adminstrator privileges, i.e. logged in as the *admin* user.
Looking at the different routes of the application we can see that only the following routes are
reachable as an unauthenticated user:
```
/
/login
/logout
/system/version
/render/<path:template>
```

The `index`, `login` and `logout` routes are not of interest to us, seeing as we aren't able to bypass
the login functionality. The `/system/version` route only displays the version and has no
interesting logic.

The `/render/<path:template>` route is interesting however, it renders a template of our choice
without arguments. 
```python
@app.route("/render", methods=["GET"])
def render():
    try:
        template = request.args.get("template")
        path = os.path.join("test_templates", template)
        data = render_template(path)
    except:
        data = render_template("invalid.html", title="Oops")
    return Response(data, mimetype="text/html")
```

This means we are able to render templates which are not accessible to
unauthenticated users.

```
templates
│ test_templates
│ │ └ running.html
│ │ base.html
│ │ dashboard.html <-- requires auth
│ │ downloads.html <-- requires auth
│ │ index.html
│ │ invalid.html
│ │ login.html
│ └ system.html    <-- requires auth
```

However when we try to traverse the folders by doing `/render?template=../downloads.html` we get an
error. Looking closer we can see that the `path` variable is set to `test_template/../downloads.html` when it is passed to the `render_template` function. Reading Flask internals we can see that the `render_template` function is defined like so:
```python
def render_template(
    template_name_or_list: str | Template | list[str | Template],
    **context: t.Any,
) -> str:
    """Render a template by name with the given context.

    :param template_name_or_list: The name of the template to render. If
        a list is given, the first name to exist will be rendered.
    :param context: The variables to make available in the template.
    """
    app = current_app._get_current_object()  # type: ignore[attr-defined]
    template = app.jinja_env.get_or_select_template(template_name_or_list)
    return _render(app, template, context)
```

We can see that it calls the Jinja function `get_or_select_template`. Tracing through the code path
we end up at `src/jinja2/loaders.py:split_template_path()` in the [Jinja repository](https://github.com/pallets/jinja/blob/main/src/jinja2/loaders.py#L25). For those interested in the full trace, you can find it in the [Appendix](#appendix). Taking a look at the code we see the following:

```python
def split_template_path(template: str) -> t.List[str]:
    """Split a path into segments and perform a sanity check.  If it detects
    '..' in the path it will raise a `TemplateNotFound` error.
    """
    pieces = []
    for piece in template.split("/"):
        if (
            os.sep in piece
            or (os.path.altsep and os.path.altsep in piece)
            or piece == os.path.pardir
        ):
            raise TemplateNotFound(template)
        elif piece and piece != ".":
            pieces.append(piece)
    return pieces
```

We can see that Jinja splits the path into pieces which are seperated by slashes. If any of the
pieces include either `/` or `..` it raises a `TemplateNotFound` exception. However there is lesser
known feature of the [`os.path.join`](https://docs.python.org/3/library/os.path.html#os.path.join) function. If the last argument to the function is an absolute path
it returns the absolute path, so `os.path.join("test_templates", "/src/templates/downloads.html")`
will return `/src/templates/downloads.html`. If we try calling
`/render?template=/src/templates/downloads.html` we still get the same error. Why?

If we continue reading the Jinja internals we can see that it ends up setting the filename like so `filename = posixpath.join(searchpath, *pieces)` this means that if we input a value like `/downloads.html` we will get `templates/downloads.html` since the default searchpath in Flask is `templates`. This we can do by simply inputing `/render?template=/downloads.html`. Now we can take a look at those templates that are behind auth.

Trying all the templates of interest to us we can see that `/render?template=/dashboard.html` results in an error due to the `session` and `summary` variables are missing, `/render?template=/downloads.html` results in an empty table since the `downloads` variable is empty. 

Finally, when we try `/render?template=/system.html` we get a table with some data. We see that the
*Statistic* part is empty but the *Configuration* part is populated even though no arguments
followed. Taking a look at the `system.html` file we can see that the variable is named `config` the
same as the [Flask global configuration variable](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.config). Meaning, we have
managed to dump the configuration of the Flask server. Within this configuration we can find the
value of the `secret_key`.

Luckily for us the `secret_key` is used to sign session objects. Having access to the `secret_key`
allows us to sign our own sessions, in turn allowing us to create a valid session for the *admin*
user. This can be done using the [flask-unsign](https://github.com/Paradoxis/Flask-Unsign) tool.

We just have to take note of what the session is named and what it includes, replicate it, and sign
with the acquired secret key. Running the following command with the correct secret key should give
us a signed session.
```bash
flask-unsign --sign --cookie "{'user_id': '1', 'username':'admin'}" --secret 'SECRET_KEY_HERE'
```

Now we can add the outputted cookie to our requests and we should be logged in as the *admin* user.
Now when routing to `/downloads` we can see the list of files downloaded along with the flag!

## Appendix - `render_template` tracing
[`render_template`](https://github.com/pallets/flask/blob/f61172b8dd3f962d33f25c50b2f5405e90ceffa5/src/flask/templating.py#L138)

[`get_or_select_template`](https://github.com/pallets/jinja/blob/220e67ae999c24e4077d7bf5bdc932757b65a338/src/jinja2/environment.py#L1075)

[`get_template`](https://github.com/pallets/jinja/blob/220e67ae999c24e4077d7bf5bdc932757b65a338/src/jinja2/environment.py#L984)

[`_load_template`](https://github.com/pallets/jinja/blob/220e67ae999c24e4077d7bf5bdc932757b65a338/src/jinja2/environment.py#L959)

It ends up calling `self.loader.load` [here ](https://github.com/pallets/jinja/blob/220e67ae999c24e4077d7bf5bdc932757b65a338/src/jinja2/environment.py#L977). The Jinja template loader used by Flask is the `FileSystemLoader`.

[`FileSystemLoader`](https://github.com/pallets/jinja/blob/main/src/jinja2/loaders.py#L152)

The `FileSystemLoader` inherits the `load` function from the `BaseLoader`

[`BaseLoader.load`](https://github.com/pallets/jinja/blob/main/src/jinja2/loaders.py#L108)

[`FileSystemLoader.get_source`](https://github.com/pallets/jinja/blob/main/src/jinja2/loaders.py#L194)

[`split_template_path`](https://github.com/pallets/jinja/blob/main/src/jinja2/loaders.py#L25)
