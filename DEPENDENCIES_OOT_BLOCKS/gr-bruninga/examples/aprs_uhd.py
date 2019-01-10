#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Aprs Uhd
# Generated: Sat Dec  8 00:36:19 2018
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import bruninga
import math


class aprs_uhd(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Aprs Uhd")

        ##################################################
        # Variables
        ##################################################
        self.tuner_offset = tuner_offset = 10e3
        self.samp_rate = samp_rate = 19200
        self.rf_samp_rate = rf_samp_rate = 1000000

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=samp_rate,
                decimation=rf_samp_rate,
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, rf_samp_rate, 8000, 10000, firdes.WIN_HAMMING, 6.76))
        self.digital_hdlc_deframer_bp_0 = digital.hdlc_deframer_bp(15, 500)
        self.bruninga_hdlc_to_ax25_1 = bruninga.hdlc_to_ax25()
        self.bruninga_fsk_demod_0 = bruninga.fsk_demod(samp_rate)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_rotator_cc_0 = blocks.rotator_cc(2*math.pi*-tuner_offset/rf_samp_rate)
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/ben-mccall/Desktop/flowgraphs/TJ_APRS_CAPTURES/1MHz_144_39MHz_recording_KN4DTQ.bin', True)
        self.analog_nbfm_rx_0 = analog.nbfm_rx(
        	audio_rate=rf_samp_rate,
        	quad_rate=rf_samp_rate,
        	tau=75e-6,
        	max_dev=5e3,
          )

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.digital_hdlc_deframer_bp_0, 'out'), (self.bruninga_hdlc_to_ax25_1, 'in'))
        self.connect((self.analog_nbfm_rx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_file_source_0_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_rotator_cc_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_rotator_cc_0, 0))
        self.connect((self.bruninga_fsk_demod_0, 0), (self.digital_hdlc_deframer_bp_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_nbfm_rx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.bruninga_fsk_demod_0, 0))

    def get_tuner_offset(self):
        return self.tuner_offset

    def set_tuner_offset(self, tuner_offset):
        self.tuner_offset = tuner_offset
        self.blocks_rotator_cc_0.set_phase_inc(2*math.pi*-self.tuner_offset/self.rf_samp_rate)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_rf_samp_rate(self):
        return self.rf_samp_rate

    def set_rf_samp_rate(self, rf_samp_rate):
        self.rf_samp_rate = rf_samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.rf_samp_rate, 8000, 10000, firdes.WIN_HAMMING, 6.76))
        self.blocks_rotator_cc_0.set_phase_inc(2*math.pi*-self.tuner_offset/self.rf_samp_rate)


def main(top_block_cls=aprs_uhd, options=None):

    tb = top_block_cls()
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
