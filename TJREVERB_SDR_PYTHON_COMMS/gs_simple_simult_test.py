#!/usr/bin/python2.7
import sys
import socket
import select
import readline
import thread
UDP_IP = "127.0.0.1"
TX_PORT = int(sys.argv[1])
RX_PORT = int(sys.argv[2])
def noisy_thread():
    while True:
        sys.stdout.write('\r'+' '*(len(readline.get_line_buffer())+2)+'\r')
        sys.stdout.write('give me a message>>' + readline.get_line_buffer())
        sys.stdout.flush()


msg_sckt = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
msg_sckt.bind((UDP_IP, RX_PORT))

thread.start_new_thread(noisy_thread(msg_sckt), ())
while True:
        msg = raw_input ("give me a message>>")
        msg_sckt.sendto(msg+" ", (UDP_IP, TX_PORT))
        


