#!/usr/bin/python2.7
import socket
import time
UDP_IP = "127.0.0.1"
RX_PORT = 5556
print "UDP target IP:", UDP_IP
print "UDP target port:", RX_PORT
msg_lstn = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
msg_lstn.bind((UDP_IP, RX_PORT))

while True:
    msg_rxd = 0
    while msg_rxd==0:
        msg, addr = msg_lstn.recvfrom(1024) # buffer size is 1024 bytes
        print "Full Received Message:", msg
        print "stripping header"
        scan_len = 6
        start = 0        
        stop = start+scan_len
        if msg:
            msg_rxd = 1      
        for char in msg:
            if msg[start:stop] == "pid=F0":
                print "found 'pid=F0'"
                print "extracted message:%s" % msg[start+scan_len:len(msg)]
                msg_back = msg[start+scan_len:len(msg)]
                break
            else:
                start+=1
                stop+=1
    print "in TX mode"
    TX_PORT = 5558
    print "UDP target IP:", UDP_IP
    print "UDP target port:", TX_PORT
    msg_snd = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    msg_snd.sendto(msg_back, (UDP_IP, TX_PORT))
    print "echo sent"
