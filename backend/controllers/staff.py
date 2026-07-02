from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from database import db
from models import User, StaffProfile, Trek, Booking

class StaffDashboard(Resource):

    @jwt_required()
    def get(self):

        current_user_id = get_jwt_identity()
        staff = User.query.get(current_user_id)

        if not staff:
            return {"success": False, "message": "User not found."}, 404

        if staff.role != "Staff":
            return {"success": False, "message": "Access Denied."}, 403
        
        if not staff.is_active:
            return {"success": False, "message": "Your account has been deactivated."}, 403

        staff_profile = StaffProfile.query.filter_by(user_id=current_user_id).first()
        assigned_treks = Trek.query.filter_by(staff_id=staff_profile.id).all()

        registered_trekkers = 0
        trek_data = []

        for trek in assigned_treks:
            registered_trekkers += Booking.query.filter_by(trek_id=trek.id, status="Booked").count()

            trek_data.append({
                "id": trek.id,
                "trek_name": trek.trek_name,
                "status": trek.status,
                "start_date": str(trek.start_date),
                "end_date": str(trek.end_date)
            })

        return {
            "success": True,
            "dashboard": {
                "assigned_treks": len(assigned_treks),
                "registered_trekkers": registered_trekkers,
                "treks": trek_data
            }} ,200


class TrekDetails(Resource):

    @jwt_required()
    def get(self, trek_id):

        current_user_id = get_jwt_identity()
        staff = User.query.get(current_user_id)

        if not staff:
            return {"success": False, "message": "User not found."}, 404

        if staff.role != "Staff":
            return {"success": False, "message": "Access Denied."}, 403
        
        if not staff.is_active:
            return {"success": False, "message": "Your account has been deactivated."}, 403

        staff_profile = StaffProfile.query.filter_by(user_id=current_user_id).first()
        trek = Trek.query.get(trek_id)

        if not trek:
            return {"success": False, "message": "Trek not found."} ,404

        if trek.staff_id != staff_profile.id:
            return {"success": False, "message": "You are not assigned to this trek."} ,403

        total_participants = Booking.query.filter_by(trek_id=trek.id, status="Booked").count()

        return {"success": True, "trek": {
                "id": trek.id,
                "trek_name": trek.trek_name,
                "description": trek.description,
                "location": trek.location,
                "difficulty": trek.difficulty,
                "duration": trek.duration,
                "price": trek.price,
                "image_url": trek.image_url,
                "available_slots": trek.available_slots,
                "status": trek.status,
                "start_date": str(trek.start_date),
                "end_date": str(trek.end_date),
                "participants": total_participants
            }} ,200
    
class Trekkers(Resource):

    @jwt_required()
    def get(self, trek_id):

        current_user_id = get_jwt_identity()
        staff = User.query.get(current_user_id)

        if not staff:
            return {"success": False, "message": "User not found."}, 404

        if staff.role != "Staff":
            return {"success": False, "message": "Access Denied."}, 403
        
        if not staff.is_active:
            return {"success": False, "message": "Your account has been deactivated."}, 403

        staff_profile = StaffProfile.query.filter_by(user_id=current_user_id).first()
        trek = Trek.query.get(trek_id)

        if not trek:
            return {"success": False, "message": "Trek not found."}, 404

        if trek.staff_id != staff_profile.id:
            return {"success": False, "message": "You are not assigned to this trek."}, 403
        
        bookings = Booking.query.filter_by(trek_id=trek.id, status="Booked").all()

        trekkers = []

        for booking in bookings:
            trekkers.append({
                "booking_id": booking.id,
                "user_id": booking.user.id,
                "full_name": booking.user.full_name,
                "email": booking.user.email,
                "phone": booking.user.phone,
                "booking_date": str(booking.booking_date),
                "payment_status": booking.payment_status
            })
        return {"success": True, "trekkers": trekkers}, 200
    
    
class UpdateSlots(Resource):

    @jwt_required()
    def patch(self, trek_id):

        current_user_id = get_jwt_identity()
        staff = User.query.get(current_user_id)

        if not staff:
            return {"success": False, "message": "User not found."}, 404

        if staff.role != "Staff":
            return {"success": False, "message": "Access Denied."}, 403
        
        if not staff.is_active:
            return {"success": False, "message": "Your account has been deactivated."}, 403

        staff_profile = StaffProfile.query.filter_by(user_id=current_user_id).first()
        trek = Trek.query.get(trek_id)

        if not trek:
            return {"success": False, "message": "Trek not found."}, 404

        if trek.staff_id != staff_profile.id:
            return {"success": False, "message": "You are not assigned to this trek."}, 403

        data = request.get_json()
        available_slots = data.get("available_slots")

        if available_slots <= 0:
            return {"success": False, "message": "Available slots must be greater than 0."}, 400

        trek.available_slots = available_slots
        db.session.commit()

        return {"success": True, "message": "Available slots updated successfully."}, 200
    

class UpdateTrekStatus(Resource):

    @jwt_required()
    def patch(self, trek_id):

        current_user_id = get_jwt_identity()
        staff = User.query.get(current_user_id)

        if not staff:
            return {"success": False, "message": "User not found."}, 404

        if staff.role != "Staff":
            return {"success": False, "message": "Access Denied."}, 403
        
        if not staff.is_active:
            return {"success": False, "message": "Your account has been deactivated."}, 403

        staff_profile = StaffProfile.query.filter_by(user_id=current_user_id).first()
        trek = Trek.query.get(trek_id)

        if not trek:
            return {"success": False, "message": "Trek not found."}, 404

        if trek.staff_id != staff_profile.id:
            return {"success": False, "message": "You are not assigned to this trek."}, 403

        data = request.get_json()
        status = data.get("status")

        if trek.status == "Open" and status not in ["Closed", "Ongoing"]:
            return {"success": False, "message": "Invalid status."}, 400

        if trek.status == "Closed" and status != "Open":
            return {"success": False, "message": "Invalid status."}, 400

        if trek.status == "Ongoing" and status != "Completed":
            return {"success": False, "message": "Invalid status."}, 400

        if trek.status == "Completed":
            return {"success": False, "message": "Completed trek cannot be updated."}, 400

        trek.status = status

        if status == "Completed":
            bookings = Booking.query.filter_by(trek_id=trek.id, status="Booked").all()
            for booking in bookings:
                booking.status = "Completed"
                
        db.session.commit()

        return {"success": True, "message": "Trek status updated successfully."}, 200