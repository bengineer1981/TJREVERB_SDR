#!/usr/bin/python2.7
import sys
import socket
import time
UDP_IP = "127.0.0.1"

startup = 0
while startup == 0:
    if len(sys.argv) >= 2:
        RX_PORT = int(sys.argv[1])
        TX_PORT = int(sys.argv[2])
        if (RX_PORT>=5500 and RX_PORT<=5599):
            startup = 1
            print "valid port numbers RX:%d TX:%d" % (RX_PORT,TX_PORT)
        else:
            startup = 0
            print "invalid port number"
    elif len(sys.argv) == 1:
        print("BTW, you can enter the RX and TX port #'s as arguments")
        RX_PORT = int(raw_input("port number(5500-5599)>>"))
        if (RX_PORT>=5500 and RX_PORT<=5599):
            startup = 1
            print("valid port number (5500-5599)")
        else:
            print "invalid port number"
            startup = 0
    else:
        print("you need a (valid) port number (5500-5599)")
        startup = 0
    
initial = 1
exit = 0
print "%"*80+"\n"+"%"*80
print "WELCOME TO TJ REVERB CUBESAT MESSAGE SERVER"

print "UDP target IP:", UDP_IP
print "UDP target port:", RX_PORT
    
msg_lstn = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
msg_lstn.bind((UDP_IP, RX_PORT))

while True:
    msg_rxd = 0
    while msg_rxd==0:
        msg, addr = msg_lstn.recvfrom(1024) # buffer size is 1024 bytes
        print "%"*80+"\n"+"%"*80
        print "Complete Received Message:\n", msg
        print "%"*80+"\n"+"%"*80
        print "stripping header"
        scan_len = 6
        start = 0        
        stop = start+scan_len
        if msg:
            msg_rxd = 1      
        for char in msg:
            if msg[start:stop] == "pid=F0":
                if "\n" in msg:
                    msg.replace("\n","")
                else:
                    continue
                print "found 'pid=F0'"
                print "%"*80+"\n"+"%"*80
                print "extracted message:%s" % msg[start+scan_len:len(msg)]
                print "%"*80+"\n"+"%"*80
                if msg == "hello_tj":
                    msg_back = "hello_groundstation_my_time_is:%s" % strftime("%a%d%b%Y%H:%M:%S", gmtime())
                    break
                elif msg == "get_time":
                    msg_back = strftime("%a%d%b%Y%H:%M:%S", gmtime())    
                    break
                elif msg == "noop":
                    msg_back = "noop"
                else:
                    msg_back = msg[start+scan_len:len(msg)]
                    break
            else:
                start+=1
                stop+=1

    print "UDP target port:", TX_PORT
    msg_snd = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    msg_snd.sendto(msg_back, (UDP_IP, TX_PORT))
    print "echo sent"
    msg_rxd = 0
    msg = False
