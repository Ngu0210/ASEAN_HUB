from dotenv import load_dotenv
load_dotenv()

from flask import Flask
app = Flask(__name__)

from menu import menu
app.register_blueprint(menu)

@app.route("/")
def home_page():
    return "The index page"

