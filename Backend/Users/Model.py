from flask_sqlalchemy import SQLAlchemy
import uuid 
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(PG_UUID, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    userAuth_id = db.Column(PG_UUID, foreign_key=True)