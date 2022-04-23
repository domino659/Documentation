from pathlib import Path

PATH = Path('H:/Mon Drive/Code/Formation/Python/Project/prenoms.txt')
NEW_PATH = Path('H:/Mon Drive/Code/Formation/Python/Project/prenoms_final.txt')

prenoms = []

with open(PATH) as f:
    lines = f.read().splitlines()

for line in lines:
    prenoms.extend(line.split())

prenoms_final = [prenom.strip(",. ") for prenom in prenoms]

with open(NEW_PATH, "w") as f:
    f.write("\n".join(sorted(prenoms_final)))