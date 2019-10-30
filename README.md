# USBoN

*Serial over Network Plugin for Octoprint*

***Please see /qemu_env for ARM Raspian emulation!***

*remote setup:*
```bash
# install depends:
pip3 install Requests
sudo apt-get install usbip
# nohup usbipd &  # starts daemon, this is run from the python script 

# move files to destinations:
cp Py3_client.py ~
sudo cp client.service /etc/systemd/client.service

# start systemd service:
sudo systemctl daemon-reload
sudo systemctl enable client.service

# reboot for changes to take effect:
sudo reboot
```

*server setup:*  
```bash
# install depends:
sudo apt-get install linux-tools-generic
sudo modprobe vhci-hcd
python3 Py3_server.py
```

***Status***        

Intended for remote Pi Zeros (raspian + motioneye) installed around our facility.     
A central server manages motioneye streams, OctoPrint, job slicing, etc.    

Serial device (e.g. 3d printer) connected to a remote client is mounted on the server using the Debian usbip package.       

As of 10/28/19, scripts / functions have yet to be merged into the OctoPrint plugin scaffold. 