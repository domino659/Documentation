## [Sommaire](README.md)

# 02 Le type des objets et la conversion

Python est un **language dynamique**, il n'est dont pas nécessaire de préciser les **types de variables** et il est possible de modifier le type d'une variable sans devoir en créer une autre contrairement a un **lanquage statique**.

Il est nécessaire dans certains cas d'empécher les erreurs liée a l'incompatibilité des objets en modifiant le type d'une variable.

Fonction permettant de changer le type des variables:

* int()

* str()

<br>

```python
>>> a = 5
>>> b = "10"
>>> b = int(b)
>>> print(a + b)
15

nombre = 15
resultat = "Le nombre est " + str(nombre)
```

### Afficher le type d'une fonction

```python
type()
```