#!/usr/bin/python2.7
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#take user inputs for ports between 5500 and 5599
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
    
server_address = ('127.0.0.1', int(port_num))
print >> sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
expected_pktlen = 127
header_len = 68
message_len = 58
msg_cnt = 0
while True:
    # Wait for a connection
    print >> sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        start_of_data = 68
        while True:
            data = connection.recv(expected_pktlen)
            print "%"*80+"\n"+"%"*80
            msg_cnt += 1
            print "msg #: %d" % msg_cnt
            print >>sys.stderr, "raw data length:'%d'\n" % len(data)
            print >>sys.stderr, "raw data text:'%s'" % data
            print >>sys.stderr, '\nstripping header\nreceived message (chars [%d:%d]:\n"%s"'% (start_of_data,expected_pktlen,data[start_of_data:expected_pktlen])
            data = data[start_of_data:expected_pktlen] #add '.' to end. It will be stripped off by the string to APRS block
            if data:
                print "%"*80+"\n"+"%"*80
                print >>sys.stderr, "sending the following data length back to client: '%d' chars" % len(data)
                print >>sys.stderr, "sending the following data back to client:\n'%s'END" % data
                connection.sendall(data)
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
            
    finally:
        # Clean up the connection
        connection.close()
