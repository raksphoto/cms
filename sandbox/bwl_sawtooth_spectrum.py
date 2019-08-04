#! /usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def bwl_sawtooth_analysis(test_freq, num_harm=24, zoom=False):
    # sampling setup
    samp_freq = 192000
    nyquist = samp_freq/2
    samp_seq = np.arange(samp_freq)

    # additive synthesis of sawtooth tone at test_freq
    samp_dat = np.zeros(samp_freq)
    for i in range(num_harm):
        j = i + 1
        sp, fp = 1/float(samp_freq), 1/(j * test_freq)
        samp_wave = (fp / sp)
        samp_arg = ((samp_seq % samp_wave) / samp_wave) * 2 * np.pi
        samp_dat += np.sin(samp_arg) / j

    # compute fft of the tone for samp_in_1s records
    spectrum = np.fft.fft(samp_dat)

    # get frequencies, compute power magnitude, normalize
    freq = np.fft.fftfreq(samp_seq.shape[-1], d=sp)
    abs_spectrum = np.abs(spectrum)**2
    ymax = max(abs_spectrum)
    norm_spectrum = abs_spectrum/ymax

    if zoom is True:
        # plot up to 24th harmonic
        max_harmonic = 24.0 * test_freq
        plt.xlim(-1*max_harmonic, max_harmonic)
        plt.xlabel("frequency to 24th harmonic")

    if zoom is False:
        # to nyquist
        plt.xlim(-1*nyquist, nyquist)
        plt.xlabel("frequency to nyquist limit")

    # plot spectrum results
    plt.grid(True)
    plt.yscale("log")
    plt.ylim(1E-06, 1.0)  # about 20-bits dynamic range
    plt.ylabel("normalized power magnitude")
    plt.plot(freq, norm_spectrum, "r-")
    plt.show()


if __name__ == "__main__":
    # harmonic evolution kept < nyquist
    bwl_sawtooth_analysis(440.0, 24, False)
    bwl_sawtooth_analysis(880.0, 24, False)
    bwl_sawtooth_analysis(1760.0, 24, False)
    bwl_sawtooth_analysis(3520.0, 24, False)
    bwl_sawtooth_analysis(7040.0, 13, False)
