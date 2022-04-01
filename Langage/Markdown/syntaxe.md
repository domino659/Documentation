## [Sommaire](README.md)

# Syntaxe Markdown

# Titre de niveau 1

    # Titre de niveau 1

## Titre de niveau 2

    ## Titre de niveau 2

### Titre de niveau 3

    ### Titre de niveau 3

#### Titre de niveau 4

    #### Titre de niveau 4

##### Titre de niveau 5

    ##### Titre de niveau 5

###### Titre de niveau 6

    ###### Titre de niveau 6

<br>

**Phrase en gras**

    **Phrase en gras**

_Phrase en italique_

    _Phrase en italique_

<br>

## Listes à puces ordonées

* Item 1
* Item 2
* Item 3

```
* Item 1
* Item 2
* Item 3
```

<br>

## Listes numérotées

1. Item 1
2. Item 2
3. Item 3

```
1. Item 1
2. Item 2
3. Item 3
```

<br>

## Liens

[Texte du lien](http://www.google.fr "Texte pour le titre, facultatif")

    [Texte du lien](http://www.google.fr "Texte pour le titre, facultatif")

<br>

## Ancrage

[lien afficher](#nomAncre)
## Titre <a id="nomAncre"></a>

    [lien afficher](#nomAncre)
    ## Titre <a id="nomAncre"></a>

<br>

## Liens par référence

Rendez-vous sur [Texte du lien][monsite] !
[monsite]: http://www.google.fr "Titre facultatif"

    Rendez-vous sur [Texte du lien][monsite] !
    [monsite]: http://www.google.fr "Titre facultatif"

<br>

## Images

![Texte alternatif](http://www.monsite.fr/image.png "Texte pour le titre, facultatif")

    ![Texte alternatif](http://www.monsite.fr/image.png "Texte pour le titre, facultatif")

<br>


## Images par référence

![Text alternatif][img-monsite]
[img-monsite]: http://www.monsite.fr/image.png "Titre facultatif"

    ![Text alternatif][img-monsite]
    [img-monsite]: http://www.monsite.fr/image.png "Titre facultatif"

<br>

## Citations

> Ceci est une citation

    > Ceci est une citation

<br>

## Code source ```<LANGAGE> au début et a la fin du bloc ou indentation d'une tabulation ou 4 espaces

```python
print("Hello World!")
```    

<br>

## Code source (en ligne)

Utilises la fonction `strpad()` !

<br>

## Séparateur Horizontal
---

<br>

* * *

<br>

- - -

<br>

## Espacement

Retour a la ligne: <br/>
Espaces: &nbsp;

<br>

## Diagramme d'arborescence

    ├── file
    │   └── var.yml
    │   └── vault.yml
    |
    ├── file2
    │   └── prod
    │   │   └── users
    │   │   └── hosts