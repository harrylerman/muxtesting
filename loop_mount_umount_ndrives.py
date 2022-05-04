import muxtools
import time
import subprocess
import os

def lprint(logfile=None,*args,**kwargs):
    mystr=''
    for arg in args:
        if len(mystr)>0:
            mystr=mystr+' '
        if isinstance(arg,str):
            mystr=mystr+arg
        else:
            mystr=mystr+repr(arg)
    print(mystr)
    if not(logfile is None):
        logfile.write(mystr+'\n')
        logfile.flush()
    


dt=1
muxtools.init_mux()
time.sleep(dt)
muxtools.poweren(0)
time.sleep(dt)
muxtools.muxen(0)
time.sleep(dt)
muxtools.select_drive(0)
time.sleep(dt)
muxtools.poweren(1)
time.sleep(dt)
#diskid='sda2'
diskid='sda1'
ndrives=2
iter=0
timeout=60
while (1):
    for i in range(ndrives):
        #drv=i+8
        muxtools.select_drive(i)
        time.sleep(dt)
        muxtools.poweren(1)
        time.sleep(dt)
        muxtools.muxen(1)
        time.sleep(dt)
        isthere=False
        t0=time.time()
        while isthere==False:
            if (time.time()-t0)>timeout:
                print('timing out on drive mount.  exiting...')
                exit(1)
            lsblk=subprocess.check_output(['lsblk']).decode('utf-8')
            if diskid in lsblk:
                isthere=True
                print('Found drive')
            else:
                time.sleep(dt)
        time.sleep(dt)
        df=subprocess.check_output(['df']).decode('utf-8')
        if not(diskid in df):
            os.system('sudo mount /dev/sda1 /media/pi/MARS3')
            time.sleep(dt)
        df=subprocess.check_output(['df']).decode('utf-8')
        if not(diskid in df):
            print("Um, disk ",i," should have showed up in df, but it did not .")
        else:
            os.system('sudo  eject /dev/'+diskid)
            time.sleep(dt)
            os.system('sudo udisksctl power-off -b /dev/sda')
            time.sleep(dt)
            lsblk=subprocess.check_output(['lsblk']).decode('utf-8')
            if diskid in lsblk:
                print("oddness.  Drive ",i," should be gone, but shows up in lsblk.")
            else:
                iter=iter+1
                print("successfully completed mount iteration ",iter," using drive ",i)
                muxtools.muxen(0)
                time.sleep(dt)
                muxtools.poweren(0)
                time.sleep(dt)
