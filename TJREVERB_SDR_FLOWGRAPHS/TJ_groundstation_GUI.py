#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: TJ Groundstation GUI
# Author: Thomas Jefferson High School
# Description: TJ Reverb AFSK Modem
# Generated: Fri Jan 25 19:09:30 2019
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

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from detectMarkSpace import detectMarkSpace  # grc-generated hier_block
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import afsk
import bruninga
import sip
import time
from gnuradio import qtgui


class TJ_groundstation_GUI(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "TJ Groundstation GUI")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("TJ Groundstation GUI")
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

        self.settings = Qt.QSettings("GNU Radio", "TJ_groundstation_GUI")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.interp = interp = 4
        self.freq_chooser = freq_chooser = 137.62e6
        self.audio_rate = audio_rate = 48000
        self.tx_gain = tx_gain = 10
        self.rx_downsamp_bw = rx_downsamp_bw = 10000
        self.rf_tx_rate = rf_tx_rate = audio_rate*interp
        self.rf_rx_rate = rf_rx_rate = 192000
        self.preamble_len = preamble_len = 300
        self.groundstation_port_2 = groundstation_port_2 = "5557"
        self.groundstation_port_1 = groundstation_port_1 = "5555"
        self.gain = gain = 40
        self.freq = freq = freq_chooser
        self.cubesat_ip_addr = cubesat_ip_addr = "127.0.0.1"
        self.baud_rate = baud_rate = 1200
        self.audio_line_driver = audio_line_driver = 0.8
        self.Decay = Decay = 0.8
        self.Attack = Attack = 0.8

        ##################################################
        # Blocks
        ##################################################
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
        self.uhd_usrp_source_0_1 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0_1.set_samp_rate(rf_rx_rate)
        self.uhd_usrp_source_0_1.set_center_freq(freq, 0)
        self.uhd_usrp_source_0_1.set_gain(gain, 0)
        self.uhd_usrp_source_0_1.set_antenna('RX2', 0)
        self.uhd_usrp_source_0_1.set_bandwidth(rf_rx_rate, 0)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(rf_tx_rate)
        self.uhd_usrp_sink_0.set_center_freq(freq, 0)
        self.uhd_usrp_sink_0.set_gain(tx_gain, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_sink_0.set_bandwidth(rf_tx_rate, 0)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=4,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_0_2 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq, #fc
        	rf_rx_rate, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_2.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0_2.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_2.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0_2.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0_2.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_2.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_2.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_2.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_2.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_2_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_2.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_2_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.tabs_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tabs_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0_1 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq, #fc
        	rf_rx_rate, #bw
        	"GND STAT DEMOD", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_1.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0_1.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_1.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0_1.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0_1.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_1.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_1.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_1.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_1_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_1_win, 3, 0, 1, 1)
        for r in range(3, 4):
            self.tabs_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tabs_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_1 = qtgui.time_sink_f(
        	1024, #size
        	audio_rate, #samp_rate
        	"GND STAT MOD", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0_1.disable_legend()

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
                self.qtgui_time_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_3.addWidget(self._qtgui_time_sink_x_0_1_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.tabs_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tabs_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	1024, #size
        	audio_rate, #samp_rate
        	"GND STAT DEMOD", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()

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
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_3.addWidget(self._qtgui_time_sink_x_0_0_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.tabs_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tabs_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_2 = qtgui.freq_sink_c(
        	4096, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq, #fc
        	rf_rx_rate, #bw
        	"GND STAT DEMOD", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_2.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_2.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_2.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_2.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_2.enable_grid(False)
        self.qtgui_freq_sink_x_0_2.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_2.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_2.enable_control_panel(True)

        if not True:
          self.qtgui_freq_sink_x_0_2.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_2.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_x_0_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_2.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_2.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_2.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_2.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_2_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_2.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_2_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.tabs_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tabs_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_1_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq, #fc
        	rf_tx_rate, #bw
        	"GND STAT MOD", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_1_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_1_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_1_1.enable_grid(False)
        self.qtgui_freq_sink_x_0_1_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1_1.enable_control_panel(True)

        if not True:
          self.qtgui_freq_sink_x_0_1_1.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_1_1.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_x_0_1_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1_1.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_1_1_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.tabs_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tabs_grid_layout_0.setColumnStretch(c, 1)
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(4, firdes.low_pass(
        	1, rf_rx_rate, rx_downsamp_bw/2, 1000, firdes.WIN_HAMMING, 6.76))
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
        self.detectMarkSpace_1_0_0 = detectMarkSpace(
            Frequency=2200,
            attack=Attack,
            decay=Decay,
            samp_rate=audio_rate,
        )
        self.detectMarkSpace_0_0_0 = detectMarkSpace(
            Frequency=1200,
            attack=Attack,
            decay=Decay,
            samp_rate=audio_rate,
        )
        self.bruninga_str_to_aprs_0 = bruninga.str_to_aprs('KN4DTQ', 'KN4DTQ', [])
        self.bruninga_ax25_fsk_mod_0 = bruninga.ax25_fsk_mod(audio_rate, preamble_len, 5, 2200, 1200, baud_rate)
        self.blocks_udp_sink_0_0 = blocks.udp_sink(gr.sizeof_char*1, cubesat_ip_addr, int(groundstation_port_2), 1472, True)
        self.blocks_sub_xx_0_0_0_0 = blocks.sub_ff(1)
        self.blocks_socket_pdu_0_0 = blocks.socket_pdu("UDP_SERVER", cubesat_ip_addr, groundstation_port_1, 10000, False)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((audio_line_driver, ))
        self.audio_sink_0 = audio.sink(audio_rate, 'hw:1,0', True)
        self.analog_nbfm_tx_0 = analog.nbfm_tx(
        	audio_rate=audio_rate,
        	quad_rate=audio_rate,
        	tau=75e-6,
        	max_dev=5e3,
        	fh=-1.0,
                )
        self.analog_nbfm_rx_0_0 = analog.nbfm_rx(
        	audio_rate=audio_rate,
        	quad_rate=audio_rate,
        	tau=75e-6,
        	max_dev=5e3,
          )
        self.afsk_ax25decode_1_0 = afsk.ax25decode(audio_rate, 1)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_socket_pdu_0_0, 'pdus'), (self.bruninga_str_to_aprs_0, 'in'))
        self.msg_connect((self.bruninga_str_to_aprs_0, 'out'), (self.bruninga_ax25_fsk_mod_0, 'in'))
        self.connect((self.afsk_ax25decode_1_0, 0), (self.blocks_udp_sink_0_0, 0))
        self.connect((self.analog_nbfm_rx_0_0, 0), (self.detectMarkSpace_0_0_0, 0))
        self.connect((self.analog_nbfm_rx_0_0, 0), (self.detectMarkSpace_1_0_0, 0))
        self.connect((self.analog_nbfm_rx_0_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.analog_nbfm_tx_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.analog_nbfm_tx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_0_1, 0))
        self.connect((self.blocks_sub_xx_0_0_0_0, 0), (self.afsk_ax25decode_1_0, 0))
        self.connect((self.bruninga_ax25_fsk_mod_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.detectMarkSpace_0_0_0, 0), (self.blocks_sub_xx_0_0_0_0, 0))
        self.connect((self.detectMarkSpace_1_0_0, 0), (self.blocks_sub_xx_0_0_0_0, 1))
        self.connect((self.low_pass_filter_0_0, 0), (self.analog_nbfm_rx_0_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.qtgui_freq_sink_x_0_2, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.qtgui_waterfall_sink_x_0_1, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.qtgui_freq_sink_x_0_1_1, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.qtgui_waterfall_sink_x_0_2, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.uhd_usrp_source_0_1, 0), (self.low_pass_filter_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "TJ_groundstation_GUI")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_interp(self):
        return self.interp

    def set_interp(self, interp):
        self.interp = interp
        self.set_rf_tx_rate(self.audio_rate*self.interp)

    def get_freq_chooser(self):
        return self.freq_chooser

    def set_freq_chooser(self, freq_chooser):
        self.freq_chooser = freq_chooser
        self.set_freq(self.freq_chooser)
        self._freq_chooser_callback(self.freq_chooser)

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.set_rf_tx_rate(self.audio_rate*self.interp)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.audio_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.audio_rate)
        self.detectMarkSpace_1_0_0.set_samp_rate(self.audio_rate)
        self.detectMarkSpace_0_0_0.set_samp_rate(self.audio_rate)

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        self.uhd_usrp_sink_0.set_gain(self.tx_gain, 0)


    def get_rx_downsamp_bw(self):
        return self.rx_downsamp_bw

    def set_rx_downsamp_bw(self, rx_downsamp_bw):
        self.rx_downsamp_bw = rx_downsamp_bw
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.rf_rx_rate, self.rx_downsamp_bw/2, 1000, firdes.WIN_HAMMING, 6.76))

    def get_rf_tx_rate(self):
        return self.rf_tx_rate

    def set_rf_tx_rate(self, rf_tx_rate):
        self.rf_tx_rate = rf_tx_rate
        self.uhd_usrp_sink_0.set_samp_rate(self.rf_tx_rate)
        self.uhd_usrp_sink_0.set_bandwidth(self.rf_tx_rate, 0)
        self.qtgui_freq_sink_x_0_1_1.set_frequency_range(self.freq, self.rf_tx_rate)

    def get_rf_rx_rate(self):
        return self.rf_rx_rate

    def set_rf_rx_rate(self, rf_rx_rate):
        self.rf_rx_rate = rf_rx_rate
        self.uhd_usrp_source_0_1.set_samp_rate(self.rf_rx_rate)
        self.uhd_usrp_source_0_1.set_bandwidth(self.rf_rx_rate, 0)
        self.qtgui_waterfall_sink_x_0_2.set_frequency_range(self.freq, self.rf_rx_rate)
        self.qtgui_waterfall_sink_x_0_1.set_frequency_range(self.freq, self.rf_rx_rate)
        self.qtgui_freq_sink_x_0_2.set_frequency_range(self.freq, self.rf_rx_rate)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.rf_rx_rate, self.rx_downsamp_bw/2, 1000, firdes.WIN_HAMMING, 6.76))

    def get_preamble_len(self):
        return self.preamble_len

    def set_preamble_len(self, preamble_len):
        self.preamble_len = preamble_len

    def get_groundstation_port_2(self):
        return self.groundstation_port_2

    def set_groundstation_port_2(self, groundstation_port_2):
        self.groundstation_port_2 = groundstation_port_2

    def get_groundstation_port_1(self):
        return self.groundstation_port_1

    def set_groundstation_port_1(self, groundstation_port_1):
        self.groundstation_port_1 = groundstation_port_1

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.uhd_usrp_source_0_1.set_gain(self.gain, 0)


    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.uhd_usrp_source_0_1.set_center_freq(self.freq, 0)
        self.uhd_usrp_sink_0.set_center_freq(self.freq, 0)
        self.qtgui_waterfall_sink_x_0_2.set_frequency_range(self.freq, self.rf_rx_rate)
        self.qtgui_waterfall_sink_x_0_1.set_frequency_range(self.freq, self.rf_rx_rate)
        self.qtgui_freq_sink_x_0_2.set_frequency_range(self.freq, self.rf_rx_rate)
        self.qtgui_freq_sink_x_0_1_1.set_frequency_range(self.freq, self.rf_tx_rate)

    def get_cubesat_ip_addr(self):
        return self.cubesat_ip_addr

    def set_cubesat_ip_addr(self, cubesat_ip_addr):
        self.cubesat_ip_addr = cubesat_ip_addr

    def get_baud_rate(self):
        return self.baud_rate

    def set_baud_rate(self, baud_rate):
        self.baud_rate = baud_rate

    def get_audio_line_driver(self):
        return self.audio_line_driver

    def set_audio_line_driver(self, audio_line_driver):
        self.audio_line_driver = audio_line_driver
        self.blocks_multiply_const_vxx_0.set_k((self.audio_line_driver, ))

    def get_Decay(self):
        return self.Decay

    def set_Decay(self, Decay):
        self.Decay = Decay
        self.detectMarkSpace_1_0_0.set_decay(self.Decay)
        self.detectMarkSpace_0_0_0.set_decay(self.Decay)

    def get_Attack(self):
        return self.Attack

    def set_Attack(self, Attack):
        self.Attack = Attack
        self.detectMarkSpace_1_0_0.set_attack(self.Attack)
        self.detectMarkSpace_0_0_0.set_attack(self.Attack)


def main(top_block_cls=TJ_groundstation_GUI, options=None):

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
