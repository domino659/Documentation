## [Sommaire](README.md)

# Terminal

## Affichage fichiers

    ls

## Afficher les fichiers cachés et les listés

    ls -al

## Créer Fichier
### Créer fichier

    touch
    
### Créer dossier
    
    mkdir

### L'option -p permet de créer des sous répertoires
    
    mkdir -p

### Supprimer dossier
    
    rm

## Ouvrir Dossier via VS Code
    
    code .
    
## Ouvrir Dossier via explorer
 
    explorer.exe .

## Session root

    sudo -i

## Find Package info

    apt-cache search ssl | grep openssl

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
