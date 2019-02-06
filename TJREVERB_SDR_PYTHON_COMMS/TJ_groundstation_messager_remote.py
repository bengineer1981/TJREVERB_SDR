#!/usr/bin/python2.7
import socket
import sys, select
 
# Read a line. Using select for non blocking reading of sys.stdin
def getLine():
    i,o,e = select.select([sys.stdin],[],[],0.0001)
    for s in i:
        if s == sys.stdin:
            input = sys.stdin.readline()
            return input
    return False
 
UDP_IP = "192.168.1.10"
print "UDP target IP:", UDP_IP

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

send_address = (UDP_IP, TX_PORT) # Set the address to send to
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # Create Datagram Socket (UDP)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Make Socket Reusable
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) # Allow incoming broadcasts
s.setblocking(False) # Set socket to non-blocking mode
s.bind(('192.168.1.3', RX_PORT)) #Accept Connections on port
print "Accepting connections on port", RX_PORT
print "WELCOME TO TJ REVERB GROUNDSTATION COMMUNICATOR"
print "type anything you want, but preset commands you can use are:\n'hello_tj'\n'get_sat_time'\n'noop'"
while 1:
    msg = False
    try:
        msg, address = s.recvfrom(1024) # Buffer size is 8192. Change as needed.
    except:
        pass
    if msg:
        print "%"*80
        print "Complete Received Message from Cubesat:\n", msg
        print "%"*80
        delimiter = "pid=F0"
        scan_len = len(delimiter)   
        if delimiter in msg:
            indx = msg.find(delimiter)+scan_len
            srchstr = msg[indx:len(msg)]
            print "found delimiter:", delimiter
            print "extracted message from cubesat:%s" % srchstr
            print "%"*80
    input = getLine();
    if(input != False):
        print "sending this message to TJREVERB:",input
        s.sendto(input, send_address)
