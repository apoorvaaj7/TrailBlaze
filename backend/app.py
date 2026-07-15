from flask import Flask
from flask_restful import Resource, Api
from database import db, mail, cache
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from werkzeug.security import generate_password_hash
from models import User
from dotenv import load_dotenv
import os

load_dotenv()
password = os.getenv("MAIL_APP_PASS")

app = Flask(__name__)
api = Api(app)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///trek.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "trailblaze_secret_key"
app.config["JWT_SECRET_KEY"] = "trailblaze_jwt_secret"

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_EMAIL')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_APP_PASS')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_EMAIL')

app.config['CACHE_DEFAULT_TIMEOUT'] = 60
app.config['CELERY_BROKER_URL'] = os.getenv('BROKER_URL', 'redis://localhost:6379/0')
app.config['CELERY_RESULT_BACKEND'] = os.getenv('RESULT_BACKEND', 'redis://localhost:6379/0')

try:
    import redis
    redis.Redis.from_url('redis://localhost:6379/1').ping()
    app.config['CACHE_TYPE'] = 'RedisCache'
    app.config['CACHE_REDIS_URL'] = 'redis://localhost:6379/1'
except Exception:
    app.config['CACHE_TYPE'] = 'SimpleCache'

mail.init_app(app)
cache.init_app(app)
db.init_app(app)
jwt = JWTManager(app)

from models import *

with app.app_context():
    db.create_all()

    admin = User.query.filter_by(email="apoorvajaiswal590@gmail.com").first()

    if not admin:
        admin = User(
            full_name="Admin",
            email="apoorvajaiswal590@gmail.com",
            password=generate_password_hash("admin123"),
            phone="9580222777",
            address="TrailBlaze HQ",
            role="Admin",
            is_active=True
        )
        db.session.add(admin)
        db.session.commit()

        print("Admin created.")


from controllers.auth import RegisterAPI, LoginAPI, PublicTreks
from controllers.profile import ProfileAPI
from controllers.admin import CreateStaffAPI, CreateTrek, AllStaff, AllTreks, AdminTrekDetails, UpdateTrek, DeleteTrek, AdminDashboard, AllTrekkers, AllBookings, UpdateUserStatus, AdminSearch
from controllers.staff import StaffDashboard, TrekDetails, Trekkers, UpdateSlots, UpdateTrekStatus
from controllers.trekker import ViewTreks, ViewTrekDetails, BookTrek, MyTreks, CancelBooking, PayForTrek, ExportCSV, SearchTreks


api.add_resource(RegisterAPI, "/register")
api.add_resource(LoginAPI, "/login")
api.add_resource(PublicTreks, "/public-treks")

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
api.add_resource(AdminSearch, "/admin/search")


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
api.add_resource(PayForTrek, "/bookings/<int:booking_id>/pay")
api.add_resource(ExportCSV, "/export_csv")
api.add_resource(SearchTreks, "/treks/search")


if __name__ == '__main__':
    app.run(debug=True)