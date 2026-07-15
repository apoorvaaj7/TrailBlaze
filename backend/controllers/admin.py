from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash
from datetime import datetime
from sqlalchemy import or_

from database import db, cache
from models import User, StaffProfile, Trek, Booking


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

        from tasks import staff_welcome_email
        staff_welcome_email.delay(staff_user.id, password)

        return{"success": True, "message": "Staff created successfully."}, 201


class AllStaff(Resource):
    @jwt_required()
    def get(self):

        current_user_id = get_jwt_identity()
        admin = User.query.get(current_user_id)

        if not admin:
            return {"success": False, "message": "User not found."}, 404

        if admin.role != "Admin":
            return {"success": False, "message": "Access Denied."}, 403

        staffs = StaffProfile.query.all()

        data = []

        for staff in staffs:
            data.append({
                "id": staff.id,
                "user_id": staff.user.id,
                "full_name": staff.user.full_name,
                "email": staff.user.email,
                "phone": staff.user.phone,
                "qualification": staff.qualification,
                "experience": staff.experience,
                "specialization": staff.specialization,
                "is_active": staff.user.is_active
            })
        return { "success": True, "staff": data}, 200


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
        start_date = data.get("start_date")
        end_date = data.get("end_date")

        if not all([trek_name, description, location, difficulty, duration, price, image_url, available_slots, staff_id, start_date, end_date]):
            return{"success": False, "message": "Please fill all the required fields"}, 400
        
        staff = StaffProfile.query.get(staff_id)

        if not staff:
            return {"success": False, "message": "Assigned staff not found."}, 404
        
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

        if end_date < start_date:
            return {
                "success": False, "message": "End date cannot be before start date."}, 400
        
        if difficulty not in["Easy", "Moderate", "Hard"]:
            return{"success": False, "message": "Invalid difficulty"}, 400
        
        if available_slots <= 0:
            return {"success": False, "message": "Slots ca'nt be zero."}, 400
        
        if price <= 0:
            return {"success": False, "message": "Price must be greater than 0."}, 400
        
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
            start_date = start_date,
            end_date = end_date
        )
        db.session.add(trek)
        db.session.commit()

        return {"success": True, "message": "Trek created successfully!"}, 201
    

# SHOW ALL TREKS
class AllTreks(Resource):
    @jwt_required()

    def get(self):
        current_user_id = get_jwt_identity()
        admin = User.query.get(current_user_id)

        if not admin:
            return{"success": False, "message": "User not found."}, 404

        if admin.role != "Admin":
            return{"success": False, "message": "Access Denied."}, 403
        
        treks = Trek.query.all()
        data = []

        for trek in treks:
            data.append({
                "id" : trek.id,
                "trek_name" : trek.trek_name,
                "description" : trek.description,
                "location" : trek.location,
                "difficulty" : trek.difficulty,
                "duration" : trek.duration,
                "price" : trek.price,
                "image_url" : trek.image_url,
                "available_slots" : trek.available_slots,
                "staff_name": trek.staff.user.full_name,
                "staff_id" : trek.staff_id,
                "status" : trek.status,
                "start_date" : str(trek.start_date),
                "end_date" : str(trek.end_date)
            })
        return {"success": True, "treks": data}, 200
    
# UPDATE A TREK

class AdminTrekDetails(Resource):
    @jwt_required()
    def get(self, trek_id):

        current_user_id = get_jwt_identity()
        admin = User.query.get(current_user_id)

        if not admin:
            return {"success": False, "message": "User not found."}, 404

        if admin.role != "Admin":
            return {"success": False, "message": "Access Denied."}, 403

        trek = Trek.query.get(trek_id)
        if not trek:
            return {"success": False, "message": "Trek not found."}, 404
        
        if trek.status != "Open":
            return {"success": False, "message": "Only open treks can be edited."}, 400
        
        if trek.bookings:
            return {"success": False, "message": "Booked treks can not be deleted."}, 400

        return {
            "success": True,
            "trek": {
                "id": trek.id,
                "trek_name": trek.trek_name,
                "description": trek.description,
                "location": trek.location,
                "difficulty": trek.difficulty,
                "duration": trek.duration,
                "price": trek.price,
                "image_url": trek.image_url,
                "available_slots": trek.available_slots,
                "staff_id": trek.staff_id,
                "staff_name": trek.staff.user.full_name,
                "start_date": str(trek.start_date),
                "end_date": str(trek.end_date)
            }
        }, 200


