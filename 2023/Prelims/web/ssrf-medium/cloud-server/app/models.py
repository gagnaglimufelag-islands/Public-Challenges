from app import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_utils import UUIDType
import uuid
from dataclasses import dataclass


def get_uuid_id():
    rdm = uuid.uuid4
    return rdm


@dataclass
class File(db.Model):
    __tablename__ = "file"

    id: uuid.uuid4
    name: str
    download_url: str
    session: str

    id = db.Column(UUIDType(binary=False), primary_key=True, default=get_uuid_id(), unique=True)
    session = db.Column(db.String(16), unique=False)
    name = db.Column(db.String(100), unique=False)
    download_url = db.Column(db.String(1000), unique=False)

    def __init__(self, name, session):
        self.name = name
        self.session = session
        self.download_url = f"http://fileserver/{session}/{name}"


class Config(db.Model):
    __tablename__ = "config"
    id: int
    name: str
    color: str

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(100), unique=False)
    color = db.Column(db.String(100), unique=False)




if __name__ == "__main__":

    # Run this file directly to create the database tables.
    print("Creating database tables...")
    db.create_all()
    print("Done!")
