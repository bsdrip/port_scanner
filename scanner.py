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

try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f'Port {format(port)} is open')
        s.close()
except KeyboardInterrupt:
    print("\nInterrupted")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Couldn't connect to server.")
    sys.exit()
