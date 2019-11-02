# depends:
apt-get install python-pip3 -y
apt-get install python-pillow -y
apt-get install python-pip python-dev libssl-dev libcurl4-openssl-dev libjpeg-dev libz-dev -y
pip install requests
pip3 install requests
apt-get install linux-tools-generic
modprobe usbip_host

apt-get install ffmpeg libmariadb3 libpq5 libmicrohttpd12 -y
wget https://github.com/Motion-Project/motion/releases/download/release-4.2.2/pi_buster_motion_4.2.2-1_armhf.deb
dpkg -i pi_buster_motion_4.2.2-1_armhf.deb

# motioneye setup:
pip install motioneye
mkdir -p /etc/motioneye
cp /usr/local/share/motioneye/extra/motioneye.conf.sample /etc/motioneye/motioneye.conf
mkdir -p /var/lib/motioneye
cp /usr/local/share/motioneye/extra/motioneye.systemd-unit-local /etc/systemd/system/motioneye.service
systemctl daemon-reload
systemctl enable motioneye
systemctl start motioneye

# move files to destinations:
cp Py3_client.py ~
cp client.service ~/lib/systemd/system/

# start systemd service:
sudo systemctl daemon-reload
sudo systemctl enable client.service

# reboot for changes to take effect:
sudo reboot