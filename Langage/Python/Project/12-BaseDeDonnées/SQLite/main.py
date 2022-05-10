import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users(
    prenom text,
    nom text UNIQUE,
    age int
)
""")

# d = {"prenom": "John", "nom": "Doe", "age": 00}
# c.execute("INSERT INTO users VALUES (:prenom, :nom, :age)", d)
# d = {"prenom": "Martin", "nom": "Sion", "age": 24}
# c.execute("INSERT INTO users VALUES (:prenom, :nom, :age)", d)
# d = {"prenom": "Pingu", "nom": "Pingoin", "age": 42}
# c.execute("INSERT INTO users VALUES (:prenom, :nom, :age)", d)
# d = {"prenom": "John", "nom": "Bob", "age": 99}
# c.execute("INSERT INTO users VALUES (:prenom, :nom, :age)", d)

d = {"prenom": "John"}
c.execute("SELECT * FROM users WHERE prenom=:prenom", d)
# c.execute("SELECT * FROM users WHERE prenom='Martin'")
data = c.fetchall()
print(data)

c.execute("SELECT * FROM users")
first_data = c.fetchone()
print(first_data)
second_data = c.fetchone()
print(second_data)
third_data = c.fetchone()
print(third_data)
fourth_data = c.fetchone()
print(fourth_data)

d = {"prenom": "John", "nom": "Bob", "age": 90}
c.execute("""UPDATE users SET age=:age
WHERE prenom=:prenom AND nom=:nom""", d)

c.execute("SELECT * FROM users WHERE prenom=:prenom AND nom=:nom", d)
data = c.fetchall()
print(data)

d = {"prenom": "John", "nom": "Doe"}
c.execute("DELETE FROM users WHERE prenom=:prenom AND nom=:nom", d)

c.execute("SELECT * FROM users")
data = c.fetchall()
print(data)

conn.commit()
conn.close()