from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, jsonify, abort
app = Flask(__name__)
from database import cursor, connection

@app.route("/")
def home_page():
    return "The index page"

@app.route("/menu", methods=["GET"])
def menu_index():
    sql = "select * from menu"
    cursor.execute(sql)
    menu = cursor.fetchall()
    return jsonify(menu)

@app.route("/menu", methods=["POST"])
def menu_create():
    sql = "insert into menu (title, price, vegetarian) values (%s, %s, %s)"
    cursor.execute(sql, (request.json["title"], request.json["price"], request.json["vegetarian"]))
    connection.commit()
    
    sql = "select * from menu order by ID DESC limit 1;"
    cursor.execute(sql)
    menu = cursor.fetchone()
    return jsonify(menu)

@app.route("/menu/<int:id>", methods=["GET"])
def menu_show(id):
    sql = "select * from menu where id = %s;"
    cursor.execute(sql, (id,))
    menu = cursor.fetchone()
    return jsonify(menu)

@app.route("/menu/<int:id>", methods=["PUT", "PATCH"])
def menu_update(id):
    sql = "update menu set title = %s, price = %s, vegetarian = %s where id = %s;"
    cursor.execute(sql, (request.json["title"], request.json["price"], request.json["vegetarian"], id))
    connection.commit()

    sql = "SELECT * FROM menu WHERE id = %s"
    cursor.execute(sql, (id,))
    menu = cursor.fetchone()
    return jsonify(menu)

@app.route("/menu/<int:id>", methods=["DELETE"])
def menu_delete(id):
    sql = "select * from menu where id = %s;"
    cursor.execute(sql, (id,))
    menu = cursor.fetchone()

    if menu:
        sql = "delete from menu where id = %s;"
        cursor.execute(sql, (id,))
        connection.commit()

    return jsonify(menu)    


 