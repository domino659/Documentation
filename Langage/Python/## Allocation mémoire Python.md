## [Sommaire](README.md)

# Allocation mémoir Python

Généralement lorsque l'on affecte une variable, Python généralement lui assigne un emplacement mémoire qui est unique a chaque execution du code.

Python effectue certains processus afin d'économiser de la mémoire. Il leurs assigne un empalcement mémoire fixe, on peut compter:

* Les **singelton**, ce sont des objets unique comme **True/Fale/none**.

* Les **small integer caching** qui comptent les nombres entre **-5** et **256**.

* Les **chaines de caractères** inférieur a + ou - 20 caractères.