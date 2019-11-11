#!/bin/sh

# run as admin prior to brctl.sh

apt install bridge-utils -y
apt install uml-utilities -y

sleep .5
ip link add br0 type bridge
sleep .5
ip link set eth0 master br0
sleep .5
echo 'finished public bridge br0 setup'