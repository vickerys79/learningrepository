# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import socket

host ='localhost'
port = 8080

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host,port))

sock.listen(1)

print ("The server is running")

conn,address = sock.accept()

try:
    filename = conn.recv(1024)
    file = open(filename,'rb')
    readfile = file.read()
    conn.send(readfile)
    
    file.close()
except:
    conn.send('file not found on the server'.encode())
    
conn.close()



