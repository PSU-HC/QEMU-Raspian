brctl addbr brkvm
ip addr add 192.168.56.101/24 dev brkvm
ip link set brkvm up
mkdir /etc/qemu
touch /etc/qemu/bridge.conf
echo "allow brkvm" >> /etc/qemu/bridge.conf
qemu-system-x86_64 -enable-kvm -m 1024 -kernel ./vmlinuz -initrd ./initramfs.igz -append "console=ttyS0" -nographic -netdev bridge,id=bridge,br=brkvm -device virtio net-pci,netdev=bridge

-net nic,model=virtio,macaddr=54:54:00:55:55:55 \
-net tap,script=../scripts/tap-up,downscript=../scripts/tap-down \


 
ifconfig eth0 0.0.0.0
ifconfig tap0 0.0.0.0
brctl addbr br0
brctl addif br0 eth0
brctl addif br0 tap0

# Configure the bridge via DHCP
dhcpcd br0
# Load firewall rules for br0
/etc/rc.d/rc.firewall_br0
# Activate the kvm-intel kernel module for use by qemu
modprobe kvm-intel