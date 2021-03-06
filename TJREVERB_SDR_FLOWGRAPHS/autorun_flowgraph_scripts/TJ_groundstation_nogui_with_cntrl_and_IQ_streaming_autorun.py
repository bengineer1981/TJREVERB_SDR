#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: TJ Groundstation No Gui with Control and IQ streaming
# Author: Thomas Jefferson High School
# Description: TJ Reverb AFSK Modem
# Generated: Wed Feb  6 03:08:45 2019
##################################################

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from detectMarkSpace import detectMarkSpace  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import afsk
import bruninga
import time


class TJ_groundstation_nogui_with_cntrl_and_IQ_streaming_autorun(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "TJ Groundstation No Gui with Control and IQ streaming")

        ##################################################
        # Variables
        ##################################################
        self.interp = interp = 4
        self.audio_rate = audio_rate = 48000
        self.tx_gain = tx_gain = 10
        self.rx_downsamp_bw = rx_downsamp_bw = 10000
        self.rf_tx_rate = rf_tx_rate = audio_rate*interp
        self.rf_rx_rate = rf_rx_rate = 192000
        self.preamble_len = preamble_len = 300
        self.groundstation_zmq_port_4 = groundstation_zmq_port_4 = "5504"
        self.groundstation_zmq_port_3 = groundstation_zmq_port_3 = "5503"
        self.groundstation_zmq_port_2 = groundstation_zmq_port_2 = "5502"
        self.groundstation_zmq_port_1 = groundstation_zmq_port_1 = "5501"
        self.groundstation_port_2 = groundstation_port_2 = "5557"
        self.groundstation_port_1 = groundstation_port_1 = "5555"
        self.groundstation_ip_addr = groundstation_ip_addr = "192.168.1.10"
        self.groundstation_controller_ip = groundstation_controller_ip = "192.268.1.3"
        self.gain = gain = 40
        self.freq = freq = 144.39e6
        self.baud_rate = baud_rate = 1200
        self.audio_line_driver = audio_line_driver = .8
        self.Decay = Decay = 0.8
        self.Attack = Attack = 0.8

        ##################################################
        # Blocks
        ##################################################
        self.zeromq_push_sink_0_0_0_0 = zeromq.push_sink(gr.sizeof_float, 1, "tcp://"+groundstation_ip_addr+":"+groundstation_zmq_port_4, 100, False, -1)
        self.zeromq_push_sink_0_0_0 = zeromq.push_sink(gr.sizeof_float, 1, "tcp://"+groundstation_ip_addr+":"+groundstation_zmq_port_3, 100, False, -1)
        self.zeromq_push_sink_0_0 = zeromq.push_sink(gr.sizeof_gr_complex, 1, "tcp://"+groundstation_ip_addr+":"+groundstation_zmq_port_2, 100, False, -1)
        self.zeromq_push_sink_0 = zeromq.push_sink(gr.sizeof_gr_complex, 1, "tcp://"+groundstation_ip_addr+":"+groundstation_zmq_port_1, 100, False, -1)
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
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(4, firdes.low_pass(
        	1, rf_rx_rate, rx_downsamp_bw/2, 1000, firdes.WIN_HAMMING, 6.76))
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
        self.blocks_udp_sink_0_0 = blocks.udp_sink(gr.sizeof_char*1, groundstation_controller_ip, int(groundstation_port_2), 1472, True)
        self.blocks_sub_xx_0_0_0_0 = blocks.sub_ff(1)
        self.blocks_socket_pdu_0_0 = blocks.socket_pdu("UDP_SERVER", groundstation_ip_addr, groundstation_port_1, 10000, False)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((0.8, ))
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
        self.connect((self.analog_nbfm_rx_0_0, 0), (self.zeromq_push_sink_0_0_0_0, 0))
        self.connect((self.analog_nbfm_tx_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.analog_nbfm_tx_0, 0), (self.zeromq_push_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.analog_nbfm_tx_0, 0))
        self.connect((self.blocks_sub_xx_0_0_0_0, 0), (self.afsk_ax25decode_1_0, 0))
        self.connect((self.bruninga_ax25_fsk_mod_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.bruninga_ax25_fsk_mod_0, 0), (self.zeromq_push_sink_0_0_0, 0))
        self.connect((self.detectMarkSpace_0_0_0, 0), (self.blocks_sub_xx_0_0_0_0, 0))
        self.connect((self.detectMarkSpace_1_0_0, 0), (self.blocks_sub_xx_0_0_0_0, 1))
        self.connect((self.low_pass_filter_0_0, 0), (self.analog_nbfm_rx_0_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.zeromq_push_sink_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.uhd_usrp_source_0_1, 0), (self.low_pass_filter_0_0, 0))

    def get_interp(self):
        return self.interp

    def set_interp(self, interp):
        self.interp = interp
        self.set_rf_tx_rate(self.audio_rate*self.interp)

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.set_rf_tx_rate(self.audio_rate*self.interp)
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

    def get_rf_rx_rate(self):
        return self.rf_rx_rate

    def set_rf_rx_rate(self, rf_rx_rate):
        self.rf_rx_rate = rf_rx_rate
        self.uhd_usrp_source_0_1.set_samp_rate(self.rf_rx_rate)
        self.uhd_usrp_source_0_1.set_bandwidth(self.rf_rx_rate, 0)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.rf_rx_rate, self.rx_downsamp_bw/2, 1000, firdes.WIN_HAMMING, 6.76))

    def get_preamble_len(self):
        return self.preamble_len

    def set_preamble_len(self, preamble_len):
        self.preamble_len = preamble_len

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

    def get_groundstation_port_2(self):
        return self.groundstation_port_2

    def set_groundstation_port_2(self, groundstation_port_2):
        self.groundstation_port_2 = groundstation_port_2

    def get_groundstation_port_1(self):
        return self.groundstation_port_1

    def set_groundstation_port_1(self, groundstation_port_1):
        self.groundstation_port_1 = groundstation_port_1

    def get_groundstation_ip_addr(self):
        return self.groundstation_ip_addr

    def set_groundstation_ip_addr(self, groundstation_ip_addr):
        self.groundstation_ip_addr = groundstation_ip_addr

    def get_groundstation_controller_ip(self):
        return self.groundstation_controller_ip

    def set_groundstation_controller_ip(self, groundstation_controller_ip):
        self.groundstation_controller_ip = groundstation_controller_ip

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

    def get_baud_rate(self):
        return self.baud_rate

    def set_baud_rate(self, baud_rate):
        self.baud_rate = baud_rate

    def get_audio_line_driver(self):
        return self.audio_line_driver

    def set_audio_line_driver(self, audio_line_driver):
        self.audio_line_driver = audio_line_driver

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


def main(top_block_cls=TJ_groundstation_nogui_with_cntrl_and_IQ_streaming_autorun, options=None):

    tb = top_block_cls()
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
