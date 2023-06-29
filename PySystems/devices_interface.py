from serial.tools import list_ports

# todo scan ports for any containing arduinos
#       add them to a list of connected devices, tell the
#       arduino what device it is based on port
#       need device objects to store that information.h
import serial
ports = serial.tools.list_ports.comports()

# This should list all of the COM ports and what are attached to them
for port, desc, hwid in sorted(ports):
        print(ports)
        print("{}: {} [{}]".format(port, desc, hwid))