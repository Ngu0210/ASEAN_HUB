from main import db

class Drink_Menu(db.Model):
    __tablename__ = "drink_menu"

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(),)
    price = db.Column(db.Integer(),)
    ice = db.Column(db.Boolean(),)

    def __repr__(self):
        return f"<drink {self.title}>"