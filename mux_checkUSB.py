#!/usr/bin/python
"""
@author: larry
A very simple script to check the RPi USB once per hour.
If the USB controller seems alright, it doesn't do anything.
If the USB controller looks dead, it checks it 5 times with a minute in between checks to be sure, then reboots.
If the USB comes back to life during those checks, it goes back to waiting an hour.
Method used to check the USB controller is detection of the LB. Might be a better way.
"""
import os
import subprocess
import time

def CheckUSB():
    """
    Check the USB status by checking if the LB is readable.
    """
    try:
        subprocess.check_output("lsusb | grep 1dd2", shell=True)
        return True #if the above suprocess command didn't give an error, then it successfully found the LB
    except:
        return False #can't find the LB, USB must be dead

while(True):
    ntry = 5 #if the USB looks dead, check it 5 times before rebooting.
    for i in range(ntry):
        if CheckUSB() is False: #if the USB appears dead
            if i == ntry-1:
                os.system("sudo reboot") #we checked it ntry times with a minute in between, the USB must be dead
            time.sleep(60)
        else:
            break #if CheckUSB returns true, then the USB hasn't crashed or it came back to life so wait an hour and check again
            
    time.sleep(3600)
            