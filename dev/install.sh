#!/bin/bash

# script to install all my setup linux dev

# Author: Andre V. Silva 2020-10-24
AUTHOR="Andre V. Silva"

# go to the HOME directory
#cd

date=$(date)

# general information:
echo "author: $AUTHOR / date/time: $date"
echo "Starting the instalation of ALL my setup linux dev..."
echo "This will take a while, please be pacient... :)"

# smart way to source zsh after
# to install all.
#touch WaitToSource

# update and upgrade
sudo apt update && sudo apt upgrade -y

# pre requisites
#sudo apt-get install -y build-essential git zsh libexpat1-dev libssl-dev zlib1g-dev \
#liblzma-dev libsqlite3-dev libffi-dev tcl-dev libreadline-dev tk tk-dev build-essential \
#libncurses5-dev libgdbm-dev libnss3-dev git dpkg-dev cmake g++ gcc binutils libx11-dev \
#libxpm-dev libxft-dev libxext-dev gfortran libpcre3-dev libglu1-mesa-dev libglew1.5-dev \
#libftgl-dev libfftw3-dev libcfitsio-dev graphviz-dev libavahi-compat-libdnssd-dev \
#libldap2-dev python-dev libxml2-dev libkrb5-dev libqt4-dev libncursesw5-dev libdb5.3-dev \
#libbz2-dev libicu-dev libboost-all-dev wget curl vim libpq-dev unetbootin gddrescue ssh \
#tree htop gtk2-engines-murrine gtk2-engines-pixbuf openssh-client \
#sublime-text gnome-tweak-tool

#sudo apt update && sudo apt upgrade -y

# install python 3 from source
#wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tar.xz
#tar xf Python-3.7.9.tar.xz
#cd Python-3.7.9
#./configure --enable-optimizations
#make -j 4
#sudo make altinstall

#cd

sudo apt update && sudo apt upgrade -y

# LaTeX: full package texlive
#sudo apt update 
#sudo apt install texlive-full
#sudo apt update && sudo apt upgrade -y

# install root cern
#mkdir build
#git clone http://root.cern.ch/git/root.git
#cd root
#git checkout v6-22-02
#cd
#cd build
#cmake /home/andsilva/root/
#make -j 4
#make install

#cd
#cd /home/andsilva/repo/my-setup-linux-dev/
#cat time-terminal.sh >> /home/andsilva/.zshrc

#cd

# texlive
#wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
#tar -xzf install-tl-unx.tar.gz

# get name of the folder
#foldername=$(find . -name 'install-tl*' -type d)
#cd $foldername

#echo "Installing TeXlive..."
#sudo ./install-tl

# hardware architecture
#arch=$(uname --m)

# dropbox
#cd && wget -O - "https://www.dropbox.com/download?plat=lnx.$arch" | tar xzf -
#~/.dropbox-dist/dropboxd &

cd

sudo apt update && sudo apt upgrade -y

sudo apt-get install python3-pip
cd /home/andsilva/repo/my-setup-linux-dev/
# requirements.txt
# Install pre requirements, make the command below:
sudo pip3 install -r requirements.txt

sudo python3.7 -m pip install -r requirements.txt

sudo pip3 install numpy scipy matplotlib ipython scikit-learn pandas pillow
sudo python3.7 -m pip install numpy scipy matplotlib ipython scikit-learn \
pandas notify2 dbus tdpm yfinance html5 requests pyyaml bs4 json beautifulsoup4 \
seaborn statsmodels dash plotly dash-bootstrap-components praw mysql faker \
sklearn cs50 streamlit mglearn

cd

# vim configuration:
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
cp .vimrc $HOME

sudo apt install software-properties-common apt-transport-https
sudo apt install code

cd /home/andsilva/repo/my-setup-linux-dev/
# install extensions visual studio code
# cat extensions.list |% { code --install-extension $_ }

sudo apt-get install dselect
sudo apt-key add repo-keys
sudo dpkg --set-selections < installed-packages
sudo apt-get dselect-upgrade -y

cd

# install anaconda 3
sudo apt install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 \
libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6

wget -P /tmp https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh

sha256sum /tmp/Anaconda3-2020.02-Linux-x86_64.sh

zsh /tmp/Anaconda3-2020.02-Linux-x86_64.sh

source ~/.zshrc

conda update --all

cd

# install go
wget https://golang.org/dl/go1.15.3.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.15.3.linux-amd64.tar.gz

go version

git clone https://github.com/cli/cli.git gh-cli
cd gh-cli
make
sudo mv ./bin/gh /usr/local/bin/

cd

# ZSH
#sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"

#git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# Change your default shell
#chsh -s $(which zsh)

#cd

#rm WaitToSource
