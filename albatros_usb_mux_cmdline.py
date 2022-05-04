# -*- coding: utf-8 -*-
"""
Created on Sun May  2 11:11:15 2021

@author: eamon
"""

import sys
import albatros_usb_mux as mux

# Help text
USAGE = """Usage:
	s n, 0 <= n <= 15, select drive n
	p n, n = 0 or 1, set power enable to 0 (off) or 1 (on)
	m n, n = 0 or 1, set mux enable to 0 (off) or 1 (on)"""

# require two parameters 
if len(sys.argv) > 2 :
	cmd = sys.argv[1]
	try:
		arg = int(sys.argv[2])
	except ValueError:
		print (USAGE)
		quit()

else:
	print (USAGE)
	quit()

# mux = albatros_USB_mux()

if cmd == 's': # select
	if (arg < 0 or arg > 15):
		print (USAGE)
	else: # we in business
		mux.select(arg)

elif cmd == 'p': # power enable
	if (arg < 0 or arg > 1):
		print (USAGE)
	else:
		mux.power(arg)

elif cmd == 'm': # mux enable
	if (arg < 0 or arg > 1):
		print (USAGE)
	else:
		mux.enable(arg)
else:
	print (USAGE)
	quit()
