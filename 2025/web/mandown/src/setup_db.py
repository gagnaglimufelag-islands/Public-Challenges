import os
import secrets
import sqlite3
from hashlib import sha512
from pathlib import Path

HERE = Path(__file__).parent
DB = HERE / "mandown.db"


def get_flag():
    try:
        flag = os.environ["FLAG"]
        return flag
    except KeyError:
        print("Error: Flag not found in env, setting fake flag.")
        return "gg{fakeflagfakeflag}"


def remove_db_if_exists():
    if os.path.exists(DB):
        os.remove(DB)


def open_connection():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    return (conn, cur)


def create_tables(cur):
    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    """
    )

    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS config (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        key TEXT NOT NULL UNIQUE,
        value TEXT NOT NULL
    )
    """
    )

    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS downloads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT NOT NULL,
        url TEXT NOT NULL,
        file_size INTEGER,
        status TEXT NOT NULL CHECK(status IN ('pending', 'in_progress', 'completed', 'failed')),
        download_path TEXT,
        start_time DATETIME,
        end_time DATETIME,
        error_message TEXT
    )
    """
    )


def add_admin(cur):
    password = secrets.token_hex(16)
    print(f"Admin password is: {password}")
    cur.execute(
        """
    INSERT INTO users (username, password) VALUES (?, ?)
    """,
        ("admin", sha512(password.encode()).hexdigest()),
    )


def add_config(cur):
    config_data = [
        ("download_directory", "/downloads"),
        ("max_simultaneous_downloads", "10"),
        ("auto_resume", "true"),
        ("version", "v2.5.9BetaOrAlpha-4 - Very Stable Branch"),
        ("fun_allowed", "false"),
    ]

    cur.executemany(
        """
    INSERT INTO config (key, value) VALUES (?, ?)
    """,
        config_data,
    )


def add_downloads(cur, flag):
    downloads_data = [
        (
            "wuewuewue.mp4",
            "https://www.youtube.com/watch?v=z1_9V0yVclw",
            52428800,
            "completed",
            "/downloads/wuewuewue.mp4",
            "2024-10-11 10:01:39",
            "2024-10-11 10:01:46",
            None,
        ),
        (
            "Tom___Jerry_-_070.rmvb",
            "https://www.cia.gov/library/abbottabad-compound/03/03398EE69CC92EB9C216D107A914BF92_Tom___Jerry_-_070.rmvb",
            15447729,
            "completed",
            "/downloads/Tom___Jerry_-_070.rmvb",
            "2024-10-12 14:37:01",
            "2024-10-12 14:37:04",
            None,
        ),
        (
            f"{flag}",
            "http://secret-server-for-admins-only.ggc.tf",
            len(flag),
            "completed",
            f"/downloads/{flag}",
            "2025-05-05 13:37:00",
            "2025-05-05 13:37:01",
            None,
        ),
        (
            "fun.mp3",
            "https://www.youtube.com/watch?v=L3tsYC5OYhQ",
            1,
            "failed",
            None,
            None,
            None,
            "No fun allowed",
        ),
    ]

    cur.executemany(
        """
    INSERT INTO downloads (filename, url, file_size, status, download_path, start_time, end_time, error_message)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
        downloads_data,
    )


def setup_db():
    remove_db_if_exists()
    conn, cur = open_connection()

    create_tables(cur)
    add_admin(cur)
    add_config(cur)
    add_downloads(cur, get_flag())

    conn.commit()
    cur.close()
    conn.close()
