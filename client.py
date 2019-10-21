"""
# serial over network plugin for OctoPrint
#
# WIP by Jess Sullivan
#
# systemd ideas adapted from https://derushadigital.com/other%20projects/2019/02/19/RPi-USBIP-ZWave.html
"""
import subprocess
import time

addr = '192.168.8.1'
service_type = 'client'  # must be 'client' OR 'server'
usbid = ''


def lsusb():
    return str(subprocess.Popen(['lsusb'],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT).stdout.read()).split('ID ')


def usb_waiter():
    start_devices = []
    new_devices = []

    for device in lsusb():
        start_devices.append(device[0:8])

    while len(lsusb()) <= len(start_devices):
        time.sleep(1)
        print('waiting for new serial device...')

    for device in lsusb():
        new_devices.append(device[0:8])

    new = str(set(new_devices) - set(start_devices)).strip("'}{ ")

    return new


""" Client Service: """

C_ExecStart = str('/bin/sh -c "/usr/lib/linux-tools/$(uname -r)/usbip attach -r ' +
                  addr + ' -b $(/usr/lib/linux-tools/$(uname -r)/usbip list -r ' + addr +
                  ' grep ' + usbid + ' | cut -d: -f1)')

C_ExecStop = str('/bin/sh -c "/usr/lib/linux-tools/$(uname -r)/usbip detach ' +
                 '--port=$(/usr/lib/linux-tools/$(uname -r)/usbip port ' +
                 'grep "<Port in Use>" ' + str(' sed -E "s/^Port ([0-9][0-9]).*/\\1/'))

C_contents = str('[Unit] \n' +
                 'Description=octo_usbip \n' +
                 'After=network.target \n\n' +
                 '[Service] \n' +
                 'Type=oneshot \n' +
                 'RemainAfterExit=yes \n' +
                 'ExecStart=' + C_ExecStart + '\n' +
                 'ExecStop=' + C_ExecStop + '\n\n' +
                 '[Install] \n' +
                 'WantedBy=multi-user.target \n')

""" Server Service: """

S_ExecStart = 'ExecStart=/usr/sbin/usbipd -D'

S_ExecStartPost = str('/bin/sh -c "/usr/sbin/usbip bind --$(/usr/sbin/usbip list -p -l' +
                      "grep '#usbid=" + usbid + "#'" + "cut '-d#' -f1)")

S_ExecStop = str('/bin/sh -c "/usr/sbin/usbip unbind --$(/usr/sbin/usbip list -p -l ' +
                 "grep '#usbid=" + usbid + "#'" + "cut '-d#' -f1`); killall usbipd")

S_contents = str('[Unit] \n' +
                 'Description=octo_usbip \n' +
                 'After=network.target \n\n' +
                 '[Service] \n' +
                 'Type=forking \n' +
                 'RemainAfterExit=yes \n' +
                 'ExecStart=' + S_ExecStart + '\n' +
                 'ExecStartPost=' + S_ExecStartPost + '\n' +

                 'ExecStop=' + S_ExecStop + '\n\n' +
                 '[Install] \n' +
                 'WantedBy=multi-user.target \n')


def writer():
    f = open(str(service_type + '.service'), "w")
    if service_type == 'client':
        f.write(C_contents)
    else:
        f.write(S_contents)
    f.close()
