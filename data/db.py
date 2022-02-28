import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO inventory (item_count, title, description) VALUES (?, ?, ?)",
            (2, 'RAM', 'RAM Stick 8GB.')
            )

cur.execute("INSERT INTO inventory (item_count, title, description) VALUES (?, ?, ?)",
            (10, 'ASUS Computer', 'Asus computer laptop XP.')
            )

connection.commit()
connection.close()