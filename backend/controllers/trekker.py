from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from database import db
from models import User, Trek, Booking

class ViewTreks(Resource):

    @jwt_required()
    def get(self):

        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)

        if not user:
            return {"success": False, "message": "User not found."}, 404

        if user.role != "Trekker":
            return {"success": False, "message": "Access Denied."}, 403
        
        if not user.is_active:
            return {"success": False, "message": "Your account has been deactivated."}, 403

        treks = Trek.query.filter_by(status="Open").all()
        data = []

        for trek in treks:
            data.append({
                "id": trek.id,
                "trek_name": trek.trek_name,
                "image_url": trek.image_url,
                "price": trek.price,
                "duration": trek.duration,
                "difficulty": trek.difficulty,
                "location": trek.location
            })
        return {"success": True, "treks": data}, 200
    

class ViewTrekDetails(Resource):

    @jwt_required()
    def get(self, trek_id):

        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)

        if not user:
            return {"success": False, "message": "User not found."}, 404

        if user.role != "Trekker":
            return {"success": False, "message": "Access Denied."}, 403
        
        if not user.is_active:
            return {"success": False, "message": "Your account has been deactivated."}, 403

        trek = Trek.query.get(trek_id)

        if not trek:
            return {"success": False, "message": "Trek not found."}, 404
        
        return {"success": True,
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
                "status": trek.status,
                "start_date": str(trek.start_date),
                "end_date": str(trek.end_date)
            }}, 200
    

class BookTrek(Resource):

    @jwt_required()
    def post(self, trek_id):

        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)

        if not user:
            return {"success": False, "message": "User not found."}, 404

        if user.role != "Trekker":
            return {"success": False, "message": "Access Denied."}, 403
        
        if not user.is_active:
            return {"success": False, "message": "Your account has been deactivated."}, 403
        
        trek = Trek.query.get(trek_id)

        if not trek:
            return {"success": False, "message": "Trek not found."}, 404
        
        if trek.status != "Open":
            return {"success": False, "message": "Bookings are closed for this trek."}, 400
        
        if trek.available_slots <= 0:
            return {"success": False, "message": "Slots are full."}, 400
        
        existing_booking = Booking.query.filter_by(user_id=current_user_id, trek_id=trek_id, status="Booked").first()
        
        if existing_booking:
            return {"success": False, "message": "You have already booked this trek."}, 400
        
        booking = Booking(
            user_id=current_user_id,
            trek_id=trek_id
        )
        trek.available_slots -= 1

        db.session.add(booking)
        db.session.commit()

        return {"success": True, "message": "Trek booked successfully."}, 201
    

class MyTreks(Resource):

    @jwt_required()
    def get(self):

        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)

        if not user:
            return {"success": False, "message": "User not found."}, 404

        if user.role != "Trekker":
            return {"success": False, "message": "Access Denied."}, 403
        
        if not user.is_active:
            return {"success": False, "message": "Your account has been deactivated."}, 403

        bookings = Booking.query.filter_by(user_id=current_user_id).all()
        data = []

        for booking in bookings:
            data.append({
                "booking_id": booking.id,
                "trek_id": booking.trek.id,
                "trek_name": booking.trek.trek_name,
                "image_url": booking.trek.image_url,
                "booking_status": booking.status,
                "start_date": str(booking.trek.start_date),
                "end_date": str(booking.trek.end_date)
            })

        return {"success": True, "my_treks": data}, 200
    

class CancelBooking(Resource):

    @jwt_required()
    def patch(self, booking_id):

        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)

        if not user:
            return {"success": False, "message": "User not found."}, 404

        if user.role != "Trekker":
            return {"success": False, "message": "Access Denied."}, 403
        
        if not user.is_active:
            return {"success": False, "message": "Your account has been deactivated."}, 403

        booking = Booking.query.get(booking_id)

        if not booking:
            return {"success": False, "message": "Booking not found."}, 404

        if booking.user_id != current_user_id:
            return {"success": False, "message": "You cannot cancel this booking."}, 403

        if booking.status != "Booked":
            return {"success": False, "message": "Booking is already cancelled or completed."}, 400
        
        if booking.trek.status == "Completed":
            return {"success": False, "message": "Completed treks cannot be cancelled."}, 400

        booking.status = "Cancelled"
        booking.payment_status = "Refunded"
        booking.trek.available_slots += 1
        db.session.commit()

        return {"success": True, "message": "Booking cancelled successfully."}, 200