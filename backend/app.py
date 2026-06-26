from flask import Flask, request
from flask_restful import Resource, Api
from database import db

app = Flask(__name__)
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///trek.db"

db.init_app(app)

from models import *

with app.app_context():
    db.create_all()

# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}
#     def post(self):
#         data = request.get_json()
#         new

# api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(debug=True)