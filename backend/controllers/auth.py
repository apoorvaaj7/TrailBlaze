from flask_restful import Resource, request
from models import User
from database import db
from werkzeug.security import generate_password_hash, check_password_hash

class Register(Resource):
    def post(self):
        data = request.get_json()
        full_name = data.get("full_name")
        email = data.get("email")
        password = data.get("password")

        if not full_name or not email or not password:
            return {'msg' : "all the fields are required"}

        user = User(full_name = full_name, email=email, password=generate_password_hash(password))
        db.session.add(user)
        