# -*- coding: utf-8 -*-
"""
Created on Sun May  2 15:41:23 2021

@author: eamon
"""

# hello_world.py

import PySimpleGUI as sg
import albatros_usb_mux as mux

layout =  [
            [sg.Text('Channel'), sg.Spin([i for i in range(0,15)], initial_value=0, enable_events=True, key="channel")],
            [sg.Checkbox("Power on", default=False, enable_events=True, key="power")],
            [sg.Checkbox("Mux enable", default=False, enable_events=True, key="enable")]
        ]

window = sg.Window(title="ALBATROS MUX test", layout=layout, margins=(100, 50));

while True:
    event, values = window.read()
    if event==sg.WIN_CLOSED or event=="Exit":
        break
    v = values[event]
    if event == "channel":
        mux.select(v)
        print("values", v)
    elif event == "power":
        print("power", v)
        mux.power(v)
    elif event == "enable":
        print("enable", v)
        mux.enable(v)
window.close()