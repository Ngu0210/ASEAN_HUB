from flask import Blueprint, jsonify, abort, g
from main import db
from models.Main_Menu import Main_Menu
from schemas.Main_MenuSchema import main_menu_schema, main_menus_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_service import verify_user
from sqlalchemy.orm import joinedload

main_menu = Blueprint("main_menu", __name__, url_prefix="/menu/main")

@main_menu.route("/", methods=[ "GET"])
def main_menu_index():
    main_menu = Main_Menu.query.all()
    serialized_data = main_menus_schema(main_menu)
    return jsonify(serialized_data)

@main_menu.route("/", methods=["POST"])
def main_menu_create():
    #Creates new dish in menu
    main_menu_fields = main_menu_schema.load(request.json)

    main_menu = Main_Menu()
    main_menu.title = main_menu_fields["title"]
    main_menu.price = main_menu_fields["price"]
    main_menu.vegetarian = main_menu_fields["vegetarian"]

    db.session.commit()

    return jsonify(main_menu_schema.dump(main_menu))

@main_menu.route("/<int:id>", methods=["GET"])
def main_menu_show(id):
    #Returns specific dish
    main_menu = Main_Menu.query.get(id)
    return jsonify(main_menu_schema.dump(main_menu))

@main_menu.route("/<int:id>", methods=["PUT", "PATCH"])
# @jwt_required
def main_menu_update(id):
    #Updates specific dish
    main_menu_fields = main_menu_schema.load(request.json)

    main_menu = Main_Menu.query.filter_by(id=id)

    main_menu.update(menu_fields)
    db.session.commit()

    return jsonify(main_menu_schema.dump(main_menu[0]))

@main_menu.route("/<int:id>", methods=["DELETE"])
# @jwt_required
def main_menu_delete(id):
    #Deletes specific dish

    main_menu = Menu.query.filter_by(id=id).first()

    if not main_menu:
        return abort(400)

    db.session.delete(main_menu)
    db.session.commit()

    return jsonify(main_menu_schema.dump(main_menu))