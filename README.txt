# TJREVERB_SDR
GNURadio flowgraphs and associated code for the TJREVERB cubesat project
Contained in this repo are the following general programs
GROUNDSTATION
-gnuradio flowgraph
-python terminal message sender (tcp)
-python terminal message sender (udp)
CUBESAT LOOPBACK SIMULATOR
-gnuradio flowgraph
-python terminal message sender (tcp)
-python terminal message sender (udp)

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
