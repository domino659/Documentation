## [Sommaire](README.md)

# Les fonctions

## Pourquoi utiliser des fonctions

Les fonctions permettent d'éviter la répétition de code dans nos programmes.

En créant des fonctions, on va ainsi pouvoir ré-utiliser certains morceaux de code et même, grâce aux paramètres, obtenir différents résultats en fonction des arguments envoyés.

<br>

## La syntaxe

Pour créer une fonction, on la déclare avec l'instruction **def**, suivie du **nom de la fonction**, de **parenthèses**, et de **deux points**:

```python
def ma_fonction():
```

Même si vous ne mettez rien à l'intérieur des parenthèses pour le moment, vous êtes obligés de les mettre.

Une fonction ne peut cependant pas être vide, au minimum, vous devrez donc indiquer une ligne de code dans un bloc d'instruction contenu à l'intérieur de votre fonction. Si vous ne savez pas encore ce que votre fonction va contenir, vous pouvez utiliser l'instruction pass:

```python
def ma_fonction():
    pass
```

<br>

## Retourner une valeur

Pour retourner une valeur dans une fonction, on utilise l'instruction **return**.

Une fonction n'est pas obligée de retourner une valeur ! Vous pouvez très bien créer des fonctions qui exécutent une action et ne retournent rien (par défaut, la valeur None sera tout de même retournée si vous ne mettez aucune instruction **return**).

Vous pouvez également retourner plusieurs valeurs en les séparant par une virgule, par exemple:

```python
def foo():
return 5, 10
```

<br>

## Les paramètres et les arguments

Attention à la nomenclature ici, les mots paramètres et arguments sont bien souvent utilisés à tort et à travers dans de nombreux tutoriels que vous trouverez en ligne. Mais il existe bien une différence entre les deux:

- Les _paramètres_ c'est ce que vous écrivez entre les parenthèses **lorsque vous définissez la fonction**.

- Les _arguments_, ce sont les valeurs que vous envoyez à ces paramètres **lorsque vous appelez la fonction**.

Prenons un exemple :

```python
def addition(a, b):
return a + b

addition(a=5, b=10)
```

Dans le code ci-dessus, vous établissez **deux paramètres**, **a** et **b**, dans la **définition** de la fonction :

```python
def addition(a, b):
```

Ensuite, **vous envoyez comme argument** respectivement les valeurs **5** et **10** aux **paramètres** **a** et **b**.

Les paramètres que vous définissez peuvent avoir des valeurs par défaut. Cela vous permet de ne pas forcément envoyer d'argument lorsque vous appelez votre fonction:

```python
def addition(a=1, b=1):
return a + b

addition() # 2
```

La fonction ci-dessus peut-être appelée sans envoyer aucune valeur en argument et elle retournera 2 (1 + 1) en utilisant les valeurs par défaut définis dans la définition de la fonction.

Si un paramètre n'a pas de valeur par défaut, vous devez absolument lui envoyer une valeur en argument, faute de quoi Python vous retournera une erreur :

```python
def addition(a, b=2):
return a + b

addition(b=5) # TypeError: addition() missing 1 required positional argument: 'a'
```

Notez également qu'il n'est pas possible de définir un paramètre sans valeur par défaut après un paramètre avec une valeur par défaut.

```python
def addition(a=1, b):
return a + b

# SyntaxError: non-default argument follows default argument
```

Dans ce cas-ci, vous avez **trois options** : ajouter une valeur par défaut au paramètre **b**, enlever la valeur par défaut au paramètre **a**, ou bien placer le paramètre **a** et sa valeur par défaut après le paramètre **b**:

```python
def addition(a=1, b=2): # Valide
def addition(a, b): # Valide
def addition(b, a=1): # Valide
```

<br>

## Espaces global et local

Quand vous définissez une fonction, vous définissez un espace local à la fonction.

Cela signifie que toutes les variables définies à l'intérieur de cette fonction ne seront pas disponibles en dehors de la fonction :

```python
def foo():
a = 5

print(a) # NameError: name 'a' is not defined
```

☝️ La variable **a** définie à l'intérieur de la fonction n'est pas accessible en dehors de la fonction.

Vous avez par contre accès à l'intérieur d'une fonction à une variable définie dans l'espace global de votre script :

```python
a = 5

def foo():
print(a)

foo()
```

☝️ Le code suivant affichera bien la valeur de **a** et vous n'aurez pas d'erreur.

Attention cependant : dès que vous créez une variable à l'intérieur d'une fonction, cette variable devient local à la fonction et ne modifiera donc pas la variable global :

```python
a = 5

def foo():
a = 10
print(a)

foo()
print(a)
```

☝️ Dans ce code, on crée une variable **a** dans la fonction qui est donc différente de la variable **a** définie dans l'espace globale.

Ce script affichera donc 10 (la valeur de **a** dans la fonction **foo** que l'on appelle) puis 5 (la valeur de **a** dans l'espace global, qui n'a donc pas été modifiée).

Deux fonctions existent pour afficher les variables stockès dans les espaces **locales** et **globals**.

```python
a = 4

def foo():
    b = 5
    locals()

globals()
```
