from flask import Flask, request
from flask_restful import Resource, Api
from database import db

app = Flask(__name__)
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///trek.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "trailblaze-secret-key"

db.init_app(app)

from models import *

with app.app_context():
    db.create_all()



if __name__ == '__main__':
    app.run(debug=True)