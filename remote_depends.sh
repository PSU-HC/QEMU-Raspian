
# motion setup:
apt-get install ffmpeg libmariadb3 libpq5 libmicrohttpd12
wget https://github.com/Motion-Project/motion/releases/download/release-4.2.2/pi_buster_motion_4.2.2-1_armhf.deb
dpkg -i pi_buster_motion_4.2.2-1_armhf.deb
apt-get install python-pip python-dev libssl-dev libcurl4-openssl-dev libjpeg-dev libz-dev
apt-get install python-pip3
apt-get install python-pillow

# motioneye setup:
pip install motioneye
mkdir -p /etc/motioneye
cp /usr/local/share/motioneye/extra/motioneye.conf.sample /etc/motioneye/motioneye.conf
mkdir -p /var/lib/motioneye
cp /usr/local/share/motioneye/extra/motioneye.systemd-unit-local /etc/systemd/system/motioneye.service
systemctl daemon-reload
systemctl enable motioneye
systemctl start motioneye

# usbip depends:
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