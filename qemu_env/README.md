# Using QEMU for Raspian ARM

*tested on Mac OSX 10.14.6*

Emulates a variety of Raspian releases on proper ARM hardware with QEMU.

***Prerequisites:***    

QEMU and wget on Mac (homebrew):

```bash
brew install qemu wget
```      

Get the Python3 CLI in this repo:
```bash
wget https://raw.githubusercontent.com/Jesssullivan/USBoN/master/qemu_env/QEMU_Raspian.py
```     

Each Pi emulation gets a directory: 
```bash
# make two directories for two rPi emulations:
mkdir p1 
mkdir p2

# copy script into the new directories:
cp QEMU_Raspian.py p1
cp QEMU_Raspian.py p2
cd p1  
``` 

***Usage:***     

With no arguments & in a new folder, Raspian "stretch-lite" (no desktop environment) will be:
    - downloaded as a zip archive with a release kernel
    - unarchived --> to img
    - converted to a Qcow2 with 8gb allocated as disk
    - launched from Qcow2 as administrator 
     
```bash
sudo python3 QEMU_Raspian.py 
```             

After the first launch, ``` sudo python3 QEMU_Raspian.py ```will launch straight from the Qcow2 image.       
Other releases are available as optional arguments:
    - ``` stretch ``` is the standard distribution with the usual GUI, desktop environment, applications, etc
    - ``` buster ``` is buster-lite.
      
```bash
sudo python3 QEMU_Raspian.py stretch  # with GUI
sudo python3 QEMU_Raspian.py buster  # newer release + newer kernel  
```
  
![Alt text](imgs.png?raw=true)
