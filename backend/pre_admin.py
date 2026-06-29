from app import app
from database import db
from models import User
from werkzeug.security import generate_password_hash

with app.app_context():

    admin = User.query.filter_by(email="admin@trailblaze.com").first()

    if not admin:
        admin = User(
            full_name = "Admin",
            email = "admin@trailblaze.com",
            password = generate_password_hash("admin123"),
            phone = "9580222777",
            address = "TrailBlaze HQ",
            role = "Admin"
        )

        db.session.add(admin)
        db.session.commit()

        print("admin created successfully.")
    
    else:
        print("admin already exists")