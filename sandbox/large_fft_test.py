#! /usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    # populate samp_dat with 1 tone at test_freq, using samp_in_1s Fs
    samp_in_1s = 200000
    test_freq = 10000.0
    samp_seq = np.arange(samp_in_1s)
    sp, fp = 1/float(samp_in_1s), 1/test_freq
    samp_wave = fp/sp
    samp_arg = ((samp_seq % samp_wave) / samp_wave) * 2 * np.pi
    samp_dat = np.sin(samp_arg)

    # compute fft of the tone for samp_in_1s records
    spectrum = np.fft.fft(samp_dat)
    freq = np.fft.fftfreq(samp_seq.shape[-1], d=sp)
    
    print(samp_seq.shape[-1])
    
    # plot results, with some formatting for audio signals
    plt.xlabel("frequency")
    plt.ylabel("amplitude")
    plt.xlim(-20000, 20000)
    plt.plot(freq, spectrum.real, freq, spectrum.imag)
    plt.show()
