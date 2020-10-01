# change the pins to the correct ones

import RPi.GPIO as gpio
import time

#17 and 27 - on motor
# 23 and 24 - another


# init means initialize
def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(27, gpio.OUT)
    gpio.setup(24, gpio.OUT)
    gpio.setup(17, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.output(27, True)
    gpio.output(23, True)


# forward means to go forward
def forward(tf):
    gpio.output(17, True)
    gpio.output(23, False)
    time.sleep(tf)


def reverse(tf):
    gpio.output(17, False)
    gpio.output(23, True)
    time.sleep(tf)


init()
forward(0.5)
reverse(0.5)

gpio.cleanup()

# 17,27,23,24