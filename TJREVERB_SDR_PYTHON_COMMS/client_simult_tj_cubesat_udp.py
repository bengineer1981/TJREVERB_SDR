#!/usr/bin/python2.7
import sys
import socket

UDP_IP = "127.0.0.1"
print "UDP target IP:", UDP_IP

startup = 0
while startup == 0:
    if len(sys.argv) == 3:
        TX_PORT = int(sys.argv[1])
        RX_PORT = int(sys.argv[2])
        print "you entered TX port: %d and RX port: %d as arguments" % (TX_PORT,RX_PORT)
        if (RX_PORT>=5500 and RX_PORT<=5599) and (TX_PORT>=5500 and TX_PORT<=5599):
            startup = 1
            print "valid port numbers TX:%d RX:%d" % (TX_PORT,RX_PORT)
        else:
            startup = 0
            print "invalid port number"
    elif len(sys.argv) == 2:
        print("FYI, you can enter the TX and RX port #'s as arguments")
        TX_PORT = int(raw_input("enter TX port number(5500-5599)>>"))
        RX_PORT = int(raw_input("enter RX port number(5500-5599)>>"))
        if (RX_PORT>=5500 and RX_PORT<=5599) and (TX_PORT>=5500 and TX_PORT<=5599):
            startup = 1
            print("valid port number (5500-5599)")
    elif len(sys.argv) == 4:
        TX_PORT = int(sys.argv[1])
        RX_PORT = int(sys.argv[2])
        msg = (str(sys.argv[3]))        
        print "you entered TX port: %d, RX port: %d and message %s as arguments" % (TX_PORT,RX_PORT,sys.argv[3])
        if (RX_PORT>=5500 and RX_PORT<=5599) and (TX_PORT>=5500 and TX_PORT<=5599):
            startup = 1
            print("valid port numbers")
        else:
            print "invalid port numbers (port range is 5500-5599)"
            startup = 0

        
    else:
        print("you need a (valid) port number (5500-5599)")
        startup = 0
    
initial = 1
exit = 0
print "%"*80+"\n"+"%"*80
if len(sys.argv) > 3:
    print "WELCOME TO TJ REVERB GROUNDSTATION COMMUNICATOR"
    print "MESSAGE = sys.argv[3]:",str(sys.argv[3])
else:
    print "WELCOME TO TJ REVERB GROUNDSTATION COMMUNICATOR"
    print "type anything you want, but preset commands you can use are:\n'hello_tj'\n'get_sat_time'\n'noop'"
while True:
    if msg:
        print 'theres already a message'
    else:
	    msg = raw_input("enter your message:")
    print "Transmitting Message:", msg
#    test_delim = "pid=F0" #use this for testing when there is no header
#    msg = test_delim+msg  #add fake delimiter to msg
    msg_snd = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    msg_snd.sendto(msg+" ", (UDP_IP, TX_PORT))


##### RECEIVED MESSAGE FROM CUBESAT #####
    msg_lstn = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    msg_lstn.bind((UDP_IP, RX_PORT))
    ack_rxd = 0
    while ack_rxd==0:
        print "UDP RX Port:", RX_PORT
        print "in rx mode"
        ack, addr = msg_lstn.recvfrom(1024) # buffer size is 1024 bytes
        print "Full Received Reply from Cubesat:", ack
        if ack:
            ack_rxd = 1
        print "begin delimiter search"
        delimiter = "pid=F0"
        scan_len = len(delimiter)
        start = 0        
        stop = start+scan_len
        if ack:
            ack_rxd = 1       
        for char in ack:
            #print "ack[start:stop]: %s" % ack[start:stop]
            if ack[start:stop] == delimiter:
                print "found delimiter: %s",delimiter
                print "extracted reply from cubesat:%s" % ack[start+scan_len:len(ack)]
                break
            else:
                #print "no delimiter found yet"
                start+=1
                stop+=1
        print "end of message"
