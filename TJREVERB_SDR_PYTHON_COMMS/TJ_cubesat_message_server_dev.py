#!/usr/bin/python2.7
import socket
import sys
import select
import time

UDP_IP = "127.0.0.1"
print "UDP target IP:", UDP_IP
if len(sys.argv) < 2:
    print"YOU CAN ENTER UDP PORTS AS ARGUMENTS"
    print"PORT RANGE IS: 5500-5599"
    print"ARG1 = UDP TX PORT, ARG2 = UDP RX PORT" 
startup = 0
while startup == 0:
    if len(sys.argv) >= 2:
        TX_PORT = int(sys.argv[1])
        RX_PORT = int(sys.argv[2])
        if (RX_PORT>=5500 and RX_PORT<=5599) and (TX_PORT>=5500 and TX_PORT<=5599):
            startup = 1
            print "valid port numbers TX:%d RX:%d" % (TX_PORT,RX_PORT)
        else:
            startup = 0
            print "invalid port number"
    elif len(sys.argv) == 1:
        print("BTW, you can enter the TX and RX port #'s as arguments")
        TX_PORT = int(raw_input("enter TX port number(5500-5599)>>"))
        RX_PORT = int(raw_input("enter RX port number(5500-5599)>>"))
        if (RX_PORT>=5500 and RX_PORT<=5599) and (TX_PORT>=5500 and TX_PORT<=5599):
            startup = 1
            print("valid port number (5500-5599)")
        else:
            print "invalid port number"
            startup = 0
    else:
        print("you need a (valid) port number (5500-5599)")
        startup = 0
print "%"*80+"\n"+"%"*80
print "WELCOME TO TJ REVERB CUBESAT MESSAGE SERVER"
print "UDP target IP:", UDP_IP
print "UDP RX port:", RX_PORT
print "UDP TX port:", TX_PORT
send_address = (UDP_IP, TX_PORT) # Set the address to send to
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # Create Datagram Socket (UDP)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Make Socket Reusable
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) # Allow incoming broadcasts
s.setblocking(False) # Set socket to non-blocking mode
s.bind(('', RX_PORT)) #Accept Connections on port
print "Accepting connections on port", RX_PORT
beacon_intvl = 10.0
bcn_num = 0
msg_num = 0
timer = time.time()+beacon_intvl
print "beacon interval set to: ", beacon_intvl
while 1:
    msg_back = False
    msg = False
    try:
        msg, address = s.recvfrom(1024) # Change buffer as needed
    except:
        pass
    if msg:
        print "%"*80+"\n"
        print "Complete Received Message from Groundstation:", msg
        print "%"*80+"\n"
        print "begin delimiter search"
        delimiter = "pid=F0"
        scan_len = len(delimiter)   
        if delimiter in msg:
            indx = msg.find(delimiter)+scan_len
            srchstr = msg[indx:len(msg)]
            print "found delimiter:", delimiter
            print "extracted message from groundstation:%s" % srchstr
            if "hello_tj" in srchstr:
                msg_back = "hello_groundstation_my_time_is:%s" % time.strftime("%a%d%b%Y%H:%M:%S", time.gmtime())
                s.sendto(msg_back+' ', send_address)
                print "sent:", msg_back
                msg_num+=1
            elif "get_sat_time" in srchstr:
                msg_back = time.strftime("%a%d%b%Y%H:%M:%S", time.gmtime())    
                s.sendto(msg_back+' ', send_address)
                print "sent:", msg_back
                msg_num+=1
            elif "noop" in srchstr:
                msg_back = "noop"
                s.sendto(msg_back+' ', send_address)
                print "sent:", msg_back
                msg_num+=1
            else:#no set message, just send back whatever was rx'd 
                msg_back = srchstr
                s.sendto(msg_back+' ', send_address)
                print "sent reply to groundstation:", msg_back
                msg_num+=1
        else:
            "no delimiter found"
#if theres no message present and it's time (or past time) send a beacon
    elif time.time() >= timer:
        beacon = "BEACON TIME:%s" % time.strftime("%a%d%b%Y%H:%M:%S", time.gmtime())
        s.sendto(beacon+' ', send_address)
        print "sent beacon#:%d with content:%s" % (bcn_num,beacon)
        bcn_num+=1
        timer = time.time()+beacon_intvl #reset beacon timer
    else:
        "nothing to do"
