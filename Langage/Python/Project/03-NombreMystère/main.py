import random

MYSTERY_NUMBER = random.randint(0, 100)
remaining_attempts = 5

print("--- Le jeu du nombre mystère ---")
while remaining_attempts > 0:
    print(f"Il te reste {remaining_attempts} essai{'s' if remaining_attempts > 1 else ''}.")

    user_choice = input("Devine le nombre: ")
    if not user_choice.isdigit():
        print("Veuillez entrer un nombre valide.\n")
        continue

    user_choice = int(user_choice)

    if user_choice > MYSTERY_NUMBER:
        print(f"Le nombre mystère est plus petit que {user_choice}.")
    elif user_choice < MYSTERY_NUMBER:
        print(f"Le nombre mystère est plus grand que {user_choice}.")
    elif user_choice == MYSTERY_NUMBER:
        break

    remaining_attempts -= 1

if remaining_attempts == 0:
    print(f"Dommage ! Le nombre mystère était {MYSTERY_NUMBER}.")
else:
    print(f"Bravo ! Le nombre mystère était {MYSTERY_NUMBER}.")
    print(f"Tu as trouvé le nombez en {6 -remaining_attempts} essai.")

print("Fin du jeu..")