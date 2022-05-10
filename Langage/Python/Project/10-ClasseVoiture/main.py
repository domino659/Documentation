from dataclasses import dataclass
from typing import Optional

@dataclass
class Voiture:
    essence: int = 100

    def afficher_reservoir(self):
        return print(f"La voiture contient {self.essence}L d'essence.")

    def roule(self, km):
        if self.essence <= 0:
            print("Vous n'avez plus d'essence, faites le plein !")
            return
        
        self.essence -= (km*5)/100

        if self.essence < 10:
            print("Vous n'avez bientôt plus d'essence !")
        
        self.afficher_reservoir    

    def faire_le_plein(self):
        self.essence = 100
        return print("Vous pouvez repartir !")

msg = Voiture()

msg.roule(500000)
msg.afficher_reservoir()

msg.roule(500000)
