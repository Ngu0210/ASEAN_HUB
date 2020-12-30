from main import db

class Menu(db.Model):
    __tablename__ = "menu"

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())
    price = db.Column(db.Integer())
    vegetarian = db.Column(db.Boolean())