########## TJREVERB_SDR ##########
GNURadio flowgraphs and associated python scripts for the TJREVERB cubesat project
Contained in this repo are combined to create the following general programs

GROUNDSTATION UHD
-gnuradio flowgraph
-python groundstation messenger (tcp client)
-python groundstation messenger (udp client) *future*

CUBESAT UHD
-gnuradio flowgraph
-python cubesat echo server (tcp server)
-python cubesat echo server (udp server) *future*

GROUNDSTATION/CUBESAT SIMULATOR UHD
-gnuradio flowgraph
-python groundstation messenger (tcp client)
-python cubesat echo server (tcp server)
-python groundstation messenger (udp client)*future*
-python cubesat echo server (udp server) *future*

GROUNDSTATION/CUBESAT SIMULATOR NO RADIO
-gnuradio flowgraph
-python groundstation messenger (tcp client)
-python cubesat echo server (tcp server)
-python groundstation messenger (udp client) *future*
-python cubesat echo server (udp server) *future*

DEPENDENCIES (pybombs is recommended for gnuradio see below instructions)
-gnuradio
    https://github.com/gnuradio/gnuradio
-gr-ax25
    https://github.com/dl1ksv/gr-ax25/
-gr-bruninga
    https://github.com/tkuester/gr-bruninga
-python2.7
    apt-get or equivalent pkg manager
-scipy
    apt-get or equivalent pkg manager

INSTALLATION NOTES
clone this repository to your home directory
Recommended installation for gnuradio and gr-ax25 is PYBOMBS
pybombs instructions are here: https://www.gnuradio.org/blog/2016-06-19-pybombs-the-what-the-how-and-the-why/
pybobms install gnuradio (covered in link above)
pybombs install gr-ax25
install gr-bruninga*
follow the normal build proceedure for gr-bruninga:
cd gr-bruninga
mkdir build 
cd build
cmake ..
make
make install

*gr-bruninga is in the "DEPENDENCIES_OOT_BLOCKS" directory
and has been modified to work with pybombs by doing the following:
edited CMakeLists.txt after the line that says "cmake_minimum_required(VERSION 3.0)"
-----------------------------------------------------------------
#install to PyBOMBS target prefix if defined
if (DEFINED ENV{PYBOMBS_PREFIX})
       set(CMAKE_INSTALL_PREFIX $ENV{PYBOMBS_PREFIX})
       message(STATUS "PyBOMBS installed GNU Radio. Setting CMAKE_INSTALL_PREFIX to $ENV{PYBOMBS_PREFIX}")
endif ()
-----------------------------------------------------------------

GENERAL USAGE/OPERATING INSTRUCTIONS
-make the python scripts executable by running
sudo chmod +x 
-launch GNURadio Companion (GRC)
-open one of the flowgraphs
-run the 
This project contains 6 main applications (4 gnuradio flowgraphs
and 2 python scripts). The python GROUNDSTATION MESSENGER is the
endpoint UI at the groundstation used to send messages to the
cubesat.
The python CUBESAT ECHO SERVER sends the message back to the 
GROUNDSTATION MESSENGER which displays the acknowledgement
to confirm the RF path was successful.

The operational flow is as follows:
When using GROUNDSTATION/CUBESAT SIMULATOR UHD
PC#1
 ^
 |
 v
GROUNDSTATION MESSENGER
 ^
 |
 v
GROUNDSTATION/CUBESAT SIMULATOR UHD
 ^
 |
 v
SDR TX RF PORT
 ^
 |
 v
OVER THE AIR/RF CABLES
 ^
 |
 v
SDR RX RF PORT
 ^
 |
 v
GROUNDSTATION/CUBESAT SIMULATOR UHD
 ^
 |
 v
CUBESAT ECHO SERVER
 ^
 |
 v
PC#1



When using GROUNDSTATION/CUBESAT SIMULATOR NO RADIO
PC#1
 ^
 |
 V
GROUNDSTATION MESSENGER
 ^
 |
 V
GROUNDSTATION/CUBESAT SIMULATOR NO RADIO
 ^
 |
 V
CHANNEL SIMULATION BLOCK
 ^
 |
 V
GROUNDSTATION/CUBESAT SIMULATOR NO RADIO
 ^
 |
 V
CUBESAT ECHO SERVER
 ^
 |
 V
PC#1

When using GROUNDSTATION UHD and CUBESAT UHD with 2 separate computers
PC#1
 ^
 |
 V
GROUNDSTATION MESSENGER
 ^
 |
 V
GROUNDSTATION UHD
 ^
 |
 V
SDR TX RF PORT
 ^
 |
 V
OVER THE AIR/RF CABLES
 ^
 |
 V
SDR RX RF PORT
 ^
 |
 V
CUBESAT UHD RX PORT
 ^
 |
 V
CUBESAT ECHO SERVER
 ^
 |
 V
PC#2



PHYSICAL SETUPS
You can use any SDR's, but the example below is for the Ettus B-series
USRP radios. (tested with a B205mini-i and B210)

PHYSICAL SETUP WHEN USING GROUNDSTATION/CUBESAT SIMULATOR UHD
This is run on one PC.
   USRP#1
----RFA----
TX/RX  RX2
 |     ^
 v     |
RX2  TX/RX
----RFA----
   USRP#2
Enter the serial numbers from each USRP in the UHD blocks in the flowgraph.
Enter USRP#1's serial number in the lefthand UHD blocks and USRP#2's serial 
number in the righthand UHD blocks 
If you aren't sure what the serial numbers are, run 'uhd_find_devices'
from a terminal and it will show you the serial numbers.

PHYSICAL SETUP WHEN USING GROUNDSTATION UHD and CUBESAT UHD
on 2 separate PCs. 

PC1 running GROUNDSTATION UHD
   USRP#1
----RFA----
TX/RX  RX2
 |     ^
 v     |
RX2  TX/RX
----RFA----
   USRP#2
PC2 running CUBESAT UHD

TROUBLESHOOTING
-alsa audio issues: 
    *if alsa driver is preventing flowgraph from running
     make sure any other applications using the audio driver are closed
     this can include web browsers, audio players/applications, etc.
    *change the audio sink device name to hw:1,0 or launch it empty

