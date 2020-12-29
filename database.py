import psycopg2

connection = psycopg2.connect(
    database="asean_hub",
    user="app",
    password="4124",
    host="localhost"
)

cursor = connection.cursor()

cursor.execute("create table if not exists menu (id serial PRIMARY KEY, title varchar, price integer, vegetarian boolean);")
connection.commit()