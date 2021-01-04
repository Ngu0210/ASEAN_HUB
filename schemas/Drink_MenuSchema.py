from main import ma
from models.Drink_Menu import Drink_Menu

class Drink_MenuSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Drink_Menu

drink_menu_schema = Drink_MenuSchema()
drink_menus_schema = Drink_MenuSchema()