class UpdateTrek(Resource):
    @jwt_required()

    def patch(self, trek_id):
        current_user_id = get_jwt_identity()

        admin = User.query.get(current_user_id)

        if not admin:
            return{"success": False, "message": "User not found."}, 404

        if admin.role != "Admin":
            return{"success": False, "message": "Access Denied."}, 403
        
        if trek.status != "Open":
            return {"success": False, "message": "Only open treks can be edited."}, 400
        
        if trek.bookings:
            return {"success": False, "message": "Booked treks can not be deleted."}, 400
        
        trek = Trek.query.get(trek_id)

        if not trek:
            return {"success": False, "message": "Trek not found."}, 404
        
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
        start_date = data.get("start_date")
        end_date = data.get("end_date")

        if trek_name:
            trek.trek_name = trek_name

        if description:
            trek.description = description

        if location:
            trek.location = location
        
        if difficulty:
            if difficulty not in ["Easy", "Moderate", "Hard"]:
                return {"success": False, "message": "Invalid difficulty."}, 400
            trek.difficulty = difficulty
        
        if duration is not None:
            trek.duration = duration

        if price is not None:
            if price <= 0:
                return {
                    "success": False, "message": "Price must be greater than 0."}, 400
            trek.price = price
        
        if image_url:
            trek.image_url = image_url

        if available_slots is not None:
            if available_slots <= 0:
                return {
                    "success": False, "message": "Available slots must be greater than 0."}, 400
            trek.available_slots = available_slots

        if staff_id is not None:
            staff = StaffProfile.query.get(staff_id)
            if not staff:
                return {"success": False, "message": "Assigned staff not found."}, 404
            trek.staff_id = staff_id
        
        if start_date:
            trek.start_date = datetime.strptime(start_date, "%Y-%m-%d").date()

        if end_date:
            trek.end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

        if trek.end_date < trek.start_date:
            return {"success": False, "message": "End date cannot be before start date."}, 400
        
        db.session.commit()
        return {"success": True, "message": "Trek updated successfully."}, 200
    
# DELETE A TREK
class DeleteTrek(Resource):
    @jwt_required()

    def delete(self, trek_id):
        current_user_id = get_jwt_identity()

        admin = User.query.get(current_user_id)

        if not admin:
            return{"success": False, "message": "User not found."}, 404

        if admin.role != "Admin":
            return{"success": False, "message": "Access Denied."}, 403
        
        trek = Trek.query.get(trek_id)

        if not trek:
            return {"success": False, "message": "Trek not found."}, 404
        
        if trek.status != "Open":
            return {"success": False, "message": "Only open treks can be deleted."}, 400
        
        if trek.bookings:
            return {"success": False, "message": "Booked treks can not be deleted."}, 400
        
        db.session.delete(trek)
        db.session.commit()

        return {"success": True, "message": "Trek deleted successfully."}, 200
    
# DASHBOARD
class AdminDashboard(Resource):
    @jwt_required()
    @cache.cached(timeout=60)
    def get(self):
        current_user_id = get_jwt_identity()

        admin = User.query.get(current_user_id)

        if not admin:
            return{"success": False, "message": "User not found."}, 404

        if admin.role != "Admin":
            return{"success": False, "message": "Access Denied."}, 403
        
        total_users = User.query.filter_by(role="Trekker", is_active=True).count()
        total_staff = User.query.filter_by(role="Staff", is_active=True).count()
        total_treks = Trek.query.count()
        total_bookings = Booking.query.count()
        open_treks = Trek.query.filter_by(status="Open").count()
        closed_treks = Trek.query.filter_by(status="Closed").count()
        completed_treks = Trek.query.filter_by(status="Completed").count()

        recent_treks = Trek.query.order_by(Trek.id.desc()).limit(3).all()
        recent_data = []

        for trek in recent_treks:
            recent_data.append({
                "id": trek.id,
                "trek_name": trek.trek_name,
                "location": trek.location,
                "difficulty": trek.difficulty,
                "price": trek.price,
                "status": trek.status,
                "image_url": trek.image_url
            })

        return {
            "success": True,
    
            "dashboard": {
                "total_users": total_users,
                "total_staff": total_staff,
                "total_treks": total_treks,
                "total_bookings": total_bookings,
                "recent_treks": recent_data
            }
        }, 200
    

