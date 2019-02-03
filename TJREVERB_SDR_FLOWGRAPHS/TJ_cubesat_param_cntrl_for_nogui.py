#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: TJ Cubesat Parameter Control (no GUI)
# Author: Thomas Jefferson High School
# Description: TJ Reverb Headless Cubesat Simulator with Message Loopback
# Generated: Sun Feb  3 05:30:07 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sys
import xmlrpclib
from gnuradio import qtgui


class TJ_cubesat_param_cntrl_for_nogui(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "TJ Cubesat Parameter Control (no GUI)")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("TJ Cubesat Parameter Control (no GUI)")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "TJ_cubesat_param_cntrl_for_nogui")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.freq_chooser = freq_chooser = 144.39e6
        self.xml_rpc_port = xml_rpc_port = 5550
        self.tx_gain = tx_gain = 10
        self.gain = gain = 40
        self.freq = freq = freq_chooser
        self.cubesat_ip_addr = cubesat_ip_addr = "192.168.1.23"
        self.audio_line_driver = audio_line_driver = 0.8

        ##################################################
        # Blocks
        ##################################################
        self.xmlrpc_client1_1 = xmlrpclib.Server('http://192.168.1.23:1234')
        self.xmlrpc_client1_0_1 = xmlrpclib.Server('http://192.168.1.23:1234')
        self.xmlrpc_client1_0_0_1 = xmlrpclib.Server('http://192.168.1.23:1234')
        self.xmlrpc_client1_0_0_0_0 = xmlrpclib.Server('http://192.168.1.23:1234')
        self._tx_gain_range = Range(1, 89, 1, 10, 200)
        self._tx_gain_win = RangeWidget(self._tx_gain_range, self.set_tx_gain, 'tx gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._tx_gain_win, 0, 2, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.tabs = Qt.QTabWidget()
        self.tabs_widget_0 = Qt.QWidget()
        self.tabs_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabs_widget_0)
        self.tabs_grid_layout_0 = Qt.QGridLayout()
        self.tabs_layout_0.addLayout(self.tabs_grid_layout_0)
        self.tabs.addTab(self.tabs_widget_0, 'Big Picture')
        self.tabs_widget_1 = Qt.QWidget()
        self.tabs_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabs_widget_1)
        self.tabs_grid_layout_1 = Qt.QGridLayout()
        self.tabs_layout_1.addLayout(self.tabs_grid_layout_1)
        self.tabs.addTab(self.tabs_widget_1, 'CUBESAT TX/RX')
        self.tabs_widget_2 = Qt.QWidget()
        self.tabs_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabs_widget_2)
        self.tabs_grid_layout_2 = Qt.QGridLayout()
        self.tabs_layout_2.addLayout(self.tabs_grid_layout_2)
        self.tabs.addTab(self.tabs_widget_2, 'GND STAT TX/RX')
        self.tabs_widget_3 = Qt.QWidget()
        self.tabs_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabs_widget_3)
        self.tabs_grid_layout_3 = Qt.QGridLayout()
        self.tabs_layout_3.addLayout(self.tabs_grid_layout_3)
        self.tabs.addTab(self.tabs_widget_3, 'MOD/DEMOD')
        self.top_grid_layout.addWidget(self.tabs, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._gain_range = Range(1, 89, 1, 40, 200)
        self._gain_win = RangeWidget(self._gain_range, self.set_gain, "rx gain", "counter_slider", float)
        self.top_grid_layout.addWidget(self._gain_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._freq_chooser_options = (144.39e6, 137.62e6, 137.9125e6, 137.1e6, 88.5e6, )
        self._freq_chooser_labels = ('APRS (144.39MHz)', 'NOAA-15 (137.62MHz)', 'NOAA-18 (137.9125MHz)', 'NOAA-19 (137.1MHz)', 'FM (88.5MHz)', )
        self._freq_chooser_group_box = Qt.QGroupBox('APRS/NOAA Satellite Frequencies')
        self._freq_chooser_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._freq_chooser_button_group = variable_chooser_button_group()
        self._freq_chooser_group_box.setLayout(self._freq_chooser_box)
        for i, label in enumerate(self._freq_chooser_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._freq_chooser_box.addWidget(radio_button)
        	self._freq_chooser_button_group.addButton(radio_button, i)
        self._freq_chooser_callback = lambda i: Qt.QMetaObject.invokeMethod(self._freq_chooser_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._freq_chooser_options.index(i)))
        self._freq_chooser_callback(self.freq_chooser)
        self._freq_chooser_button_group.buttonClicked[int].connect(
        	lambda i: self.set_freq_chooser(self._freq_chooser_options[i]))
        self.top_grid_layout.addWidget(self._freq_chooser_group_box, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._freq_range = Range(100e6, 6e9, 100e3, freq_chooser, 200)
        self._freq_win = RangeWidget(self._freq_range, self.set_freq, "freq", "counter_slider", float)
        self.top_grid_layout.addWidget(self._freq_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._audio_line_driver_range = Range(0.01, 1, 0.01, 0.8, 200)
        self._audio_line_driver_win = RangeWidget(self._audio_line_driver_range, self.set_audio_line_driver, 'audio line driver', "counter_slider", float)
        self.top_grid_layout.addWidget(self._audio_line_driver_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "TJ_cubesat_param_cntrl_for_nogui")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_freq_chooser(self):
        return self.freq_chooser

    def set_freq_chooser(self, freq_chooser):
        self.freq_chooser = freq_chooser
        self._freq_chooser_callback(self.freq_chooser)
        self.set_freq(self.freq_chooser)

    def get_xml_rpc_port(self):
        return self.xml_rpc_port

    def set_xml_rpc_port(self, xml_rpc_port):
        self.xml_rpc_port = xml_rpc_port

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        self.xmlrpc_client1_0_1.set_tx_gain(self.tx_gain)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.xmlrpc_client1_1.set_gain(self.gain)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.xmlrpc_client1_0_0_1.set_freq(self.freq)

    def get_cubesat_ip_addr(self):
        return self.cubesat_ip_addr

    def set_cubesat_ip_addr(self, cubesat_ip_addr):
        self.cubesat_ip_addr = cubesat_ip_addr

    def get_audio_line_driver(self):
        return self.audio_line_driver

    def set_audio_line_driver(self, audio_line_driver):
        self.audio_line_driver = audio_line_driver
        self.xmlrpc_client1_0_0_0_0.set_audio_line_driver(self.audio_line_driver)


def main(top_block_cls=TJ_cubesat_param_cntrl_for_nogui, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
