from main import db
from flask import Blueprint

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables Created")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables deleted")

@db_commands.cli.command("seed")
def seed_db():
    from models.Menu import Menu
    from faker import Faker
    faker = Faker()

    for i in range(10):
        menu = Menu()
        menu.title = faker.color_name()
        menu.price = faker.random_number(digits=2)
        menu.vegetarian = faker.boolean(chance_of_getting_true=50)
        db.session.add(menu)
        print(f"{i} book record(s) created")

    db.session.commit()
    print("Tables seeded")
