from flask import Flask, request, jsonify, abort
app = Flask(__name__)
import psycopg2

connection = psycopg2.connect(
    database="asean_hub",
    user="app",
    password="4124",
    host="localhost"
)

cursor = connection.cursor()

cursor.execute("create table if not exists menu (id serial PRIMARY KEY, title varchar, price numeric);")
connection.commit()

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
    sql = "insert into menu (title) values (%s);"
    cursor.execute(sql, (request.json["title"],))
    connection.commit()
    
    sql = "select * from menu order by ID DESC limit 1;"
    cursor.execute(sql)
    menu = cursor.fetchone()
    return jsonify(menu)

@app.route("/menu/<int:id>", methods=["GET"])
def menu_show(id):
    sql = "select * from books where id = %s;"
    cursor.execute(sql, (id,))
    menu = cursor.fetchone()
    return jsonify(menu)

@app.route("/menu/<int:id>", methods=["PUT", "PATCH"])
def menu_update(id):
    sql = "update menu set title = %s where id = %s;"
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


 