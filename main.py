from flask import Flask
app = Flask(__name__)

@app.route("/")
def home_page():
    return "The index page"

@app.route("/menu", methods=["GET"])
def menu_index():
    pass

@app.route("/menu", methods=["POST"])
def menu_create():
    pass

@app.route("/menu/<int:id>", methods=["GET"])
def menu_show(id):
    pass

@app.route("/menu/<int:id>", methods=["PUT", "PATCH"])
def menu_update(id):
    pass

@app.route("/menu/<int:id>", methods=["DELETE"])
def menu_delete(id):
    pass


 