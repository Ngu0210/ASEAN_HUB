from flask_sqlalchemy import SQLAlchemy

def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://app:{4124}@localhost/asean_hub"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)
    return db

# import psycopg2

# connection = psycopg2.connect(
#     database="asean_hub",
#     user="app",
#     password="4124",
#     host="localhost"
# )

# cursor = connection.cursor()

# cursor.execute("create table if not exists menu (id serial PRIMARY KEY, title varchar, price integer, vegetarian boolean);")
# connection.commit()