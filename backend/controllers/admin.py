from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash
from datetime import datetime

from database import db
from models import User, StaffProfile, Trek


# CREATE STAFF
class CreateStaffAPI(Resource):
    @jwt_required()
    def post(self):
        current_user_id = get_jwt_identity()

        admin = User.query.get(current_user_id)

        if not admin:
            return{"success": False, "message": "User not found."}, 404

        if admin.role != "Admin":
            return{"success": False, "message": "Access Denied."}, 403
        
        data = request.get_json()

        full_name = data.get("full_name", "").strip()
        email = data.get("email", "").strip().lower()
        password = data.get("password", "")
        phone = data.get("phone", "").strip()
        address = data.get("address", "").strip()
        qualification = data.get("qualification", "").strip()
        experience = data.get("experience")
        specialization = data.get("specialization", "").strip()

        if not all([full_name, email, password, qualification]):
            return{"success": False, "message": "Fill all mandatory fields."}, 400
        
        existing_user = User.query.filter_by(email = email).first()
        if existing_user:
            return{"success": False, "message": "Email already exists."}, 409
        
        
        #  STAFF
        staff_user = User(
            full_name = full_name,
            email = email,
            password = generate_password_hash(password),
            phone = phone,
            address = address,
            role = "Staff"
        )
        db.session.add(staff_user)
        db.session.flush()

        staff_profile = StaffProfile(
            user_id = staff_user.id,
            qualification = qualification,
            experience = experience,
            specialization = specialization
        )
        db.session.add(staff_profile)
        db.session.commit()

        return{
            "success": True,
            "message": "Staff created successfully."
        }, 201


# CREATE TREK
class CreateTrek(Resource):
    @jwt_required()
    
    def post(self):
        current_user_id = get_jwt_identity()

        admin = User.query.get(current_user_id)

        if not admin:
            return{"success": False, "message": "User not found."}, 404

        if admin.role != "Admin":
            return{"success": False, "message": "Access Denied."}, 403
        
        data = request.get_json()

        trek_name = data.get("trek_name", "").strip()
        description = data.get("description", "").strip()
        location = data.get("location", "").strip()
        difficulty = data.get("difficulty", "").strip()
        duration = data.get("duration")
        price = data.get("price")
        image_url = data.get("image_url", "").strip()
        available_slots = data.get("available_slots")
        staff_id = data.get("staff_id")
        status = data.get("status", "").strip()
        start_date = data.get("start_date")
        end_date = data.get("end_date")

        if not all([trek_name, description, location, difficulty, duration, price, image_url, available_slots, staff_id, status, start_date, end_date]):
            return{"success": False, "message": "Please fill all the required fields"}, 400
        
        staff = StaffProfile.query.get(staff_id)

        if not staff:
            return {"success": False, "message": "Assigned staff not found."}
        
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

        if end_date < start_date:
            return {
                "success": False, "message": "End date cannot be before start date."}, 400
        
        trek = Trek(
            trek_name = trek_name,
            description = description,
            location = location,
            difficulty = difficulty,
            duration = duration,
            price = price,
            image_url = image_url,
            available_slots = available_slots,
            staff_id = staff_id,
            status = status,
            start_date = start_date,
            end_date = end_date
        )
        db.session.add(trek)
        db.session.commit()

        return {"success": True, "message": "Trek created successfully!"}, 201