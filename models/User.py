from main import db

class  User(db.Model):
    __tablename__="users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)


    # menu = db.relationship("Menu", backref="user", lazy="dynamic")

    def __repr__(self):
        return f"<User {self.email}>"