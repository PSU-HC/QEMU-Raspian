#!/usr/bin/env bash

apt-get install usbip
modprobe usbip_host
echo 'usbip_host' >> /etc/modules

systemctl --system daemon-reload
systemctl enable server.service
systemctl start server.service
