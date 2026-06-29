from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import User

class ProfileAPI(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()

        user = User.query.get(user_id)
        return{
            "success": True,
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "role": user.role
        }, 200