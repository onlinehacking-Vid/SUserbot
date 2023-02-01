#!/bin/bash

# shortcut file for running the bot in linux

uname=$(uname -n)
filename="./config.txt"
repo="https://github.com/Team-Deadly/DeadlyUserbot.git"
pytgcalls=$(pip3 show py-tgcalls)
G='\033[0;32m'


# not found
no_cmd="not found"


installed() {
    return $(dpkg-query -W -f '${Status}\n' "${1}" 2>&1|awk '/ok installed/{print 0;exit}{print 1}')
}


clear
echo -e "${G}Welcome to Deadly Userbot.\n"
sleep 3


if [ "$uname" == "localhost" ]; then
    clear
    # update & upgrade ubuntu
    echo -e "${G}Updating & Upgrading ubuntu apt . . .\n"
    apt update && apt upgrade
    clear

    # install python3
    if ! installed python3; then
       echo -e "${G}Installing python3 . . .\n"
       apt install python3
       clear
    fi

    # install python3 pip
    if ! installed pip; then
       echo -e "${G}Installing python3 pip . . .\n"
       apt install pip
       clear
    fi
    
    # installing all requirements
    if ! installed pip; then
       echo -e "${G}Installing requirements. . . \n"
       pip3 install -r requirements.txt
       clear
    fi

    python3 -u -m deadly
else
    python3 -u -m deadly
fi
