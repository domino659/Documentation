## [Sommaire](README.md)

# Les annotations de type

Les annotations de type sont une nouveauté de la version 3.5 de Python.

Ces annotations nous permettent de spécifier le type des paramètres d'une fonction, ou encore le type d'une variable.

Cela a beaucoup d'avantages, notamment celui de documenter notre code et de le rendre plus explicite.

Les annotations de type sont facultatives, on peut très bien s'en passer.

<br>

Python est un langage dynamique et fortement typé, le type des objets peut changer à tout moment.

Les annotations de type permet d'éviter les erreurs liées au type des objets. Et de renforcer la résilience du code.

Les annotation peuvent être du type:

- int
- float
- str
- bool
- array[int]
- list[str]

```python
a: int = 5
b: int | str = "5"

def add(a: int = 3, b: int = 4) -> int:
    return a + b

add()
```
