#loading enviroment variables
from dotenv import load_dotenv
load_dotenv()

#Flask application creation
from flask import Flask
app = Flask(__name__)

#Database connection
from database import init_db
db = init_db(app)

#Controller Registration
from controllers import registerable_controllers
for controller in registerable_controllers:
    app.register_blueprint(controller)
    
#Index page end point
@app.route("/")
def home_page():
    return "The index page"

