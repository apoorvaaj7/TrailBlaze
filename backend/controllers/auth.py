from flask_restful import Resource
from flask import request
from models import User
from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

class RegisterAPI(Resource):
    def post(self):
        data = request.get_json()
        full_name = data.get("full_name", "").strip()
        email = data.get("email", "").strip().lower()
        password = data.get("password", "")
        phone = data.get("phone", "").strip()
        address = data.get("address", "").strip()

        if not full_name or not email or not password:
            return {'msg' : "fill the mandatory fields."}, 400
        
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return {
                "success": False,
                "message": "Email already registered."
            }, 409

        user = User(full_name = full_name, email=email, password=generate_password_hash(password), phone=phone, address=address, role="Trekker")
        
        try:
            db.session.add(user)
            db.session.commit()
            return {
                "success": True,
                "message": "Registration Successful"
            }, 201

        except Exception as e:
            db.session.rollback()
            return {"msg": str(e)}, 500
        

class LoginAPI(Resource):
    def post(self):
        data = request.get_json()

        email = data.get("email", "").strip().lower()
        password = data.get("password", "")

        if not email or not password:
            return{
                "success": False,
                "message": "Credentials required."
            }, 400
        
        user = User.query.filter_by(email=email).first()

        if not user:
            return{
                "success": False,
                "message": "Invalid credentials."
            }, 401
        
        if not check_password_hash(user.password, password):
            return {
                "success": False,
                "message": "Invalid credentials."
            }, 401
        
        if not user.is_active:
            return {
                "success": False,
                "message": "Your account has been deactivated."
            }, 403
        
        access_token = create_access_token(identity=str(user.id))
        return{
            "success": True,
            "message": "Login Successful",
            "access_token": access_token,
            "role": user.role,
            "user_id": user.id,
            "full_name": user.full_name
        }, 200