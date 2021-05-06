#!/bin/python3

import socket

HOST = '127.0.0.1'
PORT = 7777
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket.af_inet = ipv4 | socket.sock_stream = the port you are trying to connect to
s.connect((HOST,PORT))


