# USBoN

Serial over Network Plugin for Octoprint    

Intended for remote Pi Zeros (raspian + motioneye) installed around our facility.     
A central server manages motioneye streams, OctoPrint, job slicing, etc.    

Serial device (e.g. 3d printer) connected to a remote client is mounted on the server using the Debian usbip package.       

As of 10/28/19, scripts / functions have yet to be merged into the OctoPrint plugin scaffold. 

# Setup:

*remote setup:*
```bash
# install depends:
pip3 install requests
sudo apt-get install linux-tools-generic
sudo modprobe usbip_host
# nohup usbipd &  # starts daemon, this is run from the python script 

# move files to destinations:
cp Py3_client.py ~
cp client.service ~/lib/systemd/system/

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