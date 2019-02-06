#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: TJ Groundstation Parameter Control (no GUI with IQ Streaming)
# Author: Thomas Jefferson High School
# Description: TJ Reverb AFSK Modem
# Generated: Wed Feb  6 01:41:55 2019
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
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys
import xmlrpclib
from gnuradio import qtgui


class TJ_groundstation_param_cntrl_for_no_gui_with_IQ_streaming(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "TJ Groundstation Parameter Control (no GUI with IQ Streaming)")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("TJ Groundstation Parameter Control (no GUI with IQ Streaming)")
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

        self.settings = Qt.QSettings("GNU Radio", "TJ_groundstation_param_cntrl_for_no_gui_with_IQ_streaming")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.freq_chooser = freq_chooser = 144.39e6
        self.xml_rpc_port = xml_rpc_port = 5550
        self.tx_gain = tx_gain = 10
        self.rf_rx_rate = rf_rx_rate = 192000
        self.groundstation_zmq_port_4 = groundstation_zmq_port_4 = "5504"
        self.groundstation_zmq_port_3 = groundstation_zmq_port_3 = "5503"
        self.groundstation_zmq_port_2 = groundstation_zmq_port_2 = "5502"
        self.groundstation_zmq_port_1 = groundstation_zmq_port_1 = "5501"
        self.groundstation_ip_addr = groundstation_ip_addr = "192.168.1.10"
        self.gain = gain = 40
        self.freq = freq = freq_chooser
        self.audio_rate = audio_rate = 48000
        self.audio_line_driver = audio_line_driver = 0.8

        ##################################################
        # Blocks
        ##################################################
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
        self.zeromq_pull_source_0_0_0_0 = zeromq.pull_source(gr.sizeof_float, 1, "tcp://"+groundstation_ip_addr+":"+groundstation_zmq_port_4, 100, False, -1)
        self.zeromq_pull_source_0_0_0 = zeromq.pull_source(gr.sizeof_float, 1, "tcp://"+groundstation_ip_addr+":"+groundstation_zmq_port_3, 100, False, -1)
        self.zeromq_pull_source_0_0 = zeromq.pull_source(gr.sizeof_gr_complex, 1, "tcp://"+groundstation_ip_addr+":"+groundstation_zmq_port_2, 100, False, -1)
        self.zeromq_pull_source_0 = zeromq.pull_source(gr.sizeof_gr_complex, 1, "tcp://"+groundstation_ip_addr+":"+groundstation_zmq_port_1, 100, False, -1)
        self.xmlrpc_client1_1 = xmlrpclib.Server('http://cubesat_ip_addr:1234')
        self.xmlrpc_client1_0_1 = xmlrpclib.Server('http://cubesat_ip_addr:1234')
        self.xmlrpc_client1_0_0_1 = xmlrpclib.Server('http://cubesat_ip_addr:1234')
        self.xmlrpc_client1_0_0_0_0 = xmlrpclib.Server('http://cubesat_ip_addr:1234')
        self._tx_gain_range = Range(1, 89, 1, 10, 200)
        self._tx_gain_win = RangeWidget(self._tx_gain_range, self.set_tx_gain, 'tx gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._tx_gain_win, 0, 2, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0_2_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	audio_rate, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_2_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0_2_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_2_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0_2_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0_2_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_2_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_2_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_2_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_2_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_2_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_2_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_2_0.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_2_0_win, 3, 1, 1, 1)
        for r in range(3, 4):
            self.tabs_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.tabs_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	audio_rate, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.tabs_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.tabs_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_2 = qtgui.time_sink_f(
        	1024, #size
        	audio_rate, #samp_rate
        	"GROUNDSTATION AUDIO DEMOD", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_2.set_update_time(0.10)
        self.qtgui_time_sink_x_0_2.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_2.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_2.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_2.enable_autoscale(False)
        self.qtgui_time_sink_x_0_2.enable_grid(False)
        self.qtgui_time_sink_x_0_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_2.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0_2.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_2.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_2_win = sip.wrapinstance(self.qtgui_time_sink_x_0_2.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_3.addWidget(self._qtgui_time_sink_x_0_2_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.tabs_grid_layout_3.setRowStretch(r, 1)
        for c in range(1, 2):
            self.tabs_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	audio_rate, #samp_rate
        	"GROUNDSTATION AUDIO MOD", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_3.addWidget(self._qtgui_time_sink_x_0_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.tabs_grid_layout_3.setRowStretch(r, 1)
        for c in range(1, 2):
            self.tabs_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_1_1_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	audio_rate, #bw
        	"GROUNDSTATION DEMOD", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_1_1_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1_1_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_1_1_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1_1_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_1_1_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_1_1_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1_1_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1_1_0.enable_control_panel(True)

        if not True:
          self.qtgui_freq_sink_x_0_1_1_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_1_1_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1_1_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1_1_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1_1_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_1_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1_1_0.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_1_1_0_win, 2, 1, 1, 1)
        for r in range(2, 3):
            self.tabs_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.tabs_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	4096, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	audio_rate, #bw
        	"GROUNDSTATION MOD", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(True)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.tabs_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.tabs_grid_layout_0.setColumnStretch(c, 1)
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
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, rf_rx_rate,True)
        self._audio_line_driver_range = Range(0.01, 1, 0.01, 0.8, 200)
        self._audio_line_driver_win = RangeWidget(self._audio_line_driver_range, self.set_audio_line_driver, 'audio line driver', "counter_slider", float)
        self.top_grid_layout.addWidget(self._audio_line_driver_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0_1_1_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_waterfall_sink_x_0_2_0, 0))
        self.connect((self.zeromq_pull_source_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.zeromq_pull_source_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.zeromq_pull_source_0_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.zeromq_pull_source_0_0_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.zeromq_pull_source_0_0_0_0, 0), (self.qtgui_time_sink_x_0_2, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "TJ_groundstation_param_cntrl_for_no_gui_with_IQ_streaming")
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

    def get_rf_rx_rate(self):
        return self.rf_rx_rate

    def set_rf_rx_rate(self, rf_rx_rate):
        self.rf_rx_rate = rf_rx_rate
        self.blocks_throttle_0.set_sample_rate(self.rf_rx_rate)

    def get_groundstation_zmq_port_4(self):
        return self.groundstation_zmq_port_4

    def set_groundstation_zmq_port_4(self, groundstation_zmq_port_4):
        self.groundstation_zmq_port_4 = groundstation_zmq_port_4

    def get_groundstation_zmq_port_3(self):
        return self.groundstation_zmq_port_3

    def set_groundstation_zmq_port_3(self, groundstation_zmq_port_3):
        self.groundstation_zmq_port_3 = groundstation_zmq_port_3

    def get_groundstation_zmq_port_2(self):
        return self.groundstation_zmq_port_2

    def set_groundstation_zmq_port_2(self, groundstation_zmq_port_2):
        self.groundstation_zmq_port_2 = groundstation_zmq_port_2

    def get_groundstation_zmq_port_1(self):
        return self.groundstation_zmq_port_1

    def set_groundstation_zmq_port_1(self, groundstation_zmq_port_1):
        self.groundstation_zmq_port_1 = groundstation_zmq_port_1

    def get_groundstation_ip_addr(self):
        return self.groundstation_ip_addr

    def set_groundstation_ip_addr(self, groundstation_ip_addr):
        self.groundstation_ip_addr = groundstation_ip_addr

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

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.qtgui_waterfall_sink_x_0_2_0.set_frequency_range(0, self.audio_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.audio_rate)
        self.qtgui_time_sink_x_0_2.set_samp_rate(self.audio_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.audio_rate)
        self.qtgui_freq_sink_x_0_1_1_0.set_frequency_range(0, self.audio_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.audio_rate)

    def get_audio_line_driver(self):
        return self.audio_line_driver

    def set_audio_line_driver(self, audio_line_driver):
        self.audio_line_driver = audio_line_driver
        self.xmlrpc_client1_0_0_0_0.set_audio_line_driver(self.audio_line_driver)


def main(top_block_cls=TJ_groundstation_param_cntrl_for_no_gui_with_IQ_streaming, options=None):

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
