#! /usr/bin/env python3


def log_weights_by_cents():
    for i in range(128):
        cents = (i * 100) / 1200
        print("{:3.0f} {:10.4f}".format(i, cents))


def testbench():
    log_weights_by_cents()


if __name__ == "__main__":
    testbench()
