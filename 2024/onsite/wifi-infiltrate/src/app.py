from fastapi import FastAPI
import sqlite3
from Crypto.Hash import MD5
import psycopg2
import os

app = FastAPI()

POSTGRES_HOST = "localhost" if os.getenv("POSTGRES_URL") == None else os.getenv("POSTGRES_URL")
POSTGRES_USER = "postgres" if os.getenv("POSTGRES_USER") == None else os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = "gaszg54wqYhzgyKasY" if os.getenv("POSTGRES_PASSWORD") == None else os.getenv("POSTGRES_PASSWORD")


conn = psycopg2.connect(
    dbname="postgres", 
    user=POSTGRES_USER, 
    password=POSTGRES_PASSWORD, 
    host=POSTGRES_HOST,
    port="5432"
)


@app.get("/")
def read_root():
    print(os.getenv("POSTGRES_URL"))
    return {"Home-semcurity": True, "public_paths": ["/login", "/users", "/users?username="], "admin_paths": ["/admin", "/flag"]}

@app.get("/users")
def list_users(username = None):
    cursor = conn.cursor()

    if username != None:
        # cmd = f"SELECT username FROM users WHERE username = '{username}'"
        # cmd = "SELECT username FROM users WHERE username = 'Alice' UNION ALL SELECT PASSWORD FROM users"
        # /users?username=Eve' UNION ALL SELECT password FROM users WHERE username = 'Eve
        # /users?username=Eve'; SELECT * FROM users where 'a' = 'a
        # print(cmd)
        try:
            cmd = "SELECT username FROM users WHERE username = '%s'" % username
            cmd = f"SELECT username FROM users WHERE username = '{username}'"
            print(cmd)
            cursor.execute(cmd)
        except psycopg2.Error as e:
            conn.rollback()
            print(e.pgerror)
            return {"message": "Something went wrong", "error": e.pgerror}
    else:
        cursor.execute(f"SELECT username FROM users")

    results = cursor.fetchall()
    print(results)

    return {"users": results}

@app.get("/login")
def login(username, password):
    results = get_user(username, password)

    if results:
        # TODO: implement some cookie based auth
        return {"OK": True, "cookie": "TODO"}

    return {"OK": False}

@app.get("/admin")
def login(username, password):
    results = get_user(username, password)
    if is_admin(results):
        return {"message": "Under construction"}
    return unauthorized()

@app.get("/flag")
def login(username, password):
    results = get_user(username, password)
    if is_admin(results):
        with open('flag') as f:
            flag = f.read()
        return {"flag": flag}
    return unauthorized()

def get_user(username, password):
    cursor = conn.cursor()

    h = MD5.new()
    h.update(password.encode())
    enc_pass = h.hexdigest()

    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, enc_pass))
    return cursor.fetchone()

def is_admin(results):
    try:
        if results[2] == True:
            return True
    except:
        pass
    return False

def unauthorized():
    return {"error": "Unauthorized"}