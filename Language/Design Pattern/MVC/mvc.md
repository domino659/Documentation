## MVC

Modèle-vue-contrôleur ou MVC est un motif d'architecture logicielle destiné aux interfaces graphiques.

Le motif est composé de trois types de modules ayant trois responsabilités différentes : les modèles, les vues et les contrôleurs.

### Model
Un modèle contient les fonctions chargés d'aller chercher les données en BDD. On y trouve les appels SQL et les opérations (Create, Read, Update, Delete).

### View
La vue est la partie chargé de l'affichage, elle récupére les variables et les affiches. Elle est majoritairement composé de HTML et d'un language type PHP ou Jinja2 par exemple.

### Controller
Un contrôleur contient la logique qui gère les conditions et qui prend les décisions. Il fait la liaison entre le Model et la View.
Son rôle est donc de demander les données au Model, de les analyser, prendre les décisions avant de les passer a la View. C'est ici que va se faire le contrôle d'accès.

### Entité
L'entité représente la donnée que l'on va manipuler. Elle prend souvent la forme d'un objet avec les mêmes propriétés inscrites que celles dans la BDD.a

![mvc](/File/Language/Architecture/mvc.png)

Le controlleur sait ce qu'il doit faire via l'URL. En fonction de la l'URL séléctionné le routeur enverra la requête au bon controlleur, qui lui même interrogera le model et ensuite celui-ci passera les donnérs a la view.

![mvc](/File/Language/Architecture/mvc_router.png)