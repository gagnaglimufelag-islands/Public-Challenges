import hashlib
import secrets
import sqlite3

from pathlib import Path

HERE = Path(__file__).parent
DB = HERE / "db.sqlite"


def digest(pw):
    return hashlib.sha256(pw.encode()).hexdigest()


def authenticate(username, pw):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    res = c.execute(
        "SELECT username FROM users WHERE username=? and password=?",
        (username, digest(pw)),
    ).fetchone()
    if res:
        return res[0]
    return res


def get_user_details(username):
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    res = c.execute(
        "SELECT username, email, mfa FROM users WHERE username=?", (username,)
    ).fetchone()
    return list(res)


def has_mfa(username):
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    res = c.execute("SELECT mfa FROM users WHERE username=?", (username,)).fetchone()
    return res == 1


def setup_db():
    if DB.exists():
        DB.unlink()

    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(
        "CREATE TABLE users (username text, email text, password text, mfa integer)"
    )
    # MFA for admin for added security
    c.execute(
        "INSERT INTO users (username, email, password, mfa) VALUES ('admin', 'admin@hospital.is', ?, 1)",
        (digest(secrets.token_urlsafe(64)),),
    )
    c.execute(
        "INSERT INTO users (username, email, password, mfa) VALUES ('doctor', 'doctor@hospital.is', ?, 0)",
        (digest(secrets.token_urlsafe(64)),),
    )
    c.execute(
        "INSERT INTO users (username, email, password, mfa) VALUES ('nurse', 'nurse@hospital.is', ?, 0)",
        (digest(secrets.token_urlsafe(64)),),
    )
    c.execute(
        "INSERT INTO users (username, email, password, mfa) VALUES ('dog', 'dog@hospital.is', ?, 0)",
        (digest("i34tsk3l3t0nsf0rfun"),),
    )
    conn.commit()
    conn.close()
