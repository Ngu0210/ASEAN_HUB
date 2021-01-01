from flask import Blueprint, about
from schemas.UserSchema import user_schema
from models.User import Users

auth = Blueprint("auth", __name__, url_prefix="/auth")

@auth.route("/register", methods=["POST"])
def auth_register():
    user_fields = user.schema.load(request.json)
    
    user = User.query.filter_by(email=user_fields["email"]).first()

    if user:
        return abort(400, description="Email already registered")