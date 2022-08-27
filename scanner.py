#!/bin/python3

import sys
import socket
from datetime import datetime


# define target <ip>
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of arguments.")
    print("syntax: python3 scanner.py <ip>")

# add banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)
