#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Aprs Loopback
# Generated: Mon Dec 17 13:31:11 2018
##################################################

from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import bruninga


class aprs_loopback(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Aprs Loopback")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 48000

        ##################################################
        # Blocks
        ##################################################
        self.digital_hdlc_deframer_bp_0 = digital.hdlc_deframer_bp(15, 500)
        self.bruninga_str_to_aprs_0 = bruninga.str_to_aprs('NOCALL', 'NOCALL', [])
        self.bruninga_hdlc_to_ax25_1 = bruninga.hdlc_to_ax25()
        self.bruninga_fsk_demod_0 = bruninga.fsk_demod(samp_rate)
        self.bruninga_ax25_fsk_mod_0 = bruninga.ax25_fsk_mod(samp_rate, 16.0/1200*1000, 5, 2200, 1200, 1200)
        self.blocks_socket_pdu_0 = blocks.socket_pdu("UDP_SERVER", '', '52001', 10000, False)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((0.1, ))
        self.audio_sink_0 = audio.sink(48000, 'hw:1,0', True)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_socket_pdu_0, 'pdus'), (self.bruninga_str_to_aprs_0, 'in'))
        self.msg_connect((self.bruninga_str_to_aprs_0, 'out'), (self.bruninga_ax25_fsk_mod_0, 'in'))
        self.msg_connect((self.digital_hdlc_deframer_bp_0, 'out'), (self.bruninga_hdlc_to_ax25_1, 'in'))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.bruninga_ax25_fsk_mod_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.bruninga_ax25_fsk_mod_0, 0), (self.bruninga_fsk_demod_0, 0))
        self.connect((self.bruninga_fsk_demod_0, 0), (self.digital_hdlc_deframer_bp_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate


def main(top_block_cls=aprs_loopback, options=None):

    tb = top_block_cls()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
