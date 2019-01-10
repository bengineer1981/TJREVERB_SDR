#!/usr/bin/python2.7
import socket
import sys
import time
#APRS HEADER FORMAT:
#2018-12-22.02:51:50 PM
#AFSK1200: fm KN4DTQ-0 to ARISS-0 via WIDE2-2,-0 UI  pid=F0
#message goes here

#establish static message size
#max TX payload size: HDR+MSG+TAIL (in ascii chars)
header_len = 68#ascii chars (header is appended downstream)
max_msg_len = 58#maximum msg size (in ascii chars)
tail_len = 1#at least 1 '#'
payload_len = header_len+max_msg_len+tail_len
msg_cnt = 0

startup = 0
while startup == 0:
    if len(sys.argv) == 2:
        port_num = int(sys.argv[1])
        if (port_num>=5500 and port_num<=5599):
            startup = 1
            print "valid port number"
        else:
            startup = 0
            print "invalid port number"
    elif len(sys.argv) == 1:
        print("BTW, you can enter the port # as an argument")
        port_num = raw_input("port number(5500-5599)>>")
        if (port_num>=5500 and port_num<=5599):
            startup = 1
            print("you need a (valid) port number (5500-5599)")
        else:
            print "invalid port number"
            type(port_num)
            startup = 0
    else:
        print("you need a (valid) port number (5500-5599)")
        startup = 0
    
initial = 1
exit = 0
print "%"*80+"\n"+"%"*80
print "WELCOME TO TJ REVERB GROUNDSTATION COMMUNICATOR"
while True:
    try:
	    
	    # Get/Send data
        if initial == 0:
            print "MAX MESSAGE LENGTH IS: %d CHARS" % max_msg_len
            print "ENTER ANOTHER MESSAGE AND PRESS RETURN"\
            "(or press ENTER to quit)"
        else:
            print "ENTER A MESSAGE AND PRESS RETURN (or press ENTER to quit)"
            initial = 0			
        while True:
            message = raw_input("GROUNDSTATION to TJ REVERB>")
            if (len(message)>1) and (len(message)<max_msg_len):
                break
            elif len(message)==0:
                print "<<exiting program>>"
                exit=1
                break
            else:
                print "message has to be less than"\
                " %d characters" % max_msg_len
        if exit ==1:
            break
        print "len msg: %d" % len(message)
        tail_len = max_msg_len-len(message)
        tail = "#"*tail_len#add tail to confirm end of message
        print "len tail: %d" % len(tail)
        message += (tail+'.') #add the tail and one '.' to the 
                              #message. The '.' will be cut by 
                              #the string to aprs block
        print "size of outoing payload: %d" % len(message)

	    # Connect the socket to the port where the server is listening
        server_address = ('127.0.0.1', port_num)
        print >>sys.stderr, 'connecting to %s port %s' % server_address
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server_address)
        print "%"*80+"\n"+"%"*80
        print >> sys.stderr, "message length is:%d chars\n" % len(message)
        print >> sys.stderr, "message size is:%d bytes\n" % sys.getsizeof(message)
        print >> sys.stderr, "message text is:\n%sEND\n" % message	
        print "%"*80+"\n"+"%"*80	
        sock.sendall(message)
        msg_cnt += 1
        print "msg #: %d" % msg_cnt
        # Look for the response
        pktlen = 127
        amount_received = 0
        amount_expected = pktlen
	    
        while amount_received <= 1024:
            data = sock.recv(1024)
            amount_received += len(data)
            print "length of data received: %d" % len(data)	
            print >>sys.stderr, 'received "%s"' % data
            if len(data) < pktlen:
                print "not all chars were returned"
                break
            elif len(data)==amount_expected:
                print "all chars were returned"
                break                
            else:
                "len(data) greater than pktlen"

    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()
        print "%"*80+"\n"+"%"*80
