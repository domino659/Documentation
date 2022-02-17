## Connection ansible to machine
    ansible -i inv/udd/hosts 178.32.244.255 -m ping # Test Ping

    ansible -i inv/udd/hosts 178.32.244.255 -m setup # Print variable of the remote host

## Launch Playbook
    ansible-playbook -i inv/udd/hosts playbook.yml
        --ask-become-pass -> ask sudo
        --check -> simulate launch playbook
        --tags ->  launch only selectes tags
        --limit -> launch only selected server or group
