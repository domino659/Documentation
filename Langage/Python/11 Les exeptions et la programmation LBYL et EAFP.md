## [Sommaire](README.md)

# Les exeptions et la programmation LBYL et EAFP

## LBYL -> **L**ook **B**efore **Y**ou **L**eep

Dans ce cas, on regarde si la clé existe avant de la récupérer afin d'éviter une erreur.

```python
if "cle" in dict:
    print(dict["clé"])
```

<br>

## EAFP -> It's **E**asier to **A**sk for **F**orgiveness than **Permission**

Dans cet autre cas, on demande a python d'essayer de récupérer la valeur directement, si il recontre une erreur on lui demande de l'ignorer et de continuer le déroulement du programme.

```python
try
    print(dict["clé"])
except:
    pass
```

Il n'y a pas de bonne ou mauvaises facon de faire, cela dépend des situations.

**LBYL**
```python
liste = [2, 7, "texte", 4]
for i in liste:
    if not str(i).isdigit():
        liste.remove(i)
    total = sum(liste)
```

**EAFP**
```python
liste = [2, 7, "texte", 4]
try:
    total = sum(liste)
except:
    total = 0
```
