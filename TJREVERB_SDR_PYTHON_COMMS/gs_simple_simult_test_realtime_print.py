#!/usr/bin/python2.7
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
