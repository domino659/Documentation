ls -al #Afficher les fichiers cachés

sudo dpkg --list #Afficher list
sudo dpkg --list | grep '^rc' #Afficher package a désinstaller
purge <APP_NAME> #Remove application
autoremove #Remove package