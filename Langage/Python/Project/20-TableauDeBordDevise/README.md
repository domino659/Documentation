> poetry shell
> cd src && python manage.py runserver

Création Projet
> django-admin startproject DashboardDevise
> manage.py startapp myApp

Comme indiqué dans la vidéo précédente, voici les changements de l'API.

À la place de :
api.exchangeratesapi.io/latest

Utilisez :
api.exchangerate.host/latest

À la place de :
api.exchangeratesapi.io/history?start_at=2020-01-01&end_at=2020-01-04

Utilisez :
api.exchangerate.host/timeseries?start_date=2020-01-01&end_date=2020-01-04

Pour récupérer certaines devises uniquement dans un lapse de temps définni :
À la place de :
api.exchangerate.io/history?start_at=2020-10-01&end_at=2020-10-03&symbols=USD,CAD

Utilisez :
api.exchangerate.host/timeseries?start_date=2020-10-01&end_date=2020-10-03&symbols=USD,CAD

Vous pouvez voir la documentation de l'API ici (des exemples pour Python sont disponibles) :

https://exchangerate.host/#/#docs