Install Package Debian
    
    apt-get install ansible git ksh htop iftop grc vim net-tools screen sysstat software-properties-common apt-transport-https wget curl tree

## Charger clé SSH au lancement teminal
(ajouter a la fin du dossier ~/.bashrc)

    SSH_AGENT_CONF="$HOME/.ssh/agent"
    if [ -e "$SSH_AGENT_CONF" ];then
        . $SSH_AGENT_CONF > /dev/null
    fi
    ssh-add -l 2>/dev/null >/dev/null
    if [ $? -ne 0 ];then
        ssh-agent >| $SSH_AGENT_CONF
        if [ $? -ne 0 ];then
            echo "ERROR: Could no launch ssh-agent" >&2
        fi
        . $SSH_AGENT_CONF > /dev/null
        ssh-add ~/.ssh/<KEY_NAME>
    fi
    if [ $TILIX_ID ] || [ $VTE_VERSION ]; then
        source /etc/profile.d/vte.sh
    fi
