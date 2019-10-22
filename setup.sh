if [ "$1" == 'C' ] ; then

  echo recived "$1" as argument
  echo configuring client...

  apt-get install linux-tools-generic -y
  modprobe vhci-hcd
  echo 'vhci-hcd' >> /etc/modules

  systemctl --system daemon-reload
  systemctl enable client.service
  systemctl start client.service

fi

if [ "$1" != 'C' ] ; then

  echo recived "$1" as argument
  echo configuring server...

  apt-get install usbip
  modprobe usbip_host
  echo 'usbip_host' >> /etc/modules

  systemctl --system daemon-reload
  systemctl enable server.service
  systemctl start server.service

fi