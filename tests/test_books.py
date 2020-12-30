import unittest
from main import create_app

class TestMenu(unittest.TestCase):
    def test_menu_index(self):
        app = create_app()
        client = app.test_client()

        response = client.get("/menu/")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)