from main import db
import enum

class Portion(enum.Enum):
    small = 1
    medium = 2
    large = 3



class Menu(db.Model):
    __tablename__ = "menu"

    portion_status = db.Enum(Portion, name='portion_status_enum')

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())
    price = db.Column(db.Integer())
    vegetarian = db.Column(db.Boolean())
    portion = db.Column(portion_status)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"