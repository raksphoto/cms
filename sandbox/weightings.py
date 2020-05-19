#! /usr/bin/env python3


def decibels(a: float, b: float) -> float:
    return 20*log(a/b)


def cents_to_ratio(x: float) -> float:
    return 2**(x/1200)


def log_weights_by_cents():
    for semitone in range(128):
        cents = semitone * 100
        freqs = cents_to_ratio(cents)
        print("{:3.0f} {:6.0f} {:10.4f}".format(semitone, cents, freqs))


def testbench():
    log_weights_by_cents()


if __name__ == "__main__":
    testbench()
