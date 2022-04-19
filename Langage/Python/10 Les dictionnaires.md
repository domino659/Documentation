## [Sommaire](README.md)

# Les dictionnaires

Les dictionnaires sont des **collections d'objets non-ordonnées**.

Un dictionnaire est composé d'éléments et chaque élément se compose d'une paire _clé: valeur_.

Dans d'autres langages de programmation, on parle de tableaux associatifs ou de hashs.

Comme les listes, les dictionnaires sont des objets **muables** et **dynamiques**. Ils peuvent être modifiés et s'étendre selon vos besoins.

Un dictionnaire peut **contenir des objets de n'importe quel type** et même **inclure d'autres dictionnaires**.

C'est grâce à ces caractéristiques que les dictionnaires sont souvent utilisés pour **créer des structures de données complexes** où plusieurs éléments sont imbriqués les uns dans les autres !

<br>

## Créer un dictionnaire

La façon la plus simple de créer un dictionnaire est d'ouvrir des accolades **{}** et d'y insérer des paires de **clés** et de **valeurs**.

Pour écrire une paire, il faut respecter la syntaxe suivante: **clé: valeur**.

Chaque paire doit être séparée de l'autre par une virgule.

Les valeurs peuvent être de n'importe quel type alors que les clés doivent obligatoirement être de **type immuable **!

Vous pouvez ainsi utiliser un **float** ou un **tuple** comme clé sans problème:

```python
# En théorie
d = {
    clé: valeur,
    clé: valeur,
    clé: valeur,
    ...
    clé: valeur
}

# Dictionnaire vide
d = {}

print(d)

# Dictionnaire dont les clés ne sont que des chaînes de caractères
d = {
    'spam': 'eggs',
    'knights': 'lumberjack',
    'bacon': 'sausage'
}

print(d)

# Dictionnaire dont les clés sont des objets de différents types
d = {
    1: 'one',
    'deux': 2,
    (3, 4, 5): 'pas_de_soucis',
    9.9: 'nine_point_nine'
}
print(d)
```

Les dictionnaires que je viens de créer n'ont aucun sens, je voulais juste te montrer ce qu'il était possible de faire.

Vous pouvez aussi créer un dictionnaire grâce la fonction **dict**:

```python
d = dict()  # {}
d = dict({
    'spam': 'eggs',
    'knights': 'lumberjack',
    'bacon': 'sausage'
})

print(d)
```

Une clé doit être **unique**, les doublons ne sont pas autorisés.

Si cela arrive, cela ne va pas créer d'erreur mais votre seconde clé écrasera la première.

```python
d = {
    'spam': 'eggs',
    'knights': 'lumberjack',  # 1ère clé 'knights'
    'bacon': 'sausage',
    'knights': 'ham'  # 2ème clé 'knights' qui va écraser la première
}

print(d)
```

Une clé ne peut pas être un objet muable:

```python
d = {
    ['spam']: 'eggs'  # TypeError: unhashable type: 'list'
}
```

<br>

## Accéder à un élément dans un dictionnaire

Alors qu'on accède aux éléments contenus dans une liste ou un tuple grâce à leurs indices (car ce sont des structures ordonnés), pour les dictionnaires, **on utilise une clé**.

On peut utiliser cette clé à l'intérieur de crochets **[]** ou via la méthode **get**.

La différence entre les deux ? Avec les crochets, une erreur de type **KeyError** est levée si vous tentez d'utiliser une clé inexistante. Alors que la méthode **get** vous retournera simplement **None** ou un objet de votre choix.

```python
d = {
    'spam': 'eggs',
    'knights': 'lumberjack',
    'bacon': 'sausage'
}
d['spam']  # 'eggs'

# Si on essaie d'accéder à une clé inexistante avec les crochets, on a une erreur (KeyError)
# print(d['ham'])

d.get('spam')  # 'eggs'

# Avec get, si la clé n'existe pas, on récupère None
d.get('ham')  # None

# Ou la valeur par défaut que l'on passe en deuxième argument
d.get('ham', "Cette clé n'existe pas...")  # "Cette clé n'existe pas..."
```

<br>

## Ajouter et modifier des éléments

Les dictionnaires étant des objets muables, ils sont faciles à modifier:

```python
d = {
    'spam': 'eggs',
    'knights': 'lumberjack',
}

d['spam'] = 'ham' # Clé existe déjà, remplace la valeur
d['bacon'] = 'sausage' # Nouvelle clé, on créer la paire clé/valeur dans le dico

print(d)
```

Cela signifie que vous pouvez aussi créer des dictionnaires à la volée et y ajouter/supprimer des éléments en fonction de ce qu'il se passe dans votre code 👍

<br>

## Supprimer des items d'un dictionnaire

