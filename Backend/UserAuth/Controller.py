from flask import Flask, jsonify, request
from Model import db, UserAuth
import uuid

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ''  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/UserAuth/<uuid:user_auth_id>', method=['GET'])
def get_user_auth_by_id(user_auth_id):
    userAuth = UserAuth.query.get(user_auth_id)

    if userAuth:
        return jsonify(userAuth.to_dict())
    return jsonify({'error': 'Task not found'}), 404
