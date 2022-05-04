# -*- coding: utf-8 -*-
"""
Created on Sun May  2 11:11:15 2021

@author: eamon
"""

# GPIO pin assignments for mux
A0 = 6
A1 = 13
A2 = 19
A3 = 26
MUXEN = 12
PWREN = 16

for_real = True

if for_real:
    import RPi.GPIO as GPIO
    
    # Otherwise, we get warnings when we run it again, on setmode and setup
    GPIO.setwarnings(False)
    
    # use Broadcom pinout
    GPIO.setmode(GPIO.BCM)
    
    # set all pins for digital out
    GPIO.setup(A0, GPIO.OUT)
    GPIO.setup(A1, GPIO.OUT)
    GPIO.setup(A2, GPIO.OUT)
    GPIO.setup(A3, GPIO.OUT)
    GPIO.setup(MUXEN, GPIO.OUT)
    GPIO.setup(PWREN, GPIO.OUT)

    # GPIO values
    gv = (GPIO.LOW, GPIO.HIGH)


def select(chan):
    print ("muxmodule selecting", chan)
    if for_real:
    	GPIO.output(A0, gv[(chan >> 0) & 1])
    	GPIO.output(A1, gv[(chan >> 1) & 1])
    	GPIO.output(A2, gv[(chan >> 2) & 1])
    	GPIO.output(A3, gv[(chan >> 3) & 1])

def power(value):
    print ("muxmodule power", value)
    if for_real:
    	GPIO.output(PWREN, gv[value])

def enable(value):
    print ("muxmodule enable", value)
    if for_real:
    	GPIO.output(MUXEN, gv[value])
