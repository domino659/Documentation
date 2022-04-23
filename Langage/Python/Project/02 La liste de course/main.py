import sys, os, json

ACTIONS = ["Ajouter", "Retirer", "Afficher", "Vider", "Quitter"]
MENU_CHOICES = ["1", "2", "3", "4", "5"]

CUR_DIR = os.path.dirname(__file__)
LISTE_PATH = os.path.join(CUR_DIR, "liste.json")

if os.path.exists(LISTE_PATH):
    with open(LISTE_PATH, "r") as current_file:
        LISTE = json.load(current_file)
else:
    LISTE = []

while True:
    user_answer = ""
    while user_answer not in MENU_CHOICES:
        print("Choississez parmi les 5 options suivantes:")
        for i, action in enumerate(ACTIONS, 1):
            print(f"{i}. {action}")
        user_answer = input(" > ")
        if user_answer not in MENU_CHOICES:
            print("Veuillez choisir une option valide...\n")
            continue

    if user_answer == "1":
        print("Entrez le nom d'un élément à ajouter a la liste de courses:")
        user_add = input(" > ")
        LISTE.append(user_add)
        print(f"L'élément {LISTE[-1]} a bien été ajouté a la liste.\n")

    elif user_answer == "2":
        print("Entrez l'index d'un élément à retirer a la liste de courses:")
        user_remove = input(" > ")

        if user_remove.isdigit():
            if int(user_remove) > 0 and int(user_remove) <= len(LISTE):
                deleted_item = LISTE.pop(int(user_remove) -1)
                print(f"L'élément {deleted_item} a bien été retirer a la liste.\n")
            else:
                print("Cet index n'existe pas.\n")
        else:
            print("Veuillez rentrer un index valide.\n")

    elif user_answer == "3":
        if LISTE:
            print("Voici le contenu de votre liste:")
            for i, item in enumerate(LISTE, 1):
                    print(f"{i}. {item}")
        else:
            print("Votre liste ne contient aucun élément.\n")

    elif user_answer == "4":
        LISTE.clear()
        print("La liste a été vidé.\n")

    elif user_answer == "5":
        with open(LISTE_PATH, "w") as current_file:
            json.dump(LISTE, current_file, indent=2)
        print("A bientôt")
        sys.exit()

    print("-" * 50)