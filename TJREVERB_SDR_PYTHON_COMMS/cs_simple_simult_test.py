#!/usr/bin/python2.7
import socket
import select
import time

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 5558
Message = b"Hello World, From Client B"

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(('127.0.0.1', 5556))
print "UDP socket is listening for incoming packets on port", udp_socket.getsockname()[1]

# When we want to send the next periodic-ping-message out
nextPingTime = time.time()

while True:
   secondsUntilNextPing = nextPingTime - time.time();
   if (secondsUntilNextPing < 0):
      secondsUntilNextPing = 0

   # select() won't return until udp_socket has some data
   # ready-for-read, OR until secondsUntilNextPing seconds 
   # have passed, whichever comes first
   inReady, outReady, exReady = select.select([udp_socket], [], [], secondsUntilNextPing)

   if (udp_socket in inReady):
      # There's an incoming UDP packet ready to receive!
      print(udp_socket.recvfrom(128))

   now = time.time()
   if (now >= nextPingTime):
      # Time to send out the next ping!
      print "Sending out scheduled ping at time ", now
      udp_socket.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))
      nextPingTime = now + 5.0   # we'll do it again in another second
