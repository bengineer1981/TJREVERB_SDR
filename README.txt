# TJREVERB_SDR
GNURadio flowgraphs and associated code for the TJREVERB cubesat project
Contained in this repo are the following general programs
GROUNDSTATION
-gnuradio flowgraph
-python terminal message sender (tcp client)
-python terminal message sender (udp client) *future*
CUBESAT LOOPBACK SIMULATOR
-gnuradio flowgraph
-python terminal message sender (tcp server)
-python terminal message sender (udp server) *future*

DEPENDENCIES
gnuradio
    https://github.com/gnuradio/gnuradio
gr-bruninga
    https://github.com/tkuester/gr-bruninga
gr-ax25
    https://github.com/dl1ksv/gr-ax25/
python2.7

INSTALLATION NOTES
if gnuradio is installed using PYBOMBS, gr-bruninga and gr-ax25 
will need to have the following lines added to their CMakeLists.txt
after the line that says "cmake_minimum_required(VERSION 3.0)"
-----------------------------------------------------------------
#install to PyBOMBS target prefix if defined
if (DEFINED ENV{PYBOMBS_PREFIX})
       set(CMAKE_INSTALL_PREFIX $ENV{PYBOMBS_PREFIX})
       message(STATUS "PyBOMBS installed GNU Radio. Setting CMAKE_INSTALL_PREFIX to $ENV{PYBOMBS_PREFIX}")
endif ()
-----------------------------------------------------------------

USAGE
after installation, open the GRC flowgraph.
if using without an attached SDR, disable the 4 UHD blocks
and enable the 'multiply const' blocks and the throttle block.
this will allow the flowgraph to operate in a simulated mode.

you can use any SDR's, but the example below is for the Ettus B-series
USRP radios. (tested with a B205mini-i and B210)
If using 2 usrp radios, cross-connect their tx and rx ports like so:
   USRP#1
----RFA----
TX/RX  RX2
 |     ^
 v     |
RX2  TX/RX
----RFA----
   USRP#2
enter the serial numbers from each USRP in the UHD blocks. If you
aren't sure what the serial numbers are, run 'uhd_find_devices' from
a terminal and it will show you the serial numbers.
