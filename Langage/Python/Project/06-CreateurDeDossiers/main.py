from pathlib import Path

DIR = Path('D:/User/Downloads')

STRUCTURE = {
    "Films":
        [
        "Le seigneur des anneaux",
        "Harry Potter",
        "Moon",
        "Forrest Gump"
        ],
     "Employes":
        [
        "Paul",
        "Pierre",
        "Marie"
        ],
     "Exercices":
        [
        "les_variables",
        "les_fichiers",
        "les_boucles"
        ]
    }


for dossier_principal, sous_dossiers in STRUCTURE.items():
    for dossier in sous_dossiers:
        chemin_dossier = Path(DIR) / dossier_principal / dossier
        chemin_dossier.mkdir(exist_ok=True, parents=True)