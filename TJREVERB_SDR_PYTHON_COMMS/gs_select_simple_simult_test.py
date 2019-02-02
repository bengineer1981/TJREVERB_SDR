#!/usr/bin/python2.7
import sys
import socket
import select
UDP_IP = "127.0.0.1"
TX_PORT = int(sys.argv[1])
RX_PORT = int(sys.argv[2])

msg_lstn = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
msg_lstn.bind((UDP_IP, RX_PORT))

while True:
    inReady, outReady, exReady = select.select([msg_lstn], [], [], 1.0)
    if msg_lstn in inReady:
        print msg_lstn.recvfrom(1024)
    else:
        msg = raw_input ("give me a message>>")
        msg_snd = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP

        msg_snd.sendto(msg+" ", (UDP_IP, TX_PORT))

#!/usr/bin/python

import time,readline,thread,sys

def noisy_thread():
    while True:
        time.sleep(3)
        sys.stdout.write('\r'+' '*(len(readline.get_line_buffer())+2)+'\r')
        print 'Interrupting text!'
        sys.stdout.write('> ' + readline.get_line_buffer())
        sys.stdout.flush()

thread.start_new_thread(noisy_thread, ())
while True:
    s = raw_input('> ')
