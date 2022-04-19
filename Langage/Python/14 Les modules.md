## [Sommaire](README.md)

# Les modules

Les modules sont des fichiers contenant du code Python, pour être utilisé il doit être importé. Cela permet en plus de se servir dans des modules exterieurs de segmenter son code en différent parties.

```python
import random
```

Une fois importé on peut utiliset toutes les fonctions, classes, variables qu'il contient. (**conseillé**)

```python
import random

random.uniform(2,5)
```

Il est aussi possible d'importer directement une fonction spécifique d'un module (**déconseillé**).

```python
from random import uniform

uniform(2,5)
```

La variable **name** permet de détécter dans quelle module le script est entrain de s'executer.
Dans l'exemple ci-dessous le print ne sera exécuter que dans le ficher d'origine du module.

```python
if __name__ == "__main__:
    print("I'm here")
```

## Python Path

```python
import sys
sys.path.append("\\wsl$\Debian\home\domino659\Documentation\Langage\Python\package")
sys.path.append("Langage\Python\package")
import package
```

Voir [section 45](https://www.udemy.com/course/formation-complete-python/learn/lecture/14611514#overview) pour intégrer des modules définitivement au python path de l'OS.
