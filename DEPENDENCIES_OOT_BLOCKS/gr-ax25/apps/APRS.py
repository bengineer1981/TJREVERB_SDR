#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Receives ax.25/ aprs packets
# Author: dl1ksv
# Description: Receives ax.25 packets , display the packets, and converts aprs packet to be send via tcp/ip
# Generated: Thu Sep 27 15:09:24 2018
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
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import afsk
import math
import sip
import sys
from gnuradio import qtgui


class APRS(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Receives ax.25/ aprs packets")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Receives ax.25/ aprs packets")
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

        self.settings = Qt.QSettings("GNU Radio", "APRS")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 192000
        self.Modus = Modus = 144800
        self.IFGain = IFGain = 7
        self.FrequencyOffset = FrequencyOffset = 10
        self.Frequency = Frequency = 97000
        self.Decim = Decim = 4
        self.Decay = Decay = 0.1
        self.Attack = Attack = 0.8

        ##################################################
        # Blocks
        ##################################################
        self._Modus_options = (144800, 145819, )
        self._Modus_labels = ('APRS', 'ISS', )
        self._Modus_tool_bar = Qt.QToolBar(self)
        self._Modus_tool_bar.addWidget(Qt.QLabel("Modus"+": "))
        self._Modus_combo_box = Qt.QComboBox()
        self._Modus_tool_bar.addWidget(self._Modus_combo_box)
        for label in self._Modus_labels: self._Modus_combo_box.addItem(label)
        self._Modus_callback = lambda i: Qt.QMetaObject.invokeMethod(self._Modus_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._Modus_options.index(i)))
        self._Modus_callback(self.Modus)
        self._Modus_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_Modus(self._Modus_options[i]))
        self.top_grid_layout.addWidget(self._Modus_tool_bar, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._FrequencyOffset_range = Range(-20, 20, 1, 10, 200)
        self._FrequencyOffset_win = RangeWidget(self._FrequencyOffset_range, self.set_FrequencyOffset, "FrequencyOffset", "counter", float)
        self.top_grid_layout.addWidget(self._FrequencyOffset_win, 0, 2, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.Display = Qt.QTabWidget()
        self.Display_widget_0 = Qt.QWidget()
        self.Display_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Display_widget_0)
        self.Display_grid_layout_0 = Qt.QGridLayout()
        self.Display_layout_0.addLayout(self.Display_grid_layout_0)
        self.Display.addTab(self.Display_widget_0, 'Settings')
        self.Display_widget_1 = Qt.QWidget()
        self.Display_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Display_widget_1)
        self.Display_grid_layout_1 = Qt.QGridLayout()
        self.Display_layout_1.addLayout(self.Display_grid_layout_1)
        self.Display.addTab(self.Display_widget_1, 'Results')
        self.top_grid_layout.addWidget(self.Display, 1, 0, 1, 3)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/4, #bw
        	'QT GUI Plot', #name
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
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	(Modus-FrequencyOffset)*1000, #fc
        	samp_rate, #bw
        	'QT GUI Plot', #name
        	True, #plotfreq
        	True, #plotwaterfall
        	False, #plottime
        	False, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.Display_grid_layout_0.addWidget(self._qtgui_sink_x_0_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.Display_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Display_grid_layout_0.setColumnStretch(c, 1)


        self.qtgui_sink_x_0.enable_rf_freq(True)



        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate/4, 4900, 1000, firdes.WIN_HAMMING, 6.76))
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_char*1, '', 5577, 1472, True)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/ben-mccall/Desktop/flowgraphs/vhf_noaa_captures/capture1', True)
        self.band_pass_filter_1 = filter.fir_filter_ccc(4, firdes.complex_band_pass(
        	4, samp_rate, FrequencyOffset*500, FrequencyOffset*500+10000, 300, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0 = filter.fir_filter_fff(1, firdes.band_pass(
        	1, samp_rate/Decim, 950, 2450, 100, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate/4, analog.GR_COS_WAVE, -10000, 1, 0)
        self.analog_quadrature_demod_cf_0_0 = analog.quadrature_demod_cf(1)
        self.afsk_afsk1200_0 = afsk.afsk1200(samp_rate/Decim,4)
        self._IFGain_range = Range(1, 25, 1, 7, 200)
        self._IFGain_win = RangeWidget(self._IFGain_range, self.set_IFGain, "IFGain", "counter", int)
        self.top_grid_layout.addWidget(self._IFGain_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.afsk_afsk1200_0, 0), (self.blocks_udp_sink_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0_0, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.band_pass_filter_0_0, 0), (self.afsk_afsk1200_0, 0))
        self.connect((self.band_pass_filter_1, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.band_pass_filter_1, 0))
        self.connect((self.blocks_file_source_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_quadrature_demod_cf_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_waterfall_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "APRS")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate/4)
        self.qtgui_sink_x_0.set_frequency_range((self.Modus-self.FrequencyOffset)*1000, self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/4, 4900, 1000, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_1.set_taps(firdes.complex_band_pass(4, self.samp_rate, self.FrequencyOffset*500, self.FrequencyOffset*500+10000, 300, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate/self.Decim, 950, 2450, 100, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate/4)

    def get_Modus(self):
        return self.Modus

    def set_Modus(self, Modus):
        self.Modus = Modus
        self._Modus_callback(self.Modus)
        self.qtgui_sink_x_0.set_frequency_range((self.Modus-self.FrequencyOffset)*1000, self.samp_rate)

    def get_IFGain(self):
        return self.IFGain

    def set_IFGain(self, IFGain):
        self.IFGain = IFGain

    def get_FrequencyOffset(self):
        return self.FrequencyOffset

    def set_FrequencyOffset(self, FrequencyOffset):
        self.FrequencyOffset = FrequencyOffset
        self.qtgui_sink_x_0.set_frequency_range((self.Modus-self.FrequencyOffset)*1000, self.samp_rate)
        self.band_pass_filter_1.set_taps(firdes.complex_band_pass(4, self.samp_rate, self.FrequencyOffset*500, self.FrequencyOffset*500+10000, 300, firdes.WIN_HAMMING, 6.76))

    def get_Frequency(self):
        return self.Frequency

    def set_Frequency(self, Frequency):
        self.Frequency = Frequency

    def get_Decim(self):
        return self.Decim

    def set_Decim(self, Decim):
        self.Decim = Decim
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate/self.Decim, 950, 2450, 100, firdes.WIN_HAMMING, 6.76))

    def get_Decay(self):
        return self.Decay

    def set_Decay(self, Decay):
        self.Decay = Decay

    def get_Attack(self):
        return self.Attack

    def set_Attack(self, Attack):
        self.Attack = Attack


def main(top_block_cls=APRS, options=None):

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
