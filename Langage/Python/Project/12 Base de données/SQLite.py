import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users(
    prenom text,
    nom text   
)
""")
conn.commit()
conn.close()