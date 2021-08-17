# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 11:17:38 2021

@author: stephen.vickery
"""

import socket

host = 'localhost'
port = 8080

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect((host,port))

filename = 'abc.txt'
sock.send(filename.encode())

ReadFile = sock.recv(1024)

print(ReadFile.decode())

   
sock.close()
