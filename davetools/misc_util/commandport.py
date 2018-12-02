#! /usr/bin/env python
# -*- coding: utf-8 -*-
# fileName : commandPort.py
import socket
#HOST = '192.168.1.122'	# The remote host
HOST = '127.0.0.1'	# the local host
PORT = 6000	# The same port as used by the server
ADDR=(HOST,PORT)

def SendCommand():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    command = 'cmds.polyCube()'	# the commang from external editor to maya
    MyMessage = command
    client.send(MyMessage)
    data = client.recv(1024)	#receive the result info
    client.close()
    print 'The Result is %s'%data



if __name__=='__main__':
    SendCommand()

