# change the pins to the correct ones

import RPi.GPIO as gpio
import time

#17 and 27 - on motor
# 23 and 24 - another


# init means initialize
def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(13, gpio.OUT)
    gpio.setup(18, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(16, gpio.OUT)
    gpio.output(13, True)
    gpio.output(16, True)


# forward means to go forward
def forward(tf):
    gpio.output(11, True)
    gpio.output(16, False)
    time.sleep(tf)


def reverse(tf):
    gpio.output(11, False)
    gpio.output(16, True)
    time.sleep(tf)


init()
forward(0.5)
reverse(0.5)

gpio.cleanup()

# 17,27,23,24