#!/usr/bin/python2.7
import sys
import socket

UDP_IP = "127.0.0.1"
TX_PORT = 5555
print "UDP target IP:", UDP_IP
print "UDP TX Port:", TX_PORT

while True:
    if len(sys.argv) > 1:
	    msg = sys.argv[1]
	    print("MESSAGE = sys.argv[1]:",str(sys.argv[1]))
    else:
	    msg = raw_input("enter your message:")
    print "Transmitting Message:", msg
    msg = msg+"\n"
    msg_snd = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    msg_snd.sendto(msg, (UDP_IP, TX_PORT))


    RX_PORT = 5557
    msg_lstn = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    msg_lstn.bind((UDP_IP, RX_PORT))
    ack_rxd = 0
    while ack_rxd==0:
        print "UDP RX Port:", RX_PORT
        print "in rx mode"
        ack, addr = msg_lstn.recvfrom(1024) # buffer size is 1024 bytes
        print "Full Received Ack:", ack
        if ack:
            ack_rxd = 1
        print "stripping header"
        scan_len = 6
        start = 0        
        stop = start+scan_len
        if ack:
            ack_rxd = 1       
        for char in ack:
            #print "ack[start:stop]: %s" % ack[start:stop]
            if ack[start:stop] == "pid=F0":
                print "found 'pid=F0'"
                print "extracted ack:%s" % ack[start+scan_len:len(ack)]
                break
            else:
                start+=1
                stop+=1
