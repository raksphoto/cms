#! /usr/bin/env python3


def decibels(a: float, b: float) -> float:
    return 20*log(a/b)


def cents_to_ratio(x: float) -> float:
    return 2**(x/1200)


def log_weights_by_cents():
    sstr, cstr = "semitone".rjust(8), "cents".rjust(7)
    fstr = "f-ratio".rjust(17)
    work = sstr + cstr + fstr
    print(work)
    for semi in range(1, 128):
        cents = semi * 100
        freqs = cents_to_ratio(cents)
        fstr = "{:8.0f} {:6.0f} {:16.10f}".format(semi, cents, freqs)
        print(fstr)


def testbench():
    log_weights_by_cents()


if __name__ == "__main__":
    testbench()