Pour les suppressions, plusieurs possibilités en fonction de votre besoin:

👉 Utiliser la méthode **pop** pour supprimer un item et récupérer sa valeur dans une variable:

```python
d = {
    'spam': 'ham',
    'knights': 'lumberjack',
    'bacon': 'sausage'
}

item = d.pop('knights') # 'lumberjack'
```

👉 Utiliser la méthode **popitem** pour supprimer un item **aléatoirement** et récupérer un tuple contenant une clé et sa valeur:

```python
d = {
    'spam': 'ham',
    'knights': 'lumberjack',
    'bacon': 'sausage'
}

item = d.popitem() # ('bacon', 'sausage') OU ('spam', 'ham') OU ('knights': 'lumberjack')
```

👉 Utiliser **clear** pour vider le dictionnaire:

```python
d = {
    'spam': 'ham',
    'knights': 'lumberjack',
    'bacon': 'sausage'
}

d.clear() # {}
```

👉 Supprimer entièrement le dictionnaire grâce à l'instruction **del**:

```python
d = {
    'spam': 'ham',
    'knights': 'lumberjack',
    'bacon': 'sausage'
}

del d
print(d) # NameError: name 'd' is not defined
```

<br>

## Les defaultdict

Parfois, vous aurez besoin qu'un dictionnaire soit initialisé avec des valeurs par défaut.

Pour faire ça, vous pouvez utiliser les **defaultdict**.

Cela fonctionne exactement comme un dictionnaire à la différence qu'on doit lui passer une fonction en paramètre. Le résultat de cette fonction sera la valeur par défaut de toutes les clés du dictionnaire.

Cela signifie qu'avec un **defaultdict**, vous n'aurez jamais d'erreur de type **KeyError**.

```python
from collections import defaultdict

programming_languages = defaultdict(lambda: 'Python')

programming_languages['.js'] = 'JavaScript'
programming_languages['.php'] = 'PHP'

print(programming_languages['.js'])   # 'Javascript'
print(programming_languages['.php'])  # 'PHP'
print(programming_languages['.py'])   # 'Python' => Valeur par défaut
```

<br>

## Itérer sur un dictionnaire

Comme les dictionnaires sont des collections d'objets, vous pouvez itérer dessus pour récupérer et modifier des valeurs.

Python nous donne plusieurs outils pour faire ça que je vous présente tout de suite:

👉 **Avec une boucle for**

La boucle for classique que vous connaissez ! Il faut savoir que sur un dictionnaire, une boucle for va itérer sur les **clés uniquement**:

```pyhton
d = {
    'spam': 'ham',
    'knights': 'lumberjack',
    'bacon': 'sausage'
}

for key in d:
    print(key)
```

On pourrait utiliser la clé pour récupérer la valeur de cette façon:

```python
d = {
    'spam': 'ham',
    'knights': 'lumberjack',
    'bacon': 'sausage'
}

for key in d:
    print(key, d[key])
```

👉 Avec **keys**, **values** et **items**

Pour itérer sur les clés, vous pouvez aussi utiliser la méthode **keys**.

Cela revient au même résultat que ce qu'on a vu avec la boucle for à la différence que vous pouvez aussi l'utiliser en dehors d'une boucle:

```python
d = {
    'spam': 'ham',
    'knights': 'lumberjack',
    'bacon': 'sausage'
}

for key in d.keys():

    print(key)
keys = d.keys()
print(keys)
```

Pour itérer sur les valeurs, Python met à notre disposition la méthode **values**:

```python
d = {
    'spam': 'ham',
    'knights': 'lumberjack',
    'bacon': 'sausage'
}

for value in d.values():
    print(value)
```

Vous pouvez combiner les deux résultats précédents grâce à la méthode **items** qui permet de récupérer toutes les paires clés / valeurs:

```python
d = {
    'spam': 'ham',
    'knights': 'lumberjack',
    'bacon': 'sausage'
}

for key, value in d.items():
    print(key, value)
```

<br>

## Compréhension de dictionnaire

Comme pour les listes, il est aussi possible de passer par une compréhension de dictionnaire :

```python
d = {
    'spam': 'ham',
    'knights': 'lumberjack',
    'bacon': 'sausage'
}

d_with_s = {k:v + 's' for k, v in d.items()}  # Ajoute un 's' à toutes les valeurs
print(d_with_s)
```

<br>

## Vérifier la présence d'une clé dans un dictionnaire

Vous pouvez vérifier qu'une clé est présente dans un dictionnaire grâce à l'opérateur in:

```python
d = {
    'spam': 'ham',
    'knights': 'lumberjack',
    'bacon': 'sausage'
}
print('bacon' in d)  # True
print('ham' in d)    # False
```
