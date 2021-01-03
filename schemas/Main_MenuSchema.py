from main import ma
from models.Main_Menu import Main_Menu

class Main_MenuSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Main_Menu

main_menu_schema = Main_MenuSchema()
main_menus_schema = Main_MenuSchema(many=True)