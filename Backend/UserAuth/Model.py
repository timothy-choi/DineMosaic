from flask_sqlalchemy import SQLAlchemy
import uuid 
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

db = SQLAlchemy()

class UserAuth(db.Model):
    id = db.Column(PG_UUID, primary_key=True)
    user_id = db.Column(PG_UUID, foreign_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False) 
    email = db.Column(db.String, unique=True, nullable=False)
    google_id = db.Column(db.String, nullable=True)
    auth_provider = db.Column(db.String, default="local")