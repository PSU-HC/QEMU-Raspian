#!/bin/bash

# ARM Raspian Buster on Mac OSX (tested on 10.14.6) using QEMU
#
# QEMU is a prerequisite- ``` brew install qemu ```
#
# adapted from user tinjaw's post @ https://gist.github.com/hfreire/5846b7aa4ac9209699ba

# global exports:
export QEMU=$(which qemu-system-arm)
export TMP_DIR=~/tmp/qemu-rpi
export PTB_FILE=${TMP_DIR}/versatile-pb.dtb

# buster exports:
export B_RPI_KERNEL=${TMP_DIR}/kernel-qemu-4.19.50-buster
export B_RPI_FS=${TMP_DIR}/2019-09-26-raspbian-buster-lite.img
export B_IMAGE_FILE=2019-09-26-raspbian-buster-lite.zip
export B_IMAGE=http://downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2019-09-30/${B_IMAGE_FILE}
export B_QCOW=buster.qcow2

# stretch exports:
export S_RPI_KERNEL=${TMP_DIR}/kernel-qemu-4.14.79-stretch
export S_RPI_FS=${TMP_DIR}/2018-11-13-raspbian-stretch-lite.img
export S_IMAGE_FILE=2018-11-13-raspbian-stretch-lite.zip
export S_IMAGE=http://downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2018-11-15/${S_IMAGE_FILE}
export S_QCOW=stretch.qcow2

mkdir -p $TMP_DIR; cd "$TMP_DIR"

if [ ! -f "$B_RPI_KERNEL" ]; then
	wget https://github.com/dhruvvyas90/qemu-rpi-kernel/blob/master/kernel-qemu-4.19.50-buster?raw=true \
	    	-O ${B_RPI_KERNEL}

	wget https://github.com/dhruvvyas90/qemu-rpi-kernel/raw/master/versatile-pb.dtb \
	    	-O ${PTB_FILE}
fi

if [ ! -f "$B_IMAGE" ]; then
	wget $B_IMAGE
	unzip $B_IMAGE_FILE
fi

if [ ! -f "$B_QCOW" ]; then
	qemu-img convert -f raw -O qcow2 $B_RPI_FS $B_QCOW
	qemu-img resize $B_QCOW +4G
fi

$QEMU -kernel ${B_RPI_KERNEL} \
	-cpu arm1176 -m 256 -M versatilepb \
	-dtb ${PTB_FILE} -no-reboot \
	-serial stdio -append "root=/dev/sda2 panic=1 rootfstype=ext4 rw" \
	-hda $B_QCOW \
	-net user -net nic \
