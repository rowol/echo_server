#!/usr/bin/env python 
#
# A simple echo server 
#

import getopt, socket, sys, threading 


def server_thread(client):
    while 1: 
        data = client.recv(size) 
        if data: 
            client.send(data) 
        else: 
            client.close()
            break





host = '' 
port = 50003       #Default port
backlog = 5 
size = 1024 

try:
    opts, args = getopt.getopt(sys.argv[1:], "p:")
except getopt.GetoptError:
    print('%s [-p port]' % sys.argv[0])
    sys.exit(2)

for opt, arg in opts:
    if opt == '-p':
        port = int(arg)
print 'Running server on port', port

# Listen for inbound socket connections
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port)) 
s.listen(backlog) 

# Whenever there's a connection, accept it, and run it in a new background thread
# Kill off server threads in case of ^C, etc
try:
    while 1:
        client, address = s.accept() 
        thread = threading.Thread(target = server_thread, args = (client,))
        thread.start()
except:  
    sys.exit("Server killed by user")




