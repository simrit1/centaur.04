import sys

colors = True
machine = sys.platform # Detecting the os
if machine.lower().startswith(("os", "win", "darwin","ios")): 
    colors = False # Colors will not be displayed

if not colors:
	reset = red = white = yellow = brightred = ""

else:                                                 
    white = "\033[97m"
    red = "\033[91m"                                  
    yellow = "\033[93m"
    reset = "\033[0m"
    brightred = "\033[31;1m"
