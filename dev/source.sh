#!/bin/bash

# script to install all my setup linux dev

# Author: Andre V. Silva 2020-10-24
AUTHOR="Andre V. Silva"

# go to the HOME directory
cd

date=$(date)

# general information:
echo "author: $AUTHOR / date/time: $date"

# update and upgrade
sudo apt update && sudo apt upgrade -y

while [ $(ls -l | grep WaitToSource | wc -l) -eq 1 ]; do
    echo "Please wait to source in zsh shell file"
    sleep 5s
done

echo "Now I will source to zsh..."

# get user name
USERNAME=$whoami

# zsh
echo "source /home/$USERNAME/build/bin/thisroot.sh" >> ~/.zshrc

# root cern
echo "alias root='root -l'" >> ~/.zshrc

# go
echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.zshrc

# Add alias on shell, python 3
echo "alias python='/usr/local/bin/python3.7'" >> ~/.zshrc

source ~/.zshrc

sudo apt update && sudo apt upgrade -y
