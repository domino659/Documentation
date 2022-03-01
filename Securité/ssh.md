## Création clé SSH (à stocker dans /home/username/.ssh)
    ssh-keygen -o -a 200 -t ed25519 -C "<USERNAME> <DATE>" -f <KEY_NAME>

    Protocole	Longueur minimum (bits)	    Longueur Maximum(bits)
    RSA	        1024	                    16384
    ECDSA	    256	                        521
    DSA	        512	                        2048
    Ed25519	    256	                        256

## Connexion SSH Serveur
    
    ssh <USER>@<ADDRESSE IP/DNS>
    
Connect as root
    
    ssh <ADDRESSE IP/DNS> -l root

Example

    ssh ganymede.gwath-land.fr -l root

Dossier Config SSH

    Host *
            ForwardAgent yes
            StrictHostKeyChecking no
            HashKnownHosts yes
            PermitLocalCommand yes
            ServerAliveInterval 30

    Host    ganymede.gwath-land.fr
            User domino659
            IdentityFile ~/.ssh/msion_axians
            Port 22
