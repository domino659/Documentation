## [Sommaire](README.md)

# Les fichiers

### [Voir **ICI** pour méthodes de pathlib](<%23%23 List des modules.md>)

## Chemins d'accès

```python
chemin = r"H:\Mon Drive\Code\Formation\Python\test.json"
```

<br>

## Lire le contenu d'un fichier

Methode standard:

```python
access = open(chemin, "r")
contenu = access.read()
print(contenu)
access.close()
```

Methode avancé, ne necessite pas la fermeture du fichier:

```python
with open(chemin, "r") as access:
contenu = access.read()
print(contenu)
```

Option pour windows:

```python
with open(chemin, "r", encoding='utf-8') as access:
```

### Fonction assiocié a read

splitline <br>
Place chaque retour a la ligne comme un élément d'un array.

```python
with open(chemin, "r") as access:
contenu = access.read().splitlines()
print(contenu)
```

<br>

## Ecrire à l'intérieur d'un fichier

Remplacer contenu existant:

```python
with open(chemin, "w") as access:
contenu = access.write("Bonjour")
print(contenu)
```

Ajouter fin dossier:

```python
with open(chemin, "a") as access:
contenu = access.write("Bonjour")
print(contenu)
```

# Format JSON

**JSON** (**J**ava**S**cript **O**bject **N**otation) est le nom d'un format d'échange de données.

Bien qu'originellement créé pour une utilisation avec le langage JavaScript, ce format étant basé entièrement sur du texte, il est possible de l'utiliser avec d'autres langages.

Avec Python, on peut utiliser le module **json** disponible dans la bibliothèque standard.

Avec Python, un fichier JSON peut contenir les types de données suivants:

- Une **chaîne de caractères**
- Un nombre (**entier** et **décimal**)
- Un **booléen**
- L'objet **None**
- Une **liste**
- Un **dictionnaire**

Dans le format JSON, certains types de données seront notés différemment que ce à quoi nous sommes habitués avec Python:

- Pour les chaînes de caractères, **seuls les guillemets doubles** sont acceptés
- Les booléens s'écrivent tout en minuscule (**true** et **false**)
- L'objet **None** est représenté par **null**

Il est important de noter qu'un fichier JSON ne peut contenir **qu'un seul objet**.

Ainsi, si vous souhaitez stocker plusieurs chaînes de caractères dans un fichier JSON, vous devrez par exemple les inclure dans une liste.

Ce fichier JSON est donc valide:

```json
["Pascal", "Patrick"]
```

Mais pas celui-ci:

```json
"Pascal"
"Patrick"
```

Vous pouvez par contre sans problème stocker une seule valeur.

Un fichier JSON peut donc contenir une chaîne de caractères ou un nombre.

```json
"Patrick"
```

```json
2938.231
```

Dès que vous souhaitez stocker plusieurs objets, il faut donc passer par une liste ou un dictionnaire.

Voici quelques exemples de fichiers JSON valides:

```json
{
  "Patrick": {
    "salaire": 24000,
    "date_embauche": "2020-10-25",
    "manager": true
  },
  "Pascal": {
    "salaire": 35000,
    "date_embauche": "2020-08-17",
    "manager": false
  }
}
```

```json
{
  "Cahiers": 3,
  "Stylos": 2,
  "Agrafes": null
}
```

```json
[1, 4, 2, 3, 1, 76, 4, 23, 4]
```

```json
["Bonjour", null, "test", 34, 9.743, false]
```

De nombreux outils en ligne (comme **jsonlint**) vous permettent de vous assurer de la validité d'un fichier JSON.

Le module **json** se charge automatiquement de convertir les données JSON dans un format de donnée valide pour Python.

Si par exemple votre fichier JSON contient le booléen **true**, vous récupérerez bien un booléen (**True**) et non pas la chaîne de caractères **"true"**. Pas besoin donc de faire la moindre conversion que ce soit. C'est tout l'avantage du module **json** et des fichiers JSON.

