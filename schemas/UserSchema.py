from main import ma
from models.User import User
from marshmallow.validate import Length, Email

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_only = ["password"]

    email = ma.String(required=True, validate=[Length(min=4), Email()])
    password = ma.String(required=True, validate=[Length(min=6)])
    first_name = ma.String(validate=[Length(min=2)])
    last_name = ma.String(validate=[Length(min=2)])

class RegisterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_only = ["password"]

    email = ma.String(required=True, validate=[Length(min=4), Email()])
    password = ma.String(required=True, validate=[Length(min=6)])
    first_name = ma.String(required=True, validate=[Length(min=2)])
    last_name = ma.String(required=True, validate=[Length(min=2)])
    print("hello")

register_schema = RegisterSchema()
user_schema = UserSchema()
users_schema = UserSchema(many=True)