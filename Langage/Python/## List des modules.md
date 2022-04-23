## [Sommaire](README.md)

# Liste des modules

## Modules

- [random](#random) <br>
  Générer des nombres aléatoires

- [pathlib](#pathlib) <br>
  Gérer les fichiers de l'os

- os: Obsoléte <br>
  Gérer les fichiers de l'os

- [logging](#logging) <br>
  Gérer les messages d'erreur/avertissement

- [faker](#faker) <br>
  Génerer des données aléatoires

- [datetime](#datetime) <br>
  Gestion des dates

<br>

---
---

<br>


## Random <a id="random"></a>

```python
random.randint(5, 10)
```

## Import

    import <nom_du_module>

<br>

### Guide

Print les fonction d'un module

    print(dir(random))

Print function help

    help(random.randint)

Print function help mise en forme

    from ppritn import pprint
    pprint(dir(random))

Print si une fonction est callable
print(callable(pprint))

<br>

---
---

<br>


## Pathlib <a id="pathlib"></a>

Python est excellent pour créer des scripts qui ont pour vocation de gérer des fichiers et des dossiers.

Historiquement, on utilisait des modules comme le module **os**, **glob** ou encore **shutil** pour exécuter des opérations de création, suppression et gestion des fichiers.

Le module **pathlib**, disponible depuis la version 3.4 de Python, permet d'effectuer presque toutes les opérations courantes sur un système d'exploitation, avec une syntaxe orientée objet beaucoup plus agréable à utiliser.

<br>

### La classe Path

La classe **Path** permet de créer un objet représentant un chemin vers un fichier ou un dossier de notre ordinateur. Ce chemin peut exister ou ne pas exister sur notre disque dur, ce n'est pas un prérequis.

La classe **Path** dispose de plusieurs méthodes de classes permettant d'accéder à des chemins courants de notre système d'exploitation, comme le dossier utilisateur:

```python
from pathlib import Path

dossier_utilisateur = Path.home()
```

On peut également récupérer le dossier courant:

```python
from pathlib import Path

dossier_courant = Path.cwd()
```

Ou encore créer un chemin spécifique en passant une chaîne de caractères à la classe Path:

```python
from pathlib import Path

documents = Path("/Users/domino659/Documents")
```

Si on affiche l'objet créé à partir de la classe **Path**, on se retrouve avec un objet **PosixPath**. Cet objet représente les chemins des systèmes Linux et Mac OS. Sur Windows, l'objet sera différent, car les chemins sur Windows ne sont pas les mêmes que sur Mac et Linux. Cela ne change cependant rien aux méthodes et attributs que l'on peut utiliser sur cet objet.

```python
>>> from pathlib import Path
>>> documents = Path("/Users/thibh/Documents")
>>> print(documents)
PosixPath('/Users/thibh/Documents')
```

<br>

### Concaténer des chemins

Pour concaténer des chemins, c'est très simple, il suffit d'utiliser une barre oblique (un slash en bon franglais):

```python
from pathlib import Path

home = Path.home()              # PosixPath('/Users/thibh/')
documents = home / "Documents"  # PosixPath('/Users/thibh/Documents')
```

Le résultat de cette concaténation nous retourne un nouvel objet **PosixPath**, nous pouvons donc concaténer plusieurs chaînes de caractères à la suite.

**pathlib** se charge de son côté de gérer les différents systèmes d'exploitation et d'utiliser un slash ou un antislash selon que vous utilisiez Mac / Linux ou Windows. Ce comportement est donc similaire à la fonction **os.path.join** du module **os**.

```python
from pathlib import Path

home = Path.home()                         # PosixPath('/Users/thibh/')
documents = home / "Documents" / "Projet"  # PosixPath('/Users/thibh/Documents/Projet')
```

On peut également utiliser la méthode **joinpath** sur un objet **Path**. Ça peut être pratique si vous avez par exemple une liste de dossiers que vous souhaitez concaténer (grâce à l'unpacking et à l'opérateur splat **\***):

```python
from pathlib import Path

home = Path.home()                        # PosixPath('/Users/thibh/')
dossiers = ['Projets', 'Django', 'blog']
home.joinpath(*dossiers)                  # PosixPath('/Users/thibh/Projets/Django/blog')
```

Si vous utilisez des slashs et que vous souhaitez utiliser une méthode de l'objet **Path**, pensez à utiliser les parenthèses pour entourer les chemins concaténés:

```python
from pathlib import Path

home = Path.home() # PosixPath('/Users/thibh/')

# Ne fonctionne pas car on essaie de récupérer l'attribut suffix sur la chaîne de caractères "main.py"
home / "Projet" / "main.py".suffix

# Avec des parenthèses, ça fonctionne !
(home / "Projet" / "main.py").suffix
```

Récupérer des informations sur un chemin

Grâce à l'orienté objet, on peut accéder à de nombreuses informations sur un chemin avec les attributs de l'objet **Path**:

```python
from pathlib import Path

p = Path("/Users/thibh/Documents/index.html")
p.name    # "index.html"
p.parent  # "/Users/thibh/Documents"
p.stem    # "index"
p.suffix  # ".html"
p.parts   # ("/", "Users", "thibh", "documents", "index.html")
```

Il existe également des méthodes qui permettent de vérifier l'existence et le type d'un chemin:

```python
from pathlib import Path

p = Path("/Users/thibh/Documents/index.html")
p.exists()   # True
p.is_dir()   # False
p.is_file()  # True
```

Là encore, quand un chemin peut nous être retourné par un de ces attributs, on récupère un objet **Path**.

On peut donc mettre bout à bout plusieurs fois le même attribut pour remonter de plusieurs dossiers par exemple:

```python
from pathlib import Path

p = Path("/Users/thibh/Documents/index.html")
p.parent.parent  # "/Users/thibh"
```

<br>

### Créer et supprimer des dossiers

Pour créer un dossier, on peut utiliser la méthode **mkdi**r. Cette méthode ne fonctionnera par défaut que si le dossier n'existe pas.

Vous pouvez utiliser le paramètre **exist_ok** pour signifier que vous ne souhaitez pas qu'une erreur soit levée si le dossier existe déjà:

```python
from pathlib import Path

dossier = Path("/Users/thibh/Documents/SiteWeb")
dossier.mkdir()  # Lève une erreur si le dossier existe déjà
dossier.mkdir(exist_ok=True)
```

Si vous souhaitez créer une hiérarchie de dossier qui n'existent pas, il faut ajouter le paramètre **parents**:

```python
from pathlib import Path

# Le dossier SiteWeb et ses sous-dossiers n'existent pas
dossier = Path("/Users/thibh/Documents/SiteWeb/sources/css")

# On peut tout créer d'un coup avec le paramètre parents
dossier.mkdir(parents=True)
```

Pour supprimer un dossier, on utilise la méthode **rmdir**:

```python
from pathlib import Path

dossier = Path("/Users/thibh/Documents/SiteWeb")
dossier.rmdir()
```

Cette méthode ne fonctionne que si le dossier est vide.

Si le dossier contient des fichiers ou d'autres sous-dossiers, cette méthode ne fonctionne pas, et c'est le seul cas de figure où nous sommes obligés de repasser par le module **shutil** et la fonction **rmtree**:

```python
import shutil
from pathlib import Path

dossier = Path("/Users/thibh/Documents/SiteWeb")
shutil.rmtree(dossier)
```

<br>

### Créer, lire et écrire dans un fichier

Pour créer et supprimer un fichier, on peut utiliser respectivement les méthodes **touch** et **unlink**:

```python
from pathlib import Path

fichier = Path("/Users/thibh/Documents/SiteWeb/index.html")
fichier.touch()   # On crée le fichier
fichier.unlink()  # On supprime le fichier
```

Pour écrire du contenu dans un fichier, on utilise la méthode **write_text**:

```python
from pathlib import Path

fichier = Path("/Users/thibh/Documents/SiteWeb/index.html")
fichier.write_text("Accueil du site")
```

Il n'est pas obligatoire de créer le fichier au préalable avec la méthode **touch**.

Vous conviendrez que c'est plus rapide que de faire:

```python
from pathlib import Path

fichier = Path("/Users/thibh/Documents/SiteWeb/index.html")
with open(fichier, "w") as f:
    f.write("Accueil du site")
```

De la même façon, pour lire le contenu d'un fichier, on peut utiliser la méthode **read_text**:

```python
>>> from pathlib import Path

>>> fichier = Path("/Users/thibh/Documents/SiteWeb/index.html")
>>> fichier.read_text()
"Accueil du site"
```

<br>

#### Scanner un dossier

Là où **pathlib** rayonne, c'est vraiment dans la possibilité de scanner les dossiers de votre ordinateur avec des méthodes beaucoup plus faciles à retenir que le module **glob**.

Pour récupérer tous les fichiers et dossiers à l'intérieur d'un dossier, on peut utiliser la méthode **iterdir**:

```python
from pathlib import Path

for f in Path.home().iterdir():
    print(f.name)
```

On peut combiner cette méthode avec la méthode **is_dir** pour ne récupérer que les dossiers (ici avec une compréhension de liste):

```python
from pathlib import Path

dossiers = [d for d in Path.home().iterdir() if d.is_dir()]
```

Pour scanner un dossier avec un peu plus de flexibilité, on peut utiliser la méthode **glob** (et oui, comme le module !). On peut par exemple ne récupérer que les fichiers dont l'extension est **.png**:

```python
from pathlib import Path

for f in Path.home().glob("*.png"):
    print(f.name)
```

Si vous souhaitez scanner un dossier de façon récursive, il suffit d'utiliser rglob à la place de glob:

```python
from pathlib import Path

for f in Path.home().rglob("*.png"):
    print(f.name)
```

<br>

### Quelques cas pratiques

Voici quelques cas pratiques qui vous montrent la flexibilité et la facilité d'utilisation de **pathlib**.

#### Ajouter un suffixe à un nom de fichier

```python
from pathlib import Path

p = Path.home() / "image.png"               # "/Users/thibh/image.png"
p.parent / (p.stem + "-lowres" + p.suffix)  # "/Users/thibh/image-lowres.png"
```

#### Trier des fichiers selon leur extension

```python
from pathlib import Path

dirs = {".jpg": "Images",
        ".gif": "Images",
        ".mp4": "Videos",
        ".pdf": "Documents",
        ".mp3": "Musiques",
        ".wav": "Musiques"}

tri_dir = Path.home() / "Tri"
files = [f for f in tri_dir.iterdirs() if f.is_file()]
for f in files:
    # Si aucune correspondance n'est trouvé pour l'extension, on place les fichiers dans un dossier Autres
    output_dir = tri_dir / dirs.get(f.suffix, "Autres")
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)
```

On peut utiliser la méthode **rename** pour déplacer un fichier.

#### Créer les constantes d'un dossier avec **file**

```python
from pathlib import Path

SOURCE_FILE = Path(__file__).resolve()  # resolve permet de résoudre les liens symboliques
SOURCE_DIR = SOURCE_FILE.parent
ROOT_DIR = SOURCE_DIR.parent
DATA_DIR = SOURCE_DIR / "DATA"
```

<br>

---
---

<br>


## Logging <a id="logging"></a>

5 types de **logging**:

- Debug
- Info
- Warning
- Error
- Critical

```python
import logging

logging.basicConfig(level=logging.INFO,
                    filename="app.log",
                    # Replace
                    filemode="w",
                    # Append
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("La fonction a bien été exécutée")
logging.info("Message d'information général")
logging.warning("Attention !")
logging.error("Une erreur est arrivée")
logging.critical("Erreur critique")
```
 <a id="random"></a>

<br>

---
---

<br>

## Faker <a id="faker"></a>

```python
from faker import Faker

fake = Faker(locale="fr_FR")

print(fake.unique.name())
print(fake.text())

for _ in range(500):
    print(fake.unique.random_int())

print(fake.job())
print(fake.file_path(depth=5, category='video'))
print(fake.credit_card_number(), fake.credit_card_expire(), fake.credit_card_secrurity_code())

print(fake.rgb_color())
print(fake.hex_color())

for _ in range(5):
    print(fale.numerify(text="%%%-#-%%%%-%%%%-%%%-##"))
    print(fale.bothify(text="Product Number: ????-########"))
```

<br>

---
---

<br>

## DateTime <a id="datetime"></a>

Il est très courant que nous ayons besoin de gérer des dates en programmation.

Pour réaliser ces opérations, Python dispose de la bibliothèque native **datetime** qui permet de gérer des objets représentant des dates et des heures.

### Comment un ordinateur calcule-t-il le temps ?

Vous avez peut-être déjà entendu parler de « l'Epoch », une date arbitraire aussi appelée « heure Unix »:

    L'heure Unix ou heure Posix (aussi appelée Unix Timestamp) est une mesure du temps basée sur le nombre de secondes écoulées depuis le 1er janvier 1970 00:00:00 UTC, hors secondes intercalaires. Elle est utilisée principalement dans les systèmes qui respectent la norme POSIX1, dont les systèmes de type Unix, d'où son nom. C'est la représentation POSIX du temps.

Le calcul du temps peut s'avérer complexe pour tout un tas de raison comme les secondes intercalaires, les fuseaux horaires ou encore l'heure d'été.

Généralement cela ne pose pas de problèmes (on a rarement besoin de prendre en compte les potentielles microsecondes de différence entre le temps universel et le temps solaire).

Avec Python, il est possible d'afficher le nombre de secondes écoulées depuis l'heure Unix avec la fonction **time** du module **time**.

```python
>>> from time import time
>>> time()
1634911800.733942
```

<br>

### Représenter le temps avec **datetime**

Pour aller un peu plus loin et manipuler des dates (et des heures), Python dispose du module **datetime** ainsi que trois classes principales:

- **date**
- **time**
- **datetime**

Vous vous en doutez, la classe **date** sert à gérer des dates, **time** à gérer du temps et **datetime** les deux.

Toutes ces classes disposent d'attributs permettant d'indiquer une année, un mois, un jour, une heure et également des informations de fuseau horaire.

```python
Voyons dans le détail comment créer ces objets:

>>> from datetime import date, time, datetime
>>> date(year=2021, month=10, day=22)
datetime.date(2021, 10, 22)
>>> time(hour=10, minute=19, second=10)
datetime.time(10, 19, 10)
>>> datetime(year=2021, month=10, day=22, hour=10, minute=19, second=10)
datetime.datetime(2021, 10, 22, 10, 19, 10)
```

Le nom du module **datetime** étant le même que le nom de la classe, on confond souvent les deux. Si vous importez le module directement, il faudra donc utiliser datetime.datetime ce qui est assez confu. Je préfère ainsi importer directement la classe avec **from datetime import datetime**.

Les classes **datetime** et **date** disposent également de deux fonctions, **now** et **today** qui permettent respectivement de récupérer la date et l'heure d'aujourd'hui (pour **datetime**) et la date d'aujourd'hui (pour **date**):

```python
>>> datetime.now()
datetime.datetime(2021, 10, 22, 10, 25, 7, 742193)
>>> date.today()
datetime.date(2021, 10, 22)
```

À noter également qu'il est possible de récupérer les valeurs de ces attributs mais pas de les modifier directement.

```python
>>> today = date.today()
>>> today.day = 23
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: attribute 'day' of 'datetime.date' objects is not writable
```

Pour remplacer un élément d'un objet datetime on peut utiliser la méthode **replace**:

```python
>>> today = date.today()
>>> tomorrow = today.replace(day=today.day + 1)
>>> today
datetime.date(2021, 10, 22)
>>> tomorrow
datetime.date(2021, 10, 23)
```
Je vous déconseille cependant d'utiliser cette méthode car elle ne prend pas en compte les problèmes de fuseaux horaires et du passage à l'heure d'été.

<br>

### Créer une date avec une chaîne de caractères

Il arrive souvent que nous souhaitions créer un objet datetime non pas à partir de nombres entiers mais directement à partir d'une chaîne de caractères.

Le problème qui se pose est que la représentation des dates sous forme de chaîne de caractères peut prendre beaucoup de formes.

Par exemple aux États-Unis, les dates sont généralement représentées sous le format MM-DD-YYYY.
En Europe on utilise plutôt DD-MM-YYYY (22-10-2021 pour le 22 octobre 2021).

Tout au long de cet article, je représenterai les jours, mois et années avec les lettres **D**, **M** et **Y**.

La norme **ISO8601** a été créée pour pallier à ce problème. Selon cette norme, on va de l'élément le plus grand au plus petit, une date serait donc représentée par **YYYY-MM-DD HH:MM:SS**.

Les objets de la classe **datetime** permettent de créer une instance à partir de ce format grâce à la fonction **fromisoformat**:

```python
>>> from datetime import date
>>> date.fromisoformat("2021-10-22")
datetime.date(2021, 10, 22)
```

Dans le cas où une date n'est pas dans le format ISO8601, on peut utiliser à la place la fonction **strptime** qui permet de spécifier le formatage de la date.

Imaginons une date représentée par la chaîne de caractères suivante:

```python
'22 Oct 2021'
```

Grâce à **strptime** et à un langage spécifique, on peut indiquer le format de la date en le passant en 2e argument à la fonction:

```python
>>> datetime.strptime("22 Oct 2021", "%d %b %Y")
datetime.datetime(2021, 10, 22, 0, 0)
```

Et si nous souhaitons réaliser l'opération inverse, nous pouvons le faire avec la fonction strftime:

```python
>>> now = datetime.now()
>>> now.strftime("%d %b %Y")
'22 Oct 2021'
```

Deux modules non inclus dans la bibliothèque standard de Python permettent de manipuler les dates avec beaucoup plus de facilité:

- **dateutil**

- **dateparser**

**dateutil** nous permet grâce au module **parser** et la fonction **parse** de créer un objet **datetime** sans avoir besoin de spécifier le format comme nous l'avons fait avec **strptime** et avec beaucoup plus de libertés:

```python
>>> from dateutil import parser
>>> parser.parse("12 october 2021 at 9 am and 18 minutes")
datetime.datetime(2021, 10, 12, 9, 18)
```

Notez cependant que nous utilisons ici **october** au lieu de **octobre**, cette bibliothèque ne comprenant pas le français:

```python
>>> parser.parse("12 octobre 2021")
  File "<stdin>", line 1, in <module>
    raise ParserError("Unknown string format: %s", timestr)
dateutil.parser._parser.ParserError: Unknown string format: 12 octobre 2021
```

La bibliothèque **dateparser** elle va cependant beaucoup plus loin en nous permettant d'utiliser des mots marqueurs de temps comme « aujourd'hui » ou « demain » et ce même dans différentes langues:

```python
>>> dateparser.parse("aujourd'hui")
datetime.datetime(2021, 10, 22, 11, 11, 18, 244967)
>>> dateparser.parse("demain")
datetime.datetime(2021, 10, 23, 11, 10, 19, 246512)
>>> dateparser.parse("ontem")  # La date d'hier en Portugais
datetime.datetime(2021, 10, 21, 11, 10, 46, 885066)
```

Cette bibliothèque est vraiment incroyable et j'ai encore du mal à trouver ses limites:

```python
>>> dateparser.parse("Il y a un mois")
datetime.datetime(2021, 9, 22, 11, 12, 42, 170722)
>>> dateparser.parse("One year ago at midnight")
datetime.datetime(2020, 10, 22, 0, 0)
```

<br>

### La gestion des fuseaux horaires
**
La gestion des fuseaux horaires est possible de différentes façons, surtout depuis l'ajout dans la version 3.9 de Python d'un nouveau module **zoneinfo**.

Les différents modules que nous allons voir dans cette partie utilisent une base de données appelée **tz database** également appelée **IANA database**.

#### ***Les dates « naive » et « aware »***

Une date « naive » est une date qui n'a aucune information de fuseau horaire (timezone en anglais). À l'inverse une date « aware » est définie selon un fuseau horaire précis.

Par défaut, les objets **datetime** comme ceux que nous avons créés ci-dessus sont « naive ». La façon la plus simple de vérifier les informations de fuseau horaire d'un objet **datetime** est de vérifier l'attribut **tzinfo**:

```python
>>> from datetime import datetime
>>> now = datetime.now()
>>> now.tzinfo
None
```

<br>

### Ajouter un fuseau horaire spécifique

Il existe différentes façons d'ajouter des informations de fuseau horaire à un objet **datetime** en fonction des versions Python que vous utilisez.

Depuis la version 3.9 de Python, le module de la bibliothèque standard **zoneinfo** permet de gérer les fuseaux horaires. Si vous utilisez une version de Python inférieure à 3.9, je vous conseille de regarder des modules comme **dateutil** ou **pytz**.

Les principes que nous allons voir dans la suite de cet article restent les mêmes peu importe le module utilisé.

Grâce à la classe **ZoneInfo** du module **zoneinfo** on peut créer un fuseau horaire en nous basant sur la **base de données IANA**.

Si je souhaite récupérer le fuseau horaire de Vancouver, je peux utiliser la chaîne de caractères **"America/Vancouver"**:

```python
>>> from zoneinfo import ZoneInfo
>>> now_in_vancouver = datetime.now(tz=ZoneInfo("America/Vancouver"))
>>> now_in_montreal = datetime.now(tz=ZoneInfo("America/Montreal"))
>>> now_in_montreal.hour
12
>>> now_in_vancouver.hour
9
```

On retrouve bien les 3 heures de décalages entre Montréal et Vancouver.

Étant à Montréal à l'heure où j'écris cet article, j'aurais pu utiliser **datetime.now()** sans préciser le paramètre **tz** pour récupérer la date et l'heure de l'endroit où je me trouve.

J'aurais donc eu un objet « aware » (**now_in_vancouver**) et un objet « naive » (**now_in_montreal**).

Cela ne pose pas de problème tant que nous n'effectuons aucune opération entre ces deux objets. En cas de comparaison ou de soustraction par exemple, nous avons une erreur si nous utilisons un objet « naive » et un objet « aware »:

```python
>>> now_in_vancouver = datetime.now(tz=ZoneInfo("America/Vancouver"))
>>> now_in_montreal = datetime.now()
>>> now_in_vancouver > now_in_montreal
  File "<stdin>", line 1, in <module>
TypeError: cant compare offset-naive and offset-aware datetimes
>>> now_in_vancouver - now_in_montreal
  File "<stdin>", line 1, in <module>
TypeError: cant subtract offset-naive and offset-aware datetimes
```

Pour changer de fuseau horaire, on utilise la méthode **astimezone**:

```python
>>> now_in_paris = now_in_vancouver.astimezone(ZoneInfo("Europe/Paris"))
>>> print(now_in_paris.hour)
18
```

Là encore, la différence est cohérente (9h de décalage entre Vancouver et Paris, on passe donc de 9h à 18h).

<br>

### Le Temps universel coordonné (UTC)

Vous avez déjà probablement entendu les acronymes UTC ou GMT, souvent utilisés quand vous devez planifier une réunion avec un collègue à l'autre bout du monde.

On fait souvent la confusion entre UTC et un fuseau horaire.

UTC n'est pas un fuseau horaire, c'est une échelle de temps qui a été acceptée par la grande majorité des pays comme échelle de temps universelle.

**Petite anecdote intéressante**: l'appellation correcte en anglais du temps universel coordonné (TUC) serait coordinated universal time, abrégé en CUT. Les experts de l’Union internationale des télécommunications étaient d’accord pour définir une abréviation commune à toutes les langues, mais ils étaient divisés sur le choix de la langue entre le français et l'anglais. Finalement, c’est le compromis UTC, nécessitant un effort des deux parties, qui fut choisi. C’est cette notation qui est utilisée par la norme ISO 8601.

On pense souvent à tort qu'UTC correspond à un fuseau horaire car nous pouvons convertir un object **datetime** en UTC grâce au module **timezone** de la bibliothèque **datetime** en le passant au paramètre **tz**:

```python
>>> from datetime import datetime, timezone
>>> now = datetime.now(tz=timezone.utc)
>>> now
datetime.datetime(2021, 10, 22, 15, 57, 4, 822209, tzinfo=datetime.timezone.utc)
>>> now.tzinfo
datetime.timezone.utc
```

Quand vous comparez des dates ou que vous souhaitez les modifier, il est très important de toujours le faire sur une base UTC. Je répète: **ne faites pas d'opérations sur des dates avec un fuseau horaire spécifique**.

Il est notamment dangereux d'effectuer une opération sur une date avec un fuseau horaire précis car les changements d'heures été / hiver ne seront pas pris en compte.

Par exemple à Montréal, il existe deux fuseaux horaires, EDT et EST (Eastern Daylight Time et Estern Standard Time), selon les périodes de l'année.

En 2020, le passage de l'heure d'hiver à l'heure d'été a eu lieu dans la nuit du 7 au 8 mars.

```python
>>> from datetime import datetime
>>> from zoneinfo import ZoneInfo
 
>>> montreal_tz = ZoneInfo('America/Montreal')
>>> print(datetime(2020, 3, 7, 13, 0, 0, tzinfo=montreal_tz))
2020-03-07 13:00:00-05:00
>>> print(datetime(2020, 3, 8, 13, 0, 0, tzinfo=montreal_tz))
2020-03-08 13:00:00-04:00
```
**
Dans le code ci-dessus, on peut voir la différence avec le temps UTC à la fin de l'affichage des dates (2020-03-07 13:00:00👉**-05:00**👈)

Le 7 mars, on a une différence de 5h entre le fuseau horaire de Montréal et UTC. Le 8 mars, la différence n'est plus que de 4h entre le fuseau horaire de Montréal et UTC.

On peut également voir cette différence avec le changement de nom du fuseau horaire:

```python
>>> montreal_tz = ZoneInfo('America/Montreal')
>>> print(datetime(2020, 3, 7, 13, 0, 0, tzinfo=montreal_tz).tzname())
EST
>>> print(datetime(2020, 3, 8, 13, 0, 0, tzinfo=montreal_tz).tzname())
EDT
```

La différence d'une heure par rapport à UTC est normale car on a avancé d'une heure dans la nuit du 7 au 8 mars 2020 à Montréal. L'écart relatif par rapport à UTC n'est donc plus le même entre le 7 et le 8 mars.

L'heure universelle UTC elle n'a pas bougé, mais l'heure à Montréal oui. Et ces changements n'arrivent pas toujours au même moment partout dans le monde.

C'est pour cette raison que tous les ans, pendant 3 semaines environ, il n'y a plus que 5h de décalage entre Paris et Montréal au lieu de 6 (car le passage à l'heure d'été en France se fait en général 2 à 3 semaines après le changement au Canada).

**Et cette différence peut causer des problèmes lorsque vous réalisez des opérations sur une date.**

Pour être très précis, EST et EDT ne sont pas des fuseaux horaires en soi. Un fuseau horaire est défini par un continent et le plus souvent une ville, comme nous l'avons vu dans la base de données IANA (par exemple Europe/Paris ou America/Montreal).

EST et EDT représentent la différence de temps avec UTC. Quand nous indiquons un fuseau horaire à **ZoneInfo**, nous donnons donc le nom du fuseau horaire (par exemple **America/Montreal**) et en fonction de la période de l'année, nous nous trouverons donc soit en EST soit en EDT, avec une différence par rapport à UTC qui ne sera pas la même.

D'ailleurs, pour afficher le ou les noms associés au fuseau horaire où l'on se trouve on peut utiliser le module **time**:

```python
>>> import time
>>> time.tzname
('EST', 'EDT')
```

<br>

### La mauvaise façon de faire

Voyons maintenant un exemple dans lequel nous travaillons directement avec un objet **datetime** sur le fuseau horaire de Montréal.

Nous souhaitons ajouter un jour à la date du 7 mars (nous utilisons pour ce faire la classe **timedelta** que nous verrons plus en détail dans la suite de cet article):

```python
>>> from datetime import datetime, timedelta
>>> from zoneinfo import ZoneInfo
>>> tz_montreal = ZoneInfo('America/Montreal')
>>> march_7 = datetime(2020, 3, 7, 13, 0, 0, tzinfo=tz_montreal)
>>> march_8 = march_7 + timedelta(days=1)
>>> print(march_8)
2020-03-08 13:00:00-04:00
```

Remarquez que l'heure n'a pas bougé. On vient juste d'ajouter 1 jour à notre date, sans prendre en compte le passage à l'heure d'été.

### La bonne façon de faire

Reprenons maintenant le même exemple en convertissant d'abord notre date en UTC avant de faire l'addition, puis en modifiant le fuseau horaire par la suite:

```python
>>> from datetime import datetime, timedelta
>>> from zoneinfo import ZoneInfo
 
>>> march_7 = datetime(2020, 3, 7, 13, 0, 0)
>>> march_7_utc = march_7.astimezone(ZoneInfo("UTC"))
 
>>> march_8 = march_7_utc + timedelta(days=1)
>>> march_8 = march_8.astimezone(montreal_tz)
>>> print(march_8)
2020-03-08 14:00:00-04:00
```

Nous remarquons cette fois-ci que l'heure d'été a bien été prise en compte et notre date affiche 14h au lieu de 13.

**En faisant l'opération sur une date basée sur UTC puis en convertissant par la suite dans le fuseau horaire voulu, nous obtenons le bon résultat.**

Prenons un autre cas de figure pour illustrer les problèmes causés lors du calcul de la différence entre deux dates:

```python
>>> from datetime import datetime
>>> from zoneinfo import ZoneInfo
 
>>> utc = ZoneInfo("UTC")
>>> montreal_tz = ZoneInfo('America/Montreal')
 
>>> march_7 = datetime(2020, 3, 7, 13, 0, 0, tzinfo=montreal_tz)
>>> march_10 = datetime(2020, 3, 10, 13, 0, 0, tzinfo=montreal_tz)
>>> march_7_utc = march_7.astimezone(utc)
>>> march_10_utc = march_10.astimezone(utc)
 
>>> print(march_10 - march_7)
3 days, 0:00:00
>>> print(march_10_utc - march_7_utc)
2 days, 23:00:00
```

Dans le premier cas de figure (**march_10 - march_7**), une simple soustraction est effectuée entre les deux dates au fuseau horaire de Montréal. On obtient donc une différence parfaite de 3 jours qui ne prend là encore pas en compte le passage à l'heure d'été.

Dans le deuxième cas de figure, avec les dates converties en UTC, on observe cette fois-ci bien une différence d'1h avec le résultat précédant, indiquant la prise en compte de l'heure qui a été "perdue" lors du passage à l'heure d'été.

<br>

### Calcul sur un objet **datetime**

Nous l'avons vu brièvement dans la partie précédente avec les **timedelta**, il est possible de réaliser des opérations entre deux dates ou de modifier une date.

La classe **timedelta** permet d'ajouter un intervalle de temps à une date. Attention, **timedelta** ne représente pas une date mais un intervalle. Vous remarquerez d'ailleurs que cette fois-ci, les attributs sont au pluriel:

```python
>>> from datetime import timedelta
>>> timedelta(days=20)
datetime.timedelta(days=20)
```

La classe **timedelta** permet d'ajouter ou de soustraire des jours, heures, secondes et même microsecondes. On peut sans problème utiliser des nombres positifs et négatifs en même temps.

Dans l'exemple ci-dessous, nous ajoutons 15 jours et soustrayons 5 heures à la date actuelle:

```python
>>> now = datetime.now()
>>> now_in_15_days_minus_5_hours = now + timedelta(days=15, hours=-5)
>>> print(now)
2021-10-22 17:43:23.840561
>>> print(now_in_10_days_minus_5_hours)
2021-11-06 12:43:23.840561
```

La date passe logiquement au mois suivant. C'est valable également pour des mois comme le mois de février qui ne contient que 28 jours.

```python
>>> feb_27_2022 = datetime(2022, 2, 27)  # 27 février
>>> print(feb_27_2022 + timedelta(days=3))  # On ajoute 3 jours
2022-03-02 00:00:00
```

On tombe bien sur le 2 mars et non le 30 février.

La classe **timedelta** ne permet d'ajouter que des jours, heures, minutes mais pas des mois ou des années. C'est cependant possible avec la classe **relativedelta** du module **dateutil** que nous avons vu précédemment mais qui n'est pas disponible dans la bibliothèque standard de Python:

```python
>>> from dateutil.relativedelta import relativedelta
>>> from datetime import datetime
>>> now = datetime.now()
>>> now_in_2_months = now + relativedelta(months=2)
>>> print(now)
2021-10-22 17:52:20.878397
>>> print(now_in_2_months)
2021-12-22 17:52:20.878397
```