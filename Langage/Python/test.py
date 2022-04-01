chemin =r"G:\Mon Drive\Code\Formation\Python\test.json"
## Lire le contenu d'un fichier

# Standard Methode but need closing
access = open(chemin, "r")
access.close()


# Advanced methode don't need closing
with open(chemin, "r") as access:
    contenu = access.read().splitlines()
    print(contenu)

with open(chemin, "a") as access:
    contenu = access.write("\nBonjour")