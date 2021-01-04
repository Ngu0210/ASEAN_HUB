from models.Main_Menu import Main_Menu
# from models.User import User
from main import db
from flask import Blueprint, jsonify, abort, g, request, render_template
from schemas.Main_MenuSchema import main_menu_schema, main_menus_schema

menu = Blueprint("menu", __name__, url_prefix="/menu")

@menu.route("/", methods=["GET"])
def menu_index():
    #Returns the menu
    main = Main_Menu.query.all()
    serialised_data = main_menus_schema.dump(main)
    return(jsonify(serialised_data))

@menu.route("/main/", methods=["POST"])
def main_menu_create():
    #Creates new main in menu
    main_menu_fields = main_menu_schema.load(request.json)

    main_menu = Main_Menu()
    print("hello")
    main_menu.title = main_menu_fields["title"]
    main_menu.price = main_menu_fields["price"]
    main_menu.vegetarian = main_menu_fields["vegetarian"]

    db.session.add(main_menu)
    db.session.commit()

    return jsonify(main_menu_schema.dump(main_menu))