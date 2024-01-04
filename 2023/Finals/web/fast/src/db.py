import hashlib
import secrets
import sqlite3

from pathlib import Path

HERE = Path('/tmp')


class DB:
    def __init__(self, token):
        self.token = token
        self.path = HERE / token
        self.setup_db()

    def conn(self):
        return sqlite3.connect(self.path)

    def digest(self, pw):
        return hashlib.sha256(pw.encode()).hexdigest()

    def authenticate(self, username, pw):
        conn = self.conn()
        c = conn.cursor()
        res = c.execute(
            "SELECT username FROM users WHERE username=? and password=?",
            (username, self.digest(pw)),
        ).fetchone()
        if res:
            return res[0]
        return res

    def get_user_details(self, user):
        username = user["user"]
        conn = self.conn()
        c = conn.cursor()
        res = c.execute(
            "SELECT username, isadmin FROM users WHERE username=?",
            (username,),
        ).fetchone()
        return res

    def get_host(self):
        conn = self.conn()
        c = conn.cursor()
        res = c.execute(
            "SELECT host FROM stats",
        ).fetchone()
        if res:
            return res[0]
        return res

    def set_host(self, host):
        conn = self.conn()
        c = conn.cursor()
        c.execute("UPDATE stats SET host=? WHERE id=1", (host,))
        conn.commit()

    def setup_db(self):
        conn = self.conn()
        c = conn.cursor()
        c.execute("CREATE TABLE users (username text, password text, isadmin integer)")
        c.execute("CREATE TABLE stats (id integer, host text)")
        c.execute(
            "INSERT INTO users (username, password, isadmin) VALUES ('admin', ?, 1)",
            (self.digest(secrets.token_urlsafe(64)),),
        )
        c.execute("INSERT INTO stats (id, host) VALUES (1, 'examplestats.com')")
        conn.commit()
        conn.close()
