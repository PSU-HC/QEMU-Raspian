#!/usr/bin/env bash

apt-get install linux-tools-generic -y
modprobe vhci-hcd
echo 'vhci-hcd' >> /etc/modules

# reload systemd, enable, then start the service
systemctl --system daemon-reload
systemctl enable usbip.service
systemctl start usbip.service

