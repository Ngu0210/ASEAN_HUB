from models.Menu import Menu
from main import db
from flask import Blueprint, request, jsonify, abort    
from schemas.MenuSchema import menu_schema, menus_schema
menu = Blueprint("menu", __name__, url_prefix="/menu")

@menu.route("/", methods=["GET"])
def menu_index():
    #Returns the menu
    menu = Menu.query.all()
    serialised_data = menus_schema.dump(menu)
    return(jsonify(serialised_data))

@menu.route("/", methods=["POST"])
def menu_create():
    #Creates new dish in menu
    menu_fields = menu_schema.load(request.json)

    new_menu = Menu()
    new_menu.title = menu_fields["title"]
    new_menu.price = menu_fields["price"]
    new_menu.vegetarian = menu_fields["vegetarian"]

    db.session.add(new_menu)
    db.session.commit()

    return jsonify(menu_schema.dump(new_menu))

@menu.route("/<int:id>", methods=["GET"])
def menu_show(id):
    #Returns specific dish
    menu = Menu.query.filter_by(id=id)
    return jsonify(menu_schema.dump(menu))

@menu.route("/<int:id>", methods=["PUT", "PATCH"])
def menu_update(id):
    #Updates specific dish
    menu = Menu.query.filter_by(id=id)
    menu_fields = menu_schema.load(request.json)
    menu.update(menu_fields)
    db.session.commit()

    return jsonify(menu_schema.dump(menu[0]))

@menu.route("/<int:id>", methods=["DELETE"])
def menu_delete(id):
    #Deletes specific dish
    menu = Menu.query.get(id)

    if not menu:
        return abort(404)

    db.session.delete(menu)
    db.session.commit()

    return jsonify(menu_schema.dump(menu))