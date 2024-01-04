import json
import socket
import urllib.parse

import db


BLACKLIST = [
    "012",
    "10",
    "0xa",
    "0177",
    "127",
    "0x7f",
    "0254",
    "172.16",
    "172.17",
    "172.18",
    "172.19",
    "172.20",
    "172.21",
    "172.22",
    "172.23",
    "172.24",
    "172.25",
    "172.26",
    "172.27",
    "172.28",
    "172.29",
    "172.30",
    "172.31",
    "0xac",
    "0300.0250",
    "192.168",
    "0xc0.0xa8",
]
LOCAL_ADDRESS = "127.0.0.1"
BACKUP_HEADER = "x-real-host"
SESSION_COOKIE_NAME = "admin_sesh"

SESSIONS = {}


def get_auth(request):
    cookie = request.cookies.get(SESSION_COOKIE_NAME, "")
    user = SESSIONS.get(cookie)
    if user:
        user.update(db.get_user_details(user))
        return user
    return None


def is_admin(cookie):
    auth = get_auth(cookie)
    if auth:
        return auth.is_admin
    return False


def validate_blob(blob):
    if len(blob) > 4096:
        return None

    try:
        data = json.loads(blob)
        if "id" not in data:
            return None
        if "stats" not in data:
            return None
    except ValueError as _:
        return None

    return blob


def validate_host(host):
    try:
        address = socket.gethostbyname(host)
        if any(address.startswith(b) for b in BLACKLIST):
            return None
    except Exception as _:
        if any(host.startswith(b) for b in BLACKLIST):
            return None

    return host


def is_localhost(req):
    return (
        req.remote_addr == LOCAL_ADDRESS
        or req.headers.get(BACKUP_HEADER) == LOCAL_ADDRESS
    )
