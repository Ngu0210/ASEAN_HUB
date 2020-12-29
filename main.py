from dotenv import load_dotenv
load_dotenv()

from flask import Flask
app = Flask(__name__)

from controllers import registerable_controllers
for controller in registerable_controllers:
    app.register_blueprint(controller)
    

@app.route("/")
def home_page():
    return "The index page"

