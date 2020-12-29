from main import ma
from models.Menu import Menu

class MenuSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Menu

menu_schema = MenuSchema()
menus_schema = MenuSchema(many=True)