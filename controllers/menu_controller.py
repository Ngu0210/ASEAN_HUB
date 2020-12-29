from models.Menu import Menu
from main import db
from flask import Blueprint, request, jsonify
from schemas.MenuSchema import menu_schema, menus_schema
menu = Blueprint("menu", __name__, url_prefix="/menu")

@menu.route("/", methods=["GET"])
def menu_index():
    menu = Menu.query.all()
    serialised_data = menus_schema.dump(menu)
    return(jsonify(serialised_data))

@menu.route("/", methods=["POST"])
def menu_create():
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
    menu = Menu.query.filter_by(id=id)
    return jsonify(menu_schema.dump(menu))

# @menu.route("/<int:id>", methods=["PUT", "PATCH"])
# def menu_update(id):
#     sql = "update menu set title = %s, price = %s, vegetarian = %s where id = %s;"
#     cursor.execute(sql, (request.json["title"], request.json["price"], request.json["vegetarian"], id))
#     connection.commit()

#     sql = "SELECT * FROM menu WHERE id = %s"
#     cursor.execute(sql, (id,))
#     menu = cursor.fetchone()
#     return jsonify(menu)

# @menu.route("/<int:id>", methods=["DELETE"])
# def menu_delete(id):
#     sql = "select * from menu where id = %s;"
#     cursor.execute(sql, (id,))
#     menu = cursor.fetchone()

#     if menu:
#         sql = "delete from menu where id = %s;"
#         cursor.execute(sql, (id,))
#         connection.commit()

#     return jsonify(menu)    