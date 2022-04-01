first_number = second_number = ""

while not (first_number.isdigit() and second_number.isdigit()):
    first_number = input("Entrer un premier nombre: ")
    second_number = input("Entrer un deuxième nombre: ")

    if not (first_number.isdigit() and second_number.isdigit()):
        print("Veuillez entrer deux nombres valides")

result = int(first_number) + int(second_number)
print(f"Le resultat de l'addition de {first_number} avec {second_number} est égal à {result}")
