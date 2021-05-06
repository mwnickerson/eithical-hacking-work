#!/bin/python3
# mwnsec

import sys                           # we are importing the modules we are going to use in our script
import socket
from datetime import datetime as dt #imported a specific function from the datetime module with an alias of "dt" to save time

#define our target 
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translates a host name dirtectly to an ip address
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>") # error statement for if they fail to input proper syntax
	
# add a pretty banner 
print("#" * 50)
print("Scanning target " + target)
print("Time Started: "+str(dt.now()))   # this creates a banner for our script
print("#" * 50)


try:
	for port in range(1,65355):  # we are going to scan ports between 50 and 85
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # connecting to an ipv4 address and a port
		socket.setdefaulttimeout(1)    # here we are creating a default timeout so if it cant connect to the port it doesnt get heldup
		result = s.connect_ex((target,port)) # if this returns a 1 it means port is closed if it returns a 0 port is open  
		# print("Checking port {}".format(port)) #prints checking port while scnaning each port # commented out bc of readability and UI
		if result == 0: 
			print("Port {} is open".format(port))
		#else:
			#print("Port {} is closed".format(port)) 3commented out  the else statement because its annoying to see the closedd ports
			#s.close()

except KeyboardInterrupt:    #if user uses ctrl + c it prints a message and exits the program
	print("\nexiting program.")
	sys.exit()
except socket.gaierror:   #cant reolve the dns leads to exiting the program with error message
	print("hostname could not be resolved")
	sys.exit()
except socket.error:    # cant connect to ip address prints error message and exits the program
	print("Couldnt connect to server.")
	sys.exit()
	
		
