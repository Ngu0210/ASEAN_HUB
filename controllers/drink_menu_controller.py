from flask import Blueprint, jsonify
from models.Drink_Menu import Drink_Menu
from schemas.Drink_MenuSchema import drink_menu_schema, drink_menus_schema

drink_menu = Blueprint("drink_menu", __name__, url_prefix="/menu/drink")

@drink_menu.route("/", methods=[ "GET"])
def drink_menu_index():
    drink_menu = Drink_Menu.query.all()
    serialized_data = drink_menus_schema(drink_menu)
    return jsonify(serialized_data)
