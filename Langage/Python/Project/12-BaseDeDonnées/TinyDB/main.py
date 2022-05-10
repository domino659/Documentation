from tinydb import TinyDB, Query, where

db = TinyDB('data.json', indent=4)

# db.insert({"name": "Domino", "statue": True})
# db.insert_multiple([
#     {"name": "John", "statue": True},
#     {"name": "Paul", "statue": False}
# ])

User = Query()
finder = db.search(User.name == "Domino")
print(finder)

finder_unique = db.get(User.name == "Domino")
print(finder_unique)

is_true = db.search(where("statue") == True)
print(is_true)

print(len(db))
print(db.contains(User.name == "Domino"))

db.update({"statue": False}, where("name") == "Domino")
db.update({"roles": ["Junior"]})

db.upsert({"name": "Philippe", "statue": True, "roles": ["Senior"]}, where("name") == "Philippe")

db.remove(where("statue") == False)

# db.truncate()

users = db.table("Users")
roles = db.table("Roles")
roles.insert({"zeubi": "zeubi"})