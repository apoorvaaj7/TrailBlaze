from flask import Flask
from flask_restful import Resource, Api
from database import db
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)

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

api.add_resource(RegisterAPI, "/register")
api.add_resource(LoginAPI, "/login")
api.add_resource(ProfileAPI, "/profile")

if __name__ == '__main__':
    app.run(debug=True)