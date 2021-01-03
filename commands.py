from main import db
from flask import Blueprint

db_commands = Blueprint("db-custom", __name__)

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    db.engine.execute("drop table if exists alembic_version;")
    print("Tables deleted")

@db_commands.cli.command("seed")
def seed_db():
    from main import bcrypt
    from models.Menu import Menu
    from models.User import User
    from faker import Faker
    import random

    faker = Faker()
    users = []

    for i in range(5):
        user = User()
        user.email = faker.email()
        user.password = bcrypt.generate_password_hash("123456").decode("utf-8")
        db.session.add(user)
        users.append(user)
        print(f"{i} users created")

    db.session.commit()

    for i in range(10):
        menu = Menu()
        menu.title = faker.color_name()
        menu.price = faker.random_number(digits=2)
        menu.vegetarian = faker.boolean(chance_of_getting_true=50)
        menu.portion = random.choice(menu.portion_status.enums)

        db.session.add(menu)
        print(f"{i} book record(s) created")

    db.session.commit()

    print("Tables seeded")
