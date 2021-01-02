#loading enviroment variables
from dotenv import load_dotenv
load_dotenv()

#Flask application creation
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object("default_settings.app_config")

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)

    from commands import db_commands
    app.register_blueprint(db_commands)

    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)

    from marshmallow.exceptions import ValidationError

    @app.errorhandler(ValidationError)
    def handle_bad_request(error):
        return (jsonify(error.messages), 400)

    return app

