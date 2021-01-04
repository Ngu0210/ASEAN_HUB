from flask import Blueprint, jsonify, abort, g, request
from main import db
from models.Drink_Menu import Drink_Menu
from schemas.Drink_MenuSchema import drink_menu_schema, drink_menus_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_service import verify_user
from sqlalchemy.orm import joinedload

drink_menu = Blueprint("drink_menu", __name__, url_prefix="/menu/drink")

@drink_menu.route("/", methods=[ "GET"])
def drink_menu_index():
    drink_menu = Drink_Menu.query.all()
    serialized_data = drink_menus_schema.dump(drink_menu)
    return jsonify(serialized_data)

@drink_menu.route("/", methods=["POST"])
def drink_menu_create():
    #Creates new dish in menu
    drink_menu_fields = drink_menu_schema.load(request.json)

    drink_menu = Drink_Menu()
    drink_menu.title = drink_menu_fields["title"]
    drink_menu.price = drink_menu_fields["price"]
    drink_menu.ice = drink_menu_fields["ice"]

    db.session.add(drink_menu)
    db.session.commit()

    return jsonify(drink_menu_schema.dump(drink_menu))

@drink_menu.route("/<int:id>", methods=["GET"])
def drink_menu_show(id):
    #Returns specific dish
    drink_menu = Drink_Menu.query.get(id)
    return jsonify(drink_menu_schema.dump(drink_menu))

@drink_menu.route("/<int:id>", methods=["PUT", "PATCH"])
# @jwt_required
def drink_menu_update(id):
    #Updates specific dish
    drink_menu_fields = drink_menu_schema.load(request.json)

    drink_menu = drink_Menu.query.filter_by(id=id)

    drink_menu.update(menu_fields)
    db.session.commit()

    return jsonify(drink_menu_schema.dump(drink_menu[0]))

@drink_menu.route("/<int:id>", methods=["DELETE"])
# @jwt_required
def drink_menu_delete(id):
    #Deletes specific dish

    drink_menu = Menu.query.filter_by(id=id).first()

    if not drink_menu:
        return abort(400)

    db.session.delete(drink_menu)
    db.session.commit()

    return jsonify(drink_menu_schema.dump(drink_menu))