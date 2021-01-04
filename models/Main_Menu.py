from main import db
# from models.Menu import Menu

class Main_Menu(db.Model):
    __tablename__ = "main_menu"

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    vegetarian = db.Column(db.Boolean())

    # menu = db.relationship("Menu", backref="menu-main_menu")

    def __repr__(self):
        return f"<Menu {self.title}>"
    