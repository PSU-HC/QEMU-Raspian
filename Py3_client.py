"""
# Send IP address to OctoPrint server
# WIP by Jess Sullivan
#
# destinations:
# /home/pi/Py3_client.py
# /lib/systemd/system/client.service
"""
import requests
import socket
from time import sleep
from subprocess import Popen

verbose = False  # use prints to console?  motioneye remotes are likely headless / self sufficient

addr = '127.0.0.1'  # OctoPrint Server / static address to send ip to
port = 8888  # must match server

hostname = socket.gethostname()
myIP = socket.gethostbyname(hostname)

# start usbip daemon:
Popen('nohup usbipd &',
      shell=True,
      executable='/bin/bash')

# bind the only usb bus on Pi Zero to usbip:
Popen('usbip unbind -b 1-1 && sleep 1 && usbip bind -b 1-1',
      shell=True,
      executable='/bin/bash')


# send ip address to server:

received = bool

while not received:

    # POST request sent as JSON:
    res = requests.post(str('http://' + addr + ':' + str(port) + '/'), json={"ip": myIP})

    if res.status_code == 200:
        if verbose:
            print(str('Successfully sent IP to http server! \nMy IP is: ' + myIP))

        received = True

    else:
        sleep(2)
