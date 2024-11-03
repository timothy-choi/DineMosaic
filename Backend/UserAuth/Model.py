from flask_sqlalchemy import SQLAlchemy
import uuid 
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy import ForeignKey

db = SQLAlchemy()

class UserAuth(db.Model):
    __tablename__ = 'user_auth'

    id = db.Column(PG_UUID(as_uuid=True), primary_key=True)
    user_id = db.Column(PG_UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=True)
    password = db.Column(db.String(100), nullable=True) 
    email = db.Column(db.String(100), unique=True, nullable=False)
    google_id = db.Column(db.String(100), unique=True, nullable=True)
    auth_provider = db.Column(db.String(20), default="local")

    def to_dict(self):
        return {
            'id': str(self.id),
            'user_id': str(self.user_id),
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'google_id': self.google_id,
            'auth_provider': self.auth_provider
        }


