#!/bin/bash

num=$1

if [ $2 == enable ]
then
python albatros_usb_mux_cmdline.py s $num
python albatros_usb_mux_cmdline.py p 1
python albatros_usb_mux_cmdline.py m 1

elif [ $2 == disable ]
then
python albatros_usb_mux_cmdline.py m 0
python albatros_usb_mux_cmdline.py p 0
fi
