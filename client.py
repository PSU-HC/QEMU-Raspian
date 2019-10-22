"""
# serial over network plugin for OctoPrint
#
# WIP by Jess Sullivan
#
# systemd ideas adapted from https://derushadigital.com/other%20projects/2019/02/19/RPi-USBIP-ZWave.html
"""
from __future__ import absolute_import
import subprocess
import time
from io import open

addr = u'192.168.8.1'
service_type = u'client'  # must be 'client' OR 'server'
usbid = u''


def lsusb():
    return unicode(subprocess.Popen([u'lsusb'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT).stdout.read()).split(u'ID ')


def usb_waiter():
    start_devices = []
    new_devices = []

    for device in lsusb():
        start_devices.append(device[0:8])

    while len(lsusb()) <= len(start_devices):
        time.sleep(1)
        print u'waiting for new serial device...'

    for device in lsusb():
        new_devices.append(device[0:8])

    new = unicode(set(new_devices) - set(start_devices)).strip(u"'}{ ")
    print unicode(u'NEW USB ID IS: ' + new)
    return new


u""" Client Service: """

C_ExecStart = unicode(u'/bin/sh -c "/usr/lib/linux-tools/$(uname -r)/usbip attach -r ' +
                      addr + u' -b $(/usr/lib/linux-tools/$(uname -r)/usbip list -r ' + addr +
                      u' grep ' + usbid + u' | cut -d: -f1)')

C_ExecStop = unicode(u'/bin/sh -c "/usr/lib/linux-tools/$(uname -r)/usbip detach ' +
                     u'--port=$(/usr/lib/linux-tools/$(uname -r)/usbip port ' +
                     u'grep "<Port in Use>" ' + unicode(u' sed -E "s/^Port ([0-9][0-9]).*/\\1/'))

C_contents = unicode(u'[Unit] \n' +
                     u'Description=octo_usbip \n' +
                     u'After=network.target \n\n' +
                     u'[Service] \n' +
                     u'Type=oneshot \n' +
                     u'RemainAfterExit=yes \n' +
                     u'ExecStart=' + C_ExecStart + u'\n' +
                     u'ExecStop=' + C_ExecStop + u'\n\n' +
                     u'[Install] \n' +
                     u'WantedBy=multi-user.target \n')

u""" Server Service: """

S_ExecStart = u'ExecStart=/usr/sbin/usbipd -D'

S_ExecStartPost = unicode(u'/bin/sh -c "/usr/sbin/usbip bind --$(/usr/sbin/usbip list -p -l' +
                          u"grep '#usbid=" + usbid + u"#'" + u"cut '-d#' -f1)")

S_ExecStop = unicode(u'/bin/sh -c "/usr/sbin/usbip unbind --$(/usr/sbin/usbip list -p -l ' +
                     u"grep '#usbid=" + usbid + u"#'" + u"cut '-d#' -f1`); killall usbipd")

S_contents = unicode(u'[Unit] \n' +
                     u'Description=octo_usbip \n' +
                     u'After=network.target \n\n' +
                     u'[Service] \n' +
                     u'Type=forking \n' +
                     u'RemainAfterExit=yes \n' +
                     u'ExecStart=' + S_ExecStart + u'\n' +
                     u'ExecStartPost=' + S_ExecStartPost + u'\n' +

                     u'ExecStop=' + S_ExecStop + u'\n\n' +
                     u'[Install] \n' +
                     u'WantedBy=multi-user.target \n')


def writer():
    f = open(unicode(service_type + u'.service'), u"w")
    if service_type == u'client':
        f.write(C_contents)
    else:
        f.write(S_contents)
    f.close()
