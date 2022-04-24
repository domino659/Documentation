## [Sommaire](README.md)

# L'orienté objet

## Structure Class

```python
from typing import Optional
class User:
    # attribut de classe
    user_crees = 0
    # méhode
    def __init__(self, first_name: str, last_name: Optional[int]):
        # attribut d'instance
        User.user_crees += 1
        self.first_name = first_name
        self.last_name = last_name

        def __str__(self):
        return f"Je m'apelle {self.first_name} {self.last_name}."

    @staticmethod
    def afficher_nombre_users():
        print(f"Vous avez {User.user_crees} user dans votre maison.")

# instance
print(User("bob", None))
User.afficher_nombre_users()

```

### Dataclasse

```python
from dataclasses import dataclass
from typing import ClassVar, Optional

@dataclass
class User:
    user_crees: ClassVar[int] = 0
    last_name: Optional[int]
    first_name: str = "Bob"

    def __post_init__(self):
        User.user_crees += 1
        self.full_name = f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"Je m'apelle {self.full_name}."
        
    @classmethod
    def moi(cls):
        return cls(first_name="Martin", last_name=45)

    @staticmethod
    def afficher_nombre_users():
        print(f"Vous avez {User.user_crees} user dans votre maison.")

moi = User.moi()
print(User(None, "bob"))
User.afficher_nombre_users()
```

### Heritage

```python
from dataclasses import dataclass

projets = ["pr_GOT", "HP", "LOTR"]

@dataclass
class Utilisateur:
    nom: str = "John"
    prenom: str = "Doe"

    def __str__(self):
        return f"Utilistateur: {self.nom} {self.prenom}"
        
    def afficher_projets(self):
        for projet in projets:
            print(projet)

    def hello_world(self):
        print("Hello World")


class Junior(Utilisateur):
    def __str__(self):
        return f"Junior: {self.nom} {self.prenom}"

    def afficher_projets(self):
        for projet in projets:
            if not projet.startswith("pr_"):
                print(projet)

    def hello(self):
        super().hello_world()

domino659 = Utilisateur("Domino", "659")
domino = Junior("Domino", "Lapin")
print(domino659)
domino659.afficher_projets()
print(domino)
domino.afficher_projets()
domino.hello()
```

```python
class Vehicule:
    def avance(self):
        print("Le véhicule démarre")

class Voiture(Vehicule):
    def avance(self):
        super().avance()
        print("La voiture roule")
    
class Avion(Vehicule):
    def avance(self):
        super().avance()
        print("L'avion vol")

v = Voiture()
a = Avion()
v.avance()
a.avance()
```