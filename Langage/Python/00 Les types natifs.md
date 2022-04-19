#### [Sommaire](README.md)

# 00 Les types natifs

## Les chaînes de caractères

Les chaînes de caractères permettent de représenter du texte. Elles sont définies par des **guillemets simples** ou **doubles**. Attention avec les guillemets, vous pouvez avoir de drôle de surprises si vous utilisez des apostrophes dans votre texte.

Pour régler ce problème, vous pouvez alterner entre les **guillemets simples** ou **doubles**, ou utiliser un **anti-slash** pour 'échapper' le guillemet qui pose problème:

    "Bonjour, je m'appelle Thibault"  -> on alterne les guillemets doubles et simples (l'apostrophe)

    'Bonjour, je m\'appelle Thibault' -> on utilise l'anti-slash pour 'échapper' le guillemet simple (l'apostrophe)

#### Raw String

```python
print(r'c:/home/domino659/Linux-Test')
```

<br>

## Les nombres

Les nombres sont définis en deux catégories principales: les **nombres entiers** et les **nombres décimaux**.

<br>
    
## Les booléens
Les booléens sont des expression, qui retourneront **True** ou **False**. Permettant d'orienter votre programme dans la direction souhaitée.
  
<br>
    
## Les constructeurs de types natifs

Quand on définit un booléen, un nombre ou une chaîne de caractères, pas besoin donc de spécifier le type de la variable à créer. Python est suffisamment intelligent pour le déduire lui-même (grâce par exemple aux guillemets pour les chaînes de caractères).

Il existe cependant des classes qui nous permettent de créer ces objets:

- **str**

- **int**

- **float**

- **bool**

Ces classes ne sont pas très utiles pour créer des objets.

Mais elles sont très pratiques pour convertir un objet d'un type à un autre ! Raison pour laquelle vous les retrouverez souvent sous le nom de 'fonction de conversion'.

Ainsi, on peut convertir une chaîne de caractères en nombre entier ou vice-versa:

```python
str(5) -> "5"

int("5") -> 5
```

C'est une opération que l'on a souvent besoin de faire car il arrive que l'on récupère des variables dans un type qui n'est pas celui que l'on souhaite.

Par exemple, si vous récupérer un nombre à l'intérieur d'un fichier, il est possible qu'il vous soit retourné sous forme de chaîne de caractères. Mais pour l'additionner avec un autre nombre, vous serez obligé de convertir cette chaîne de caractères en nombre entier, ce que vous pourrez faire avec la fonction int.
