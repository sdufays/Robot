# change the pins to the correct ones

import RPi.GPIO as gpio
import time

#17 and 27 - left motor
# 23 and 24 - Right motor

# init means initialize

class robot():
    def __init__(self, a, b, c, d):
        gpio.setmode(gpio.BCM)
        gpio.setup(a, gpio.OUT)
        gpio.setup(b, gpio.OUT)
        gpio.setup(c, gpio.OUT)
        gpio.setup(d, gpio.OUT)
        # gpio.output(b, True)
        # gpio.output(c, True)


    def forward(tf):
        gpio.output(a, True)
        gpio.output(b, False)
        gpio.output(c, False)
        gpio.output(d, True)
        time.sleep(tf)

    def reverse(tf):
        gpio.output(a, False)
        gpio.output(b, True)
        gpio.output(c, True)
        gpio.output(d, False)
        time.sleep(tf)


robot1 = robot(17, 27, 23, 24)
robot1.forward(1.35)
# robot.reverse(0.9)

gpio.cleanup()

# 17,27,23,24