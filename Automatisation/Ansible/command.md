## [Sommaire](README.md)

## Connection ansible to machine

Test Ping

    ansible -i inv/udd/hosts <ADDRESSE IP/DNS> -m ping

Print variable of the remote host

    ansible -i inv/udd/hosts <ADDRESSE IP/DNS> -m setup

<br>

## Lancer Playbook

    ansible-playbook -i inv/udd/hosts playbook.yml
        --ask-become-pass -> ask sudo
        --check -> simulate launch playbook
        --tags ->  launch only selectes tags
        --limit -> launch only selected server or group
        --ask-become-pass -> If need root access

<br>

## Create Vault

Dossier externe contenant mdp

    mkdir -p .credentials/ansible.yml

Crée dossier vault si il n'existe pas

    ansible-vault create config/vault.yml

Editer le fichier vault

    ansible-vault edit config/vault.yml
