# Architecture Ansible

```
├── inv(file) 
│   └── postprod(file)
│   │   └── group_vars(file) # Variable spécifique au host des groupes de serv
│   │   └── host_vars(file) # Variable spécifique au host serveur
│   │   └── hosts # List Serveurs
│   │
│   └── prod(file)
│   |   └── group_vars(file)
│   |   └── host_vars(file)
│   |   └── hosts
│   │
│   └── udd(file)
│       └── group_vars(file)
│       └── host_vars(file)
│       └── hosts
|
|

```
roles
    mafonction(file)
        defaults(file) # Variable utilisé par defaut (variables immuables (ssh, port 22))
            main.yml
        files(file) # File
        handlers(file) # Mini-fonction utilisé par ton rôle (restart apache)
            main.yml
        tasks(file) # Main
            main.yml
        templates(file) # Fichier jinja (ou autres) template front
        vars(file) # # Variables qui ont tendance a changé selon l'infra ou autres (version WSL ou document root)
            main.yml
playbooks.yml

### Create Roles
    mkdir -p roles/monrole/{defaults,files,handlers,tasks,templates,vars}

## Playbook
---
- hosts: all
  name: Manage file
  serial: 1
  #become: true

  roles:
    - { role: createfile, tags: ['file', 'create'] }
    - { role: addline, tags: ['file', 'line'] }
    - { role: addblock, tags: ['file', 'blockt4'] }
    - { role: pause, tags: ['file', 'pause'] }
    - { role: modifypingu, tags: ['file', 'modify'] }

## Roles
---
- name: Add Block
  ansible.builtin.blockinfile:
    path: /home/msion/Test01.txt
    state: present
    block: |
      C'est un pingoin
      Il a une maison sur la glace
      Il mange des sardines
      Il aime les igloo
    owner: msion
    group: msion
