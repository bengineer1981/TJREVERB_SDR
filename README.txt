########## TJREVERB_SDR ##########
GNURadio flowgraphs and associated python scripts for the TJREVERB cubesat project
Contained in this repo are combined to create the following general programs

GROUNDSTATION UHD
Over the air Ground Station portion of the 
Telemetry & Command link. Requires Ettus Research 
UHD compatible SDR, but can be modified to
use any SDR hardware by replacing the UHD
source/sink blocks with the appropriate hardware
blocks for the replacement radio. Radio must have
transmit and receive capability.
-gnuradio flowgraph
-python groundstation messenger (tcp client)
-python groundstation messenger (udp client) *future*

CUBESAT UHD
Over the air Cubesat portion of the 
Telemetry & Command link. Used for emulating 
Cubesat for groundstation testing. Requires 
Ettus Research UHD compatible SDR, but can 
be modified to use any SDR hardware by replacing 
the UHD source/sink blocks with the appropriate 
hardware blocks for the replacement radio. Radio 
must have transmit and receive capability.
-gnuradio flowgraph
-python cubesat echo server (tcp server)
-python cubesat echo server (udp server) *future*

GROUNDSTATION/CUBESAT SIMULATOR UHD
Complete Telemetry & Command simulator that
uses hardware connected with cables and 
attenuators. Used to ensure compatibility
of hardware and software.
-gnuradio flowgraph
-python groundstation messenger (tcp client)
-python cubesat echo server (tcp server)
-python groundstation messenger (udp client)*future*
-python cubesat echo server (udp server) *future*

GROUNDSTATION/CUBESAT SIMULATOR NO RADIO
Complete Telemetry & Command simulator that
can be run with only GNURadio,the out-of-tree
blocks (included in this repo) and the two 
included python scripts. This is meant for
development of primarily the GNURadio Companion
GUI and the two python scripts with focus on
user input and command parameters (message length,
format, structure,etc.)
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
1)clone this repository to your home directory
    Recommended installation for gnuradio and gr-ax25 is PYBOMBS
    pybombs instructions are here: https://www.gnuradio.org/blog/2016-06-19-pybombs-the-what-the-how-and-the-why/
2) from the link above, install gnuradio via pybombs
3) run "pybombs install gr-ax25" (you can also build from source, see note below)
4) install gr-bruninga from source (see note below)
    follow the normal build proceedure for gr-bruninga:
    cd gr-bruninga
    mkdir build 
    cd build
    cmake .. (see note below)
    make
    make install

5) open gnuradio companion and from the file menu, navigate to
    gr-ax25/apps/ and open the file called "detectmarkspace.grc"
    in gnuradio companion, click 'run-->generate'. This will generate
    a necessary block needed for this project.
6) Open any of the flowgraphs to confirm that there are no missing blocks,
    recommend starting with either the TJ_groundstation_UHD or TJ_cubesat_UHD.
    This is mostly to confirm that you have properly configured the out of tree blocks.
7) You're setup should be complete now. You can proceed to the 

INSTALLATION NOTES MENTIONED ABOVE:
*gr-ax25 if you get an error building gr-ax25 that says it's missing swig,
it can be installed via apt-get  

*gr-bruninga: a modified verstion of this block is in the "DEPENDENCIES_OOT_BLOCKS" 
directory in this repo. It has been modified to compile into a pybombs environment.
If you intend on using gr-bruninga in a pybombs environment and choose to clone the
source from the gr-bruninga git repo instead of using the one included in this repo,
 you will need to make the modification yourself by inserting the following lines
into CMakeLists.txt:
(after the line that says "cmake_minimum_required(VERSION 3.0)")

-----------------------------------------------------------------
#install to PyBOMBS target prefix if defined
if (DEFINED ENV{PYBOMBS_PREFIX})
       set(CMAKE_INSTALL_PREFIX $ENV{PYBOMBS_PREFIX})
       message(STATUS "PyBOMBS installed GNU Radio. Setting CMAKE_INSTALL_PREFIX to $ENV{PYBOMBS_PREFIX}")
endif ()
-----------------------------------------------------------------

*cmake: if running "cmake .." doesn't work, try "cmake -DCMAKE_INSTALL_PREFIX=/usr .."
    this is especially relevant if you installed gnuradio via apt-get


GENERAL USAGE/OPERATING INSTRUCTIONS
This project contains 6 main applications (4 gnuradio flowgraphs
and 2 python scripts). The python GROUNDSTATION MESSENGER is the
endpoint UI at the groundstation used to send messages through GNURadio
to the cubesat.
The python CUBESAT ECHO SERVER receives the message from the 
GROUNDSTATION MESSENGER and sends the message through GNURadio
and back to the GROUNDSTATION MESSENGER which displays the acknowledgement
confirming the RF/simulation path was successful. (Diagrams below)


If you run one of the simulation flowgraphs, you need to use
the GROUNDSTATION MESSENGER and the CUBESAT ECHO SERVER python scripts
on the same machine. The UHD simulation flowgraph requires
2 SDR radios, but the 'no radio' flowgraph doesn't require any
hardware.
If you run the cubesat UHD or groundstation UHD flowgraphs,
you will need one SDR.


To run the applications:
-make the python scripts executable by running
 sudo chmod +x scriptname1 scriptname2
-launch GNURadio Companion (GRC)
-open one of the flowgraphs
-look at the socket PDU block(s) and note the port numbers
-enter them as the follows:
 TCP server port --> GROUNDSTATION MESSENGER
 TCP client port --> CUBESAT ECHO SERVER
-depending on the flowgraph, run one or both of the python scripts
 and launch the gnuradio flowgraph. If you are using the 
 CUBESAT ECHO SERVER you should see the server connect to the 
 flowgraph.
-typing a message in the GROUNDSTATION MESSENGER will send
 a message through GNURadio and wait for a return message from the
 CUBESAT ECHO SERVER

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
USRP radios. (tested with a B205mini-i and B210) If using different
hardware, the appropriate sources and sinks will be necessary.

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

