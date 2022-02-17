## Connection ansible to machine
Test Ping

    ansible -i inv/udd/hosts <ADDRESSE IP/DNS> -m ping

Print variable of the remote host

    ansible -i inv/udd/hosts <ADDRESSE IP/DNS> -m setup

## Lancer Playbook
    ansible-playbook -i inv/udd/hosts playbook.yml
        --ask-become-pass -> ask sudo
        --check -> simulate launch playbook
        --tags ->  launch only selectes tags
        --limit -> launch only selected server or group

## Create Vault
Dossier externe contenant mdp

    mkdir -p .credentials/ansible.yml

Crée dossier vault si il n'existe pas

    ansible-vautl create config/vault.yml

Editer le fichier vault

    ansible-vault edit config/vault.yml
