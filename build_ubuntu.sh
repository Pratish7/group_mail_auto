#!/bin/bash
sudo apt install python3-pip
pip3 install pyinstaller
prog_dir=${PWD}
work_dir="/home/$USER/.mail_by_pratish"
mkdir $work_dir
cd $work_dir
pyinstaller $prog_dir/main.py
echo -e "[Desktop Entry]
Name=group\ mail
Comment=A short description of the application
Exec='$work_dir/dist/main/main'
Terminal=false
Type=Application
Icon=''" >> ~/.local/share/applications/group\ mail.desktop