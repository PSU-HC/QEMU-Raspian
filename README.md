# Using QEMU for Raspian ARM

*tested on Mac OSX 10.14.6*

Emulates a variety of Raspian releases on proper ARM hardware with QEMU.  

***Prerequisites:***    

QEMU and wget (OSX homebrew)

```bash
brew install qemu wget
```      

Get the Python3 CLI in this repo:
```bash
wget https://raw.githubusercontent.com/Jesssullivan/USBoN/master/QEMU_Raspian.py
```     

- - -
***Usage:***               

After the first launch, it will launch from the persistent .qcow2 image.         

With no arguments & in a new folder, Raspian "stretch-lite" (no desktop environment) will be:        
    - downloaded as a zip archive with a release kernel      
    - unarchived --> to img      
    - converted to a Qcow2 with 8gb allocated as disk        
    - launched from Qcow2 as administrator       
     
```bash
sudo python3 QEMU_Raspian.py 
```             
 
***Optional Arguments:***       
    
-  ``` -h ```  prints CLI usage help         
- ``` -rm ``` removes ALL files added in dir with QEMU_Raspian.py        
- ``` stretch ``` uses standard graphical stretch release with GUI        
- ```stretchlite ``` for stretchlite release [default!]          
- ``` buster ``` for standard graphical buster release [YMMV]     
- ```busterlite``` for busterlite release [YMMV]            
    
```bash
# examples:
sudo python3 QEMU_Raspian.py busterlite
python3 QEMU_Raspian -h  # print help
```
- - -     
***Burn as .img:***        

to burn the new image back to an SD card for a hardware Pi:     

```bash
qemu-img convert -f qcow2 -O raw file.qcow2 file.img
```     

- - -

![Alt text](imgs.png?raw=true)
