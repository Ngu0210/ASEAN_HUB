from flask import Blueprint, jsonify
from models.Main_Menu import Main_Menu
from schemas.Main_MenuSchema import main_menu_schema, main_menus_schema

main_menu = Blueprint("main_menu", __name__, url_prefix="/menu/main")

@main_menu.route("/", methods=[ "GET"])
def main_menu_index():
    main_menu = Main_Menu.query.all()
    serialized_data = main_menus_schema(main_menu)
    return jsonify(serialized_data)
