from flask import Flask
from flask_restful import Resource, Api
from database import db
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///trek.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "trailblaze_secret_key"
app.config["JWT_SECRET_KEY"] = "trailblaze_jwt_secret"

db.init_app(app)
jwt = JWTManager(app)

from models import *

with app.app_context():
    db.create_all()

from controllers.auth import RegisterAPI, LoginAPI
from controllers.profile import ProfileAPI
from controllers.admin import CreateStaffAPI, CreateTrek, AllStaff, AllTreks, AdminTrekDetails, UpdateTrek, DeleteTrek, AdminDashboard, AllTrekkers, AllBookings, UpdateUserStatus
from controllers.staff import StaffDashboard, TrekDetails, Trekkers, UpdateSlots, UpdateTrekStatus
from controllers.trekker import ViewTreks, ViewTrekDetails, BookTrek, MyTreks, CancelBooking


api.add_resource(RegisterAPI, "/register")
api.add_resource(LoginAPI, "/login")
api.add_resource(ProfileAPI, "/profile")
api.add_resource(CreateStaffAPI, "/admin/staff")
api.add_resource(AllStaff, "/admin/staff")
api.add_resource(CreateTrek, "/admin/treks")
api.add_resource(AllTreks, "/admin/treks")
api.add_resource(AdminTrekDetails, "/admin/treks/<int:trek_id>")
api.add_resource(UpdateTrek, "/admin/treks/<int:trek_id>")
api.add_resource(DeleteTrek, "/admin/treks/<int:trek_id>")
api.add_resource(AdminDashboard, "/admin/dashboard")
api.add_resource(AllTrekkers, "/admin/trekkers")
api.add_resource(AllBookings, "/admin/bookings")
api.add_resource(UpdateUserStatus, "/admin/users/<int:user_id>/status")


api.add_resource(StaffDashboard, "/staff/dashboard")
api.add_resource(TrekDetails,"/staff/treks/<int:trek_id>")
api.add_resource(Trekkers, "/staff/treks/<int:trek_id>/trekkers")
api.add_resource(UpdateSlots, "/staff/treks/<int:trek_id>/slots")
api.add_resource(UpdateTrekStatus, "/staff/treks/<int:trek_id>/status")


api.add_resource(ViewTreks, "/treks")
api.add_resource(ViewTrekDetails, "/treks/<int:trek_id>")
api.add_resource(BookTrek, "/treks/<int:trek_id>")
api.add_resource(MyTreks, "/my_treks")
api.add_resource(CancelBooking, "/bookings/<int:booking_id>/cancel")


if __name__ == '__main__':
    app.run(debug=True)