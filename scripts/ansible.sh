#!/usr/bin/env bash

sudo apt-get update

sudo apt-get install python -y

mkdir -p ~/.local/bin

echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc

pip3 install --user ansible

ansible --version

. ~/.bashrc

ansible-playbook -v -i inventory.cfg playbook.yaml