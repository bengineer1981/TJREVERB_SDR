#!/usr/bin/python2.7
import socket
import sys
import select
import time

# Read a line. Using select for non blocking reading of sys.stdin
def getLine():
    i,o,e = select.select([sys.stdin],[],[],0.0001)
    for s in i:
        if s == sys.stdin:
            input = sys.stdin.readline()
            return input
    return False

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
msg_num = 0
timer = time.time()+beacon_intvl
print "timer:",timer
while 1:
    msg_back = False
    msg = False
    try:
        msg, address = s.recvfrom(1024) # Change buffer as needed
    except:
        pass
    if msg:
        print "%"*80+"\n"+"%"*80
        print "Complete Received Message from Groundstation:", msg
        print "%"*80+"\n"+"%"*80
        print "begin delimiter search"
        delimiter = "pid=F0"
        scan_len = len(delimiter)   
        if delimiter in msg:
            indx = msg.find(delimiter)
            srchstr = msg[indx:len(msg)]
            print "found delimiter: %s at index:%d" % (delimiter,indx)
            print "%"*80+"\n"+"%"*80
            print "extracted message from groundstation:%s" % srchstr
            print "%"*80+"\n"+"%"*80
            if "hello_tj" in srchstr:
                msg_back = "hello_groundstation_my_time_is:%s" % time.strftime("%a%d%b%Y%H:%M:%S", time.gmtime())
                s.sendto(msg_back+' ', send_address)
                print "sent:", msg_back
            elif "get_sat_time" in srchstr:
                msg_back = time.strftime("%a%d%b%Y%H:%M:%S", time.gmtime())    
                s.sendto(msg_back+' ', send_address)
                print "sent:", msg_back
            elif "noop" in srchstr:
                msg_back = "noop"
                s.sendto(msg_back+' ', send_address)
                print "sent:", msg_back
            else:#no set message, just send back whatever was rx'd 
                msg_back = srchstr
                s.sendto(msg_back+' ', send_address)
                print "sent:", msg_back
        else:
            "no delimiter found"
    elif time.time() >= timer:
        print "ELIF time.time():",time.time()
        print "timer:",timer
        beacon = "BEACON TIME:%s" % time.strftime("%a%d%b%Y%H:%M:%S", time.gmtime())
        s.sendto(beacon+' ', send_address)
        print "beacon:", beacon
        timer = time.time()+beacon_intvl
    else:
        "nothing to do"
