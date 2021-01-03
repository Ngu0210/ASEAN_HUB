from models.Menu import Menu
from models.User import User
from main import db
from flask import Blueprint, request, jsonify, abort, g
from schemas.MenuSchema import menu_schema, menus_schema

menu = Blueprint("menu", __name__, url_prefix="/menu")

@menu.route("/", methods=["GET"])
def menu_index():
    #Returns the menu
    menu = Menu.query.all()
    serialised_data = menus_schema.dump(menu)
    return(jsonify(serialised_data))