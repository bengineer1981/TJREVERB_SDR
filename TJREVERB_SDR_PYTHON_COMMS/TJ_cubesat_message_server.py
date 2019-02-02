#!/usr/bin/python2.7
import sys
import socket
import time
UDP_IP = "127.0.0.1"
print "UDP target IP:", UDP_IP
startup = 0
while startup == 0:
    if len(sys.argv) > 2:
        RX_PORT = int(sys.argv[1])
        TX_PORT = int(sys.argv[2])
        if (RX_PORT>=5500 and RX_PORT<=5599) and (TX_PORT>=5500 and TX_PORT<=5599):
            startup = 1
            print "valid port numbers RX:%d TX:%d" % (RX_PORT,TX_PORT)
        else:
            startup = 0
            print "invalid port number"
    elif len(sys.argv) == 1:
        print("BTW, you can enter the RX and TX port #'s as arguments")
        RX_PORT = int(raw_input("enter RX port number(5500-5599)>>"))
        TX_PORT = int(raw_input("enter TX port number(5500-5599)>>"))
        if (RX_PORT>=5500 and RX_PORT<=5599) and (TX_PORT>=5500 and TX_PORT<=5599):
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
print "UDP RX port:", RX_PORT
print "UDP TX port:", TX_PORT

#BUILD RX SOCKET
msg_lstn = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
msg_lstn.bind((UDP_IP, RX_PORT))
msg_count = 0
while True:
    msg_rxd = 0
    while msg_rxd==0:
        print "listening for new message"
        msg, addr = msg_lstn.recvfrom(1024) # buffer size is 1024 bytes
        print "%"*80+"\n"+"%"*80
        print "Complete Received Message from Groundstation:", msg
        print "%"*80+"\n"+"%"*80
        print "begin delimiter search"
        delimiter = "pid=F0"
        scan_len = len(delimiter)
        start = 0        
        stop = start+scan_len
        if msg:
            msg_rxd = 1      
        for char in msg:#scan through message and find end of APRS header
            if msg[start:stop] == delimiter:
                print "found delimiter: %s" % delimiter
                print "%"*80+"\n"+"%"*80
                print "extracted message from groundstation:%s" % msg[start+scan_len:len(msg)]
                print "%"*80+"\n"+"%"*80
                if "hello_tj" in msg:
                    msg_back = "hello_groundstation_my_time_is:%s" % time.strftime("%a%d%b%Y%H:%M:%S", time.gmtime())
                    break
                elif "get_sat_time" in msg:
                    msg_back = time.strftime("%a%d%b%Y%H:%M:%S", time.gmtime())    
                    break
                elif "noop" in msg:
                    msg_back = "noop"
                    break
                else:#no set message, just send back whatever was rx'd 
                    msg_back = msg[start+scan_len:len(msg)]
                    break
            else:
                #print "no delimiter found yet"
                start+=1
                stop+=1
    print "UDP target port:", TX_PORT
    msg_snd = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    msg_snd.sendto(msg_back+" ", (UDP_IP, TX_PORT))
    print "echo '%s' sent" % msg_back
    msg_rxd = 0#reset flag to listen for more messages
    msg = False#reset msg value for 'if msg' condition
