# Architecture Ansible

```
├── config (file) 
│   └── var.yml
│   └── vault.yml
|
├── inv (file) 
│   └── postprod (file)
│   │   └── group_vars(file) # Variable spécifique au host des groupes de serv
│   │   └── host_vars(file) # Variable spécifique au host serveur
│   │   └── hosts # List Serveurs
│   │
│   └── prod (file)
│   └── udd(file)
|
├── roles(file) 
│   └── mafonction (file)
│       └── defaults (file) # Variable utilisé par defaut (variables immuables (ssh, port 22))
│       │   └── main.ymml
│       └── files (file)
│       └── handlers (file) # Mini-fonction utilisé par ton rôle (restart apache)
│       │   └── main.ymml
│       └── tasks (file) # Main
│       │   └── main.ymml
│       └── templates (file) # Fichier jinja (ou autres) template front
│       └── vars (file) # # Variables qui ont tendance a changé selon l'infra ou autres (version WSL ou document root)
│           └── main.ymml
│ 
└── playbook00.yml
└── playbook01.yml
└── playbook02.yml
└── ansible.cfg
```


### Create Roles
    mkdir -p roles/monrole/{defaults,files,handlers,tasks,templates,vars}

## Playbook
```
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
```

## Roles
```
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
```
