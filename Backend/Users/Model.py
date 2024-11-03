from flask_sqlalchemy import SQLAlchemy
import uuid 
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy import ForeignKey


db = SQLAlchemy()

class Users(db.Model):
    _tablename_ = 'users'

    id = db.Column(PG_UUID(as_uuid=True), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    userAuth_id = db.Column(PG_UUID(as_uuid=True), ForeignKey('user_auth.id'), nullable=False)