#loading enviroment variables
from dotenv import load_dotenv
load_dotenv()

#Flask application creation
from flask import Flask, jsonify
app = Flask(__name__)
app.config.from_object("default_settings.app_config")

#Database connection
from database import init_db
db = init_db(app)

#Setup Serialization & Deserialization
from flask_marshmallow import Marshmallow
ma = Marshmallow(app)

from commands import db_commands
app.register_blueprint(db_commands)


#Controller Registration
from controllers import registerable_controllers
for controller in registerable_controllers:
    app.register_blueprint(controller)

from marshmallow.exceptions import ValidationError

@app.errorhandler(ValidationError)
def handle_bad_request(error):
    return (jsonify(error.messages), 400)
    
#Index page end point
@app.route("/")
def home_page():
    return "The index page"

