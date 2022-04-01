## [Sommaire](README.md)

# Les boucles

## La boucle **for**

Avec Python, on utilise la boucle **for** pour parcourir des objets itérables comme les listes, les tuples ou encore les chaînes de caractères.

C'est une boucle commune à presque tous les langages de programmation.

<br>

### Syntaxe de la boucle **for**

Une boucle for s'écrit de la manière suivante:

```python
for value in object:
    code
    ....
```

La variable **value** prend la valeur de chaque élément contenu dans **object** à chaque itération.

La boucle **for** continue jusqu'à ce qu'on ait atteint le dernier élément de **object**.

En pratique, cela donne:

```python
fruits = ['🍊', '🍋', '🍏', '🍒', '🥭']

for fruit in fruits:
    print(fruit)
```

```python
for i in range(10):
    print("pingu")
```


<br>

### **for ... else**

Comme pour les structures conditionnelles if..else, vous pouvez définir un comportement par défaut pour votre boucle for grâce au mot-clé else.

C'est optionnel mais cela vous permet d'exécuter du code lorsque la boucle for est terminée:

```python
fruits = ['🍊', '🍋', '🍏', '🍒', '🥭']

for fruit in fruits:
    print(fruit)
else:
    print('Plus de fruits dans le panier')
```

Avec **break** on peux donc empécher l'éxecution du **else** si la condition est verifié.

```python
fruits = ['🍊', '🍋', '🍏', '🍒', '🥭']

for fruit in fruits:
    print(fruit)
    if fruit == '🍒':
        print("On s'arrête a la cerise.")
        break

else:
    print('Plus de fruits dans le panier')
```

<br>

## La boucle **while**

La boucle **while** est utilisée pour exécuter du code tant qu'une certaine condition est vérifiée.

Cette boucle est très utile lorsqu'on ne sait pas combien de fois nous devons itérer.

### Syntaxe de la boucle **while**

Une boucle **while** s'écrit de cette manière:

```python
while condition:
    code
    ....
```

Lorsque votre script rencontre une boucle **while**, il vérifie que la **condition** renvoie **True**.

Tant que cette condition retourne **True**, il exécute le code contenu à l'intérieur de la boucle sans interruption !

À chaque itération, il vérifie la condition et ne sort de la boucle que si elle renvoie **False**.

Par exemple:

```python
i = 0
while i < 10:
    print('Salut')
    i += 1
```

☝️ Ici, tant que **i** est inférieur à **10**, on affiche **'Salut'**.

Il faut noter **deux choses très importantes**:

1. On déclare la variable qui nous sert de condition **avant** la boucle **while**

    ⇒ On assigne la valeur **O** à la variable **i** juste avant d'entrer dans la boucle.

2. On met à jour notre condition à chaque nouvelle itération

    ⇒ On incrémente **i** à la fin de ma boucle

Ce faisant, on évite de rentrer dans une **boucle infinie**.

Eh oui, d'après vous, que se passe-t-il si je n'incrémente pas i à la fin de la boucle ?

Mon script part en **boucle infinie** et mon programme ne se terminera jamais à moins que je l'arrête manuellement !

<br>

### **while...else**

Tout comme pour les boucles for, il est possible de définir un comportement par défaut grâce au mot-clé else.

Le code à l'intérieur du else sera exécuté si la condition de votre boucle while renvoie False.

```python
i = 0
while i < 3:
    print('Salut')
    i += 1
else:
    print('Au revoir')
```

☝️ Ici on affiche **'Salut'** tant que **i < 3** (**'Salut'** sera donc affiché 3 fois).

À la 4e itération, **i** est supérieur à **3**, on passe donc dans le **else** et on affiche **'Au revoir'**.

<br>

## L'instruction **continue**

L'instruction continue** permet d'ignorer des valeurs lors de l'itération en cours sans pour autant arrêter l'exécution.

```python
fruits = ['🍊', '🍋', '🍏', '🍒', '🥭']

for fruit in fruits:
    if fruit == '🍒':
        print('Pas fan des cerises')
        continue

    print(fruit)


print('On passe à la suite')
```

☝️Dans le script ci-dessus, on souhaite éviter de faire un **print** sur les cerises.

Lorsque que **fruit == '🍒'**, j'affiche un message et **continue** ignore le reste du code dans l'itération en cours.

Tout le code dans la boucle après l'instruction **continue** est donc ignoré (dans ce cas-ci, le **print**).

Le **print(fruit)** n'est donc pas exécuté, l'interpréteur Python revenant au niveau de la boucle **for** pour passer à la prochaine itération.

Il est important de noter que l'instruction **continue n'arrête pas** la boucle au complet (comme le ferait l'instruction **break**), elle permet juste d'ignorer le reste du code dans l'itération courante.

<br>

## L'instruction **break**

L'instruction **break** permet d'interrompre l'exécution d'une boucle et de passer à la partie suivante du script.

```python
fruits = ['🍊', '🍋', '🍏', '🍒', '🥭']
fruits_manges = 0

for fruit in fruits:
    print("Je mange des " + fruit)
    fruits_manges += 1
    if fruits_manges == 3:
        break

print("Je n'ai plus faim !")
```

Dans ce code, on itère sur une liste de fruits.

Au bout de 3 fruits mangés, on interrompt l'exécution de la boucle grâce à l'instruction **break**.

De cette manière, je ne m'occupe pas des fruits restants et je passe à la suite de mon code.

Dans le cas d'un bloc d'instruction à l'intérieur d'un bloc d'instruction, l'instruction break ne sortira que du bloc d'instruction dans lequel elle est contenue:

```python
for a in range(5):
    for b in range(5):
        print("a:", a, "b: ", b)
        if b == 3:
            break
```

☝️Dans le code ci-dessus, l'instruction **break** nous permet d'arrêter l'exécution de la deuxième boucle for.

Le nombre 4 n'est donc jamais affichés dans la boucle **for b in range(5)**.

Par contre, la boucle **for a in range(5)** est exécutée pour toutes les itérations.


<br>

## Les compréhensions de liste

Permet d'itérer sur une liste et de filtrer les éléments grace a des structures conditionelles sur une seul ligne.

Sans compréhension de liste:
```python
liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
nombres_positifs = []
for i in liste:
    if i > 0:
        nombres_positifs.append(i * 2)
```

Avec compréhension de liste:
```python
liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
nombres_positifs = [i * 2 for i in liste if i > 0]
```

<br>

## Les fonctions **Any** et **All**

```python
any([False, False, True, False]) -> True
```

```python
all([False, False, True, False]) -> False
```

```python
all([True, True, True, True]) -> True
```

```python
all([f.endswith(".jpg") for f in files]) -> ?
```