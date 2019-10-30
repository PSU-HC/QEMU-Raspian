from subprocess import Popen
import os
from sys import argv
from time import sleep


def argType():
    try:
        if len(argv) == 2:
            use = True
        elif len(argv) == 1:
            print("\n\nusing default type 'stretchlite': \n \
                supply arg 'stretch' for standard stretch release   \n \
                supply arg 'buster' for standard buster release  \
                \n")
            use = False
        else:
            print('command takes 0 or 1 args!')
            raise SystemExit

    except:
        print('arg error...')
        raise SystemExit
    return use


def bash(cmd):
    Popen(cmd, shell=True, executable='/bin/bash')


# global pb:
vers_pb = "versatile-pb.dtb"
wget_pb = "wget https://github.com/dhruvvyas90/qemu-rpi-kernel/raw/master/versatile-pb.dtb -O versatile-pb.dtb"

buster = dict(
    kern_loc="wget https://github.com/dhruvvyas90/qemu-rpi-kernel/blob/master/kernel-qemu-4.19.50-buster?raw=true -O ",
    kern='kernel-qemu-4.19.50-buster',
    url="wget http://downloads.raspberrypi.org/raspbian/images/raspbian-2019-09-30/",
    zip='2019-09-26-raspbian-buster.zip',
    fs='2019-09-26-raspbian-buster.img',
    qcow='buster.qcow2'
)

stretch = dict(
    kern_loc="wget https://github.com/dhruvvyas90/qemu-rpi-kernel/blob/master/kernel-qemu-4.14.79-stretch?raw=true -O ",
    kern='kernel-qemu-4.14.79-stretch',
    url="wget http://downloads.raspberrypi.org/raspbian/images/raspbian-2019-04-09/",
    zip='2019-04-08-raspbian-stretch.zip',
    fs='2019-04-08-raspbian-stretch.img',
    qcow='stretch.qcow2'
)

stretchlite = dict(
    kern_loc="wget https://github.com/dhruvvyas90/qemu-rpi-kernel/blob/master/kernel-qemu-4.14.79-stretch?raw=true -O ",
    kern='kernel-qemu-4.14.79-stretch',
    url="wget http://downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2018-11-15/",
    zip='2018-11-13-raspbian-stretch-lite.zip',
    fs='2018-11-13-raspbian-stretch-lite.img',
    qcow='stretchlite.qcow2'
)


def main(type):
    command = ' '

    if not os.path.exists(type['qcow']):
        if not os.path.exists(type['fs']):
            if not os.path.exists(type['zip']):
                if not os.path.exists(type['kern']):
                    if not os.path.exists(vers_pb):
                        command += str(wget_pb + ' && ')

                    command += str(type['kern_loc'] + type['kern'] + ' && ')

                command += str(type['url'] + type['zip'] + ' && ')

            command += str(' unzip ' + type['zip'] + ' && ')

        command += str('qemu-img convert -f raw -O qcow2 ' + type['fs'] + ' ' + type['qcow'] + ' && ' +
                       'qemu-img resize ' + type['qcow'] + ' +8G && ')

    command += str("qemu-system-arm -kernel " + type['kern'] +
             " -cpu arm1176 -m 256 -M versatilepb " +
             " -dtb " + 'versatile-pb.dtb ' + "-no-reboot " +
             ' -serial stdio -append "root=/dev/sda2 panic=1 rootfstype=ext4 rw" ' +
             " -hda " + type['qcow'] +
             " -net user -net nic ")

#   print(str('command = ' + command))
    bash(command)
    print('waiting ... ')
    sleep(2)
    print('waiting ... ')
    sleep(2)

    str("sudo qemu-system-arm -kernel " + type['kern'] +
             " -cpu arm1176 -m 256 -M versatilepb " +
             " -dtb " + 'versatile-pb.dtb ' + "-no-reboot " +
             ' -serial stdio -append "root=/dev/sda2 panic=1 rootfstype=ext4 rw" ' +
             " -hda " + type['qcow'] +
             " -net user -net nic & ")


if __name__ == '__main__':

    if not argType():
        type = stretchlite
    else:
        if str(argv[1]) == 'stretch':
            type = stretch
        elif str(argv[1]) == 'stretchlite':
            type = stretchlite
        elif str(argv[1]) == 'buster':
            type = buster
        else:
            print("\n\nERROR: arg must match one of the following release types: \n \
                supply arg 'stretchlite' for standard stretchlite release [default] \n \
                supply arg 'stretch' for standard stretch release  \n \
                supply arg 'buster' for standard buster release  \n")
            raise SystemExit

    main(type)