class AllTrekkers(Resource):
    @jwt_required()
    def get(self):
        current_user_id = get_jwt_identity()
        admin = User.query.get(current_user_id)

        if not admin:
            return {"success": False, "message": "User not found."}, 404

        if admin.role != "Admin":
            return {"success": False, "message": "Access Denied."}, 403

        trekkers = User.query.filter_by(role="Trekker").all()
        data = []

        for trekker in trekkers:
            total_bookings = Booking.query.filter_by(user_id=trekker.id).count()

            data.append({
                "id": trekker.id,
                "full_name": trekker.full_name,
                "email": trekker.email,
                "phone": trekker.phone,
                "address": trekker.address,
                "bookings": total_bookings,
                "is_active": trekker.is_active
            })
        return { "success": True, "trekkers": data}, 200

    
class AllBookings(Resource):
    @jwt_required()
    def get(self):
        current_user_id = get_jwt_identity()
        admin = User.query.get(current_user_id)

        if not admin:
            return {"success": False, "message": "User not found."}, 404

        if admin.role != "Admin":
            return { "success": False, "message": "Access Denied."}, 403

        bookings = Booking.query.all()

        data = []
        for booking in bookings:

            data.append({
                "booking_id": booking.id,
                "trekker_name": booking.user.full_name,
                "trek_name": booking.trek.trek_name,
                "booking_date": str(booking.booking_date),
                "booking_status": booking.status,
                "payment_status": booking.payment_status
            })
        return { "success": True, "bookings": data}, 200


# BLACKLISTING and ACTIVATING 

class UpdateUserStatus(Resource):
    @jwt_required()
    def patch(self, user_id):

        current_user_id = get_jwt_identity()
        admin = User.query.get(current_user_id)

        if not admin:
            return {"success": False, "message": "User not found."}, 404

        if admin.role != "Admin":
            return {"success": False, "message": "Access Denied."}, 403

        user = User.query.get(user_id)

        if not user:
            return {"success": False, "message": "User not found."}, 404

        data = request.get_json()
        is_active = data.get("is_active")

        user.is_active = is_active
        db.session.commit()

        return {"success": True, "message": "User status updated successfully."}, 200
    

# SEARCH 
class AdminSearch(Resource):

    @jwt_required()
    def get(self):
        current_user_id = get_jwt_identity()
        admin = User.query.get(current_user_id)

        if not admin:
            return {"success": False, "message": "User not found."}, 404

        if admin.role != "Admin":
            return {"success": False, "message": "Access Denied."}, 403

        query = request.args.get("query", "").strip()

        users = User.query.filter(
            or_(
                User.full_name.ilike(f"%{query}%"),
                User.email.ilike(f"%{query}%")
            )).all()

        treks = Trek.query.filter(
            or_(
                Trek.trek_name.ilike(f"%{query}%"),
                Trek.location.ilike(f"%{query}%")
            )).all()

        users_data = []

        for user in users:
            users_data.append({
                "id": user.id,
                "full_name": user.full_name,
                "email": user.email,
                "role": user.role,
                "is_active": user.is_active
            })

        treks_data = []

        for trek in treks:
            treks_data.append({
                "id": trek.id,
                "trek_name": trek.trek_name,
                "location": trek.location,
                "difficulty": trek.difficulty,
                "price": trek.price,
                "status": trek.status
            })

        return {"success": True, "users": users_data, "treks": treks_data}, 200