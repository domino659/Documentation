import random
HUMAN_PV = 50
MAX_HUMAN_PV = HUMAN_PV
HUMAN_POTION = 3
MONSTER_PV = 50
SKIP_TURN = False

user_action = ""

print("--- Welcome to Poitier 2077 Reloaded ---")

while True:
    if SKIP_TURN:
        print("Vous passez votre tour...")
        SKIP_TURN = False
    else:
        user_action = ""
        while user_action not in ["1", "2"]:
            print("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
            user_action = input(" > ")
            if user_action not in ["1", "2"]:
                print("Veuillez choisir une option valide...\n")
                continue
        
        if user_action == "1":
            human_attack = random.randint(5, 10)
            MONSTER_PV -= human_attack
            print(f"Vous avez infligé {human_attack} points de dégats à l'ennemi 🗡") 
        elif user_action == "2" and HUMAN_POTION > 0:
            hp_healed = random.randint(15, 50)
            if hp_healed + HUMAN_PV > 50:
                hp_healed = MAX_HUMAN_PV - HUMAN_PV
            HUMAN_PV += hp_healed
            HUMAN_POTION -= 1
            SKIP_TURN = True
            print(f"Vous récupérez {hp_healed} points de vie ❤ ({HUMAN_POTION} 🍯 restantes)") 
        else:
            print("Vous n'avez plus de potions...")
            continue

    if MONSTER_PV <= 0:
        print("Tu as gagné 🎉")
        break

    monster_attack = random.randint(5, 15)
    HUMAN_PV -= monster_attack
    print(f"L'ennemi vous a infligé {monster_attack} points de vie.")

    if HUMAN_PV < 0: 
        print("Tu as perdu 😭")
        break

    print(f"Il vous reste {0 if HUMAN_PV <= 0 else HUMAN_PV} points de vie.")
    print(f"Il reste {0 if MONSTER_PV <= 0 else MONSTER_PV} points de vie à l'ennemi.")
    print("-" * 50)

print("Fin du jeu")