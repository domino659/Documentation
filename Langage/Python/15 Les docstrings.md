## [Sommaire](README.md)

# Les docstrings

```python
# Ceci est un commentaire

"""
Ceci
est
un paragraphe
de
commentaire
"""
```

Les docstrings permettent de recupérer les commentaires sous forme de documentation.

Il existre 3 formats de dosctrings: **Epytext**, **reST** et **Google**:

```
"""Docstring de style Epytext

@param param1: un premier paramètre
@param param2: un autre paramètre
@return: Description de ce qui est retourné
```

```
"""Docstring de style reST

:param param1: un premier paramètre
:param param2: un autre paramètre
:return: Description de ce qui est retourné
```

```
Docstring de style Google

Args:
    param1: un premier paramètre
    param2: un autre paramètre

Returns:
    Description de ce qui est retourné
```

```python
def print(text):
    """Description de la fonction

    Args:
        text (str): Text to print

    Returns:
        str: Text to be printed
    """
    return print(text)
```
