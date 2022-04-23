## [Sommaire](README.md)

# L'orienté objet

## Structure Class

```python
# class
class Voiture:
    # attribut de classe
    pneus = 4
    # méhode
    def __init__(self, marque: str):
        # attribut d'instance
        self.marque = marque

# instance
lamborghini = Voiture("Lamborghini")
```

### Dataclasse

```python
from dataclasses import dataclass
from typing import ClassVar

@dataclass
class User:
    first_name: str = ""
    last_name: Optional[datetime]
    c: ClassVar[int]

    def __post_init_(self):
        self.full_name = f"{self.first_name} {self.last_name}"
```
