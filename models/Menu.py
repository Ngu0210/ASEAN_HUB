# from main import db
# from enum import Enum

# class Portion(str, Enum):
#     small = 'small'
#     medium = 'medium'
#     large = 'large'

# class Menu(db.Model):
#     __tablename__ = "menu"

#     portion_status = db.Enum(Portion, name='portion_status_enum')

#     id = db.Column(db.Integer(), primary_key=True)
#     main_menu = db.Column(db.Integer, db.ForeignKey("main_menu.id"), nullable=False)
#     drink_menu = db.Column(db.Integer, db.ForeignKey("drink_menu.id"), nullable=False)
#     order = db.relationship("Order", backref="menu", lazy="dynamic")

#     def __repr__(self):
#         return f"<Menu {self.title}>"