Imaginons le cas suivant: on veut sauvegarder dans un fichier JSON la valeur d'un booléen pour lire cette valeur de nouveau par la suite.

On aura donc le script suivant pour sauvegarder le booléen:

```python
import json

with open("/chemin/vers/fichier.json", "w") as f:
    json.dump(True, f)
```

À ce stade-ci, mon fichier JSON sur le disque contiendra ceci:

```json
true
```

Car rappelez-vous, avec le format JSON, les booléens sont en minuscule. Le module **json** de Python se charge donc automatiquement de faire la conversion pour nous.

Par la suite, quand on récupère la valeur du booléen sauvegardé dans le fichier JSON, on remarque que l'objet récupéré est là encore directement reconnu par Python comme un booléen:

```python
import json

with open("/chemin/vers/fichier.json", "r") as f:
    data = json.load(f)

print(data)  #  True
print(type(data))  #
```

## Lire un fichier JSON

Pour lire un fichier JSON, on utilise la fonction **load** du module **json**.

Il faudra au préalable ouvrir le fichier en mode lecture, par exemple avec l'instruction **with**:

```python
import json

with open("/chemin/vers/le_fichier.json", "r") as f:
    data = json.load(f)
```

On passe à la fonction **load** l'objet qui correspond au fichier ouvert, qui dans le cas ci-dessus est contenu dans la variable **f**.

Si vous essayez de lire un fichier JSON qui contient des données invalides, vous obtiendrez une erreur de type **JSONDecodeError**.

## Écrire dans un fichier JSON

Pour écrire dans un fichier JSON, on utilise la fonction **dump** du module **json**.

Là encore, il faudra au préalable ouvrir le fichier, cette fois-ci en mode écriture:

```python
import json

data = [1, 2, 3, 4, 5]

with open("/chemin/vers/le_fichier.json", "w") as f:
    json.dump(data, f)
```

On passe en premier à la fonction **dump** l'objet que l'on souhaite écrire (ici, l'objet **data**) et en deuxième le fichier dans lequel on veut écrire (ici, la variable **f**).

Si jamais vous ne vous souvenez plus dans quel ordre vous devez spécifier les arguments, pensez de façon logique. On indique ce que l'on veut écrire (les données), et ensuite dans quoi on veut les écrire (le fichier).

La fonction **dump** contient un paramètre **indent** auquel on peut passer un nombre entier.

Cela permet d'organiser vos données de façons plus claire dans le fichier JSON en spécifiant un nombre d'espaces selon lequel indenter l'objet écrit (un peu comme le fait le module **pprint**).

Sans **indent**:

```python
import json

data = {
    "Cahiers": 3,
    "Stylos": 2,
    "Agrafes": None
}

with open("/Users/thibh/test.json", "w") as f:
    json.dump(data, f)
```

Le fichier JSON contiendra:

```json
{ "Cahiers": 3, "Stylos": 2, "Agrafes": null }
```

Avec un **indent** de 2:

```python
import json

data = {
    "Cahiers": 3,
    "Stylos": 2,
    "Agrafes": None
}

with open("/Users/thibh/test.json", "w") as f:
    json.dump(data, f, indent=2)
```

```json
{
  "Cahiers": 3,
  "Stylos": 2,
  "Agrafes": null
}
```

Avec un **indent** de 4:

```python
import json

data = {
    "Cahiers": 3,
    "Stylos": 2,
    "Agrafes": None
}

with open("/Users/thibh/test.json", "w") as f:
    json.dump(data, f, indent=4)
```

```json
{
  "Cahiers": 3,
  "Stylos": 2,
  "Agrafes": null
}
```

Script Complet (récypération données et modification):

```python
import json

with open("data.json", "r") as f:
    donnees = json.load(f)

donnees.append(4)

with open("data.json", "w") as f:
    donnees = json.dump(donnees, fn indent=4)
```
