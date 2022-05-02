import json

fichier = "settings.json"

with open(fichier, "r") as f:
    settings = json.load(f)

print(settings.get("name"))

settings["name"] = "zeubi"

with open(fichier, "w") as f:
    json.dump(settings, f, indent=4)
