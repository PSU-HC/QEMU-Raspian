#!/bin/sh

# if interfaces has been reset -

/etc/init.d/networking restart 

sleep 1

ip link add br0 type bridge

# vbox enp0s3 nic type

ip link set enp0s3 master br0


# explicit ifup:
# -device e1000,netdev=net0,mac=$macaddress 
# -netdev tap,id=net0,script=/path/to/qemu-ifup
