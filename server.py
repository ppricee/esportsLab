from socket import *

def sendping():
    s = socket(AF_INET, SOCK_STREAM) # Create Socket
    host = "localhost"  # IP of workstation
    port = 80

    try:
        s.connect((host, port)) #tries to connect to host
    except ConnectionRefusedError: # failure to connect PC not online
        print("Server Offline")
        s.close()
        sendping() # send ping again

    while True:     #If connection is made
        print("Connected PC is live")
        s.close() #Close socket
        exit()

sendping()