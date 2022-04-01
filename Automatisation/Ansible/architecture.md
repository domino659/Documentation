## [Sommaire](README.md)

# Architecture Ansible

```yml
├── config (file) 
│   └── var.yml
│   └── vault.yml
│
├── inv (file) 
│   └── postprod (file)
│   │   └── group_vars(file)
│   |   |   └── all.ymml # Variable spécifique a toutes les entités
│   |   |   └── vm.ymml # Variable spécifique a un groupe d'entités
│   │   └── host_vars(file)
│   |   |   └── makemake.ymml # Variable spécifique a une entité
│   │   └── hosts # List Serveurs
│   │
│   └── prod (file)
│   └── udd(file)
│
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
└── ansible.cfg # Fichier config Ansible
```

<br>

#### Ancible.cfg

```yml
[defaults]
ansible_managed         = Ansible managed: {file} modified on %Y-%m-%d %H:%M:%S by {uid} on {host}
retry_files_enabled     = False
vault_password_file     = /home/domino659/.credentials/ansible.yml
# interpreter_python      = /usr/bin/python3
forks                   = 5
host_key_checking       = False
# roles_path              = ./roles
# inventory               = ./inv

[ssh_connection]
ssh_args                = -o ControlMaster=auto -o ControlPersist=60s -o ForwardAgent=yes
```

<br>

### Créer Roles


```
mkdir -p roles/monrole/{defaults,files,handlers,tasks,templates,vars}
```

<br>

### Playbook

```yml
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

<br>

### Roles

```yml
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