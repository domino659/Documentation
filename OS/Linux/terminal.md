##Affichage fichiers

    ls

## Afficher les fichiers cachés et les listés

    ls -al

## Gestion packages
Afficher list des packages

    sudo dpkg --list

## Afficher package a désinstaller

    sudo dpkg --list | grep '^rc'

## Remove package

    purge <APP_NAME>

## Remove dépendances inutiles

    autoremove

## Recherche d'un chaîne de caractères dans un fichier spécifié

    grep

## Trouver emplacement disque Ubuntu (Exolorateur de fichier)

    \\wsl$ 

## Paramètrage terminal de commande (Windows Terminal)
 Changer lancement WSL
 
    \\wsl$\<Nom_WSL>\home\<LOGIN>
