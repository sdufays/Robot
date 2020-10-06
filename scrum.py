# change the pins to the correct ones

import RPi.GPIO as gpio
import time

#17 and 27 - left motor
# 23 and 24 - Right motor

# init means initialize

class robot():
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        gpio.setmode(gpio.BCM)
        gpio.setup(a, gpio.OUT)
        gpio.setup(b, gpio.OUT)
        gpio.setup(c, gpio.OUT)
        gpio.setup(d, gpio.OUT)
        # gpio.output(b, True)
        # gpio.output(c, True)


    def forward(self, tf):
        gpio.output(self.a*1.2, True)
        gpio.output(self.b*1.2, False)
        gpio.output(self.c, False)
        gpio.output(self.d, True)
        time.sleep(tf)

    def reverse(self, tf):
        gpio.output(self.a, False)
        gpio.output(self.b, True)
        gpio.output(self.c, True)
        gpio.output(self.d, False)
        time.sleep(tf)


robot1 = robot(17, 27, 23, 24)
robot1.forward(1.35)
# robot.reverse(0.9)

gpio.cleanup()

# 17,27,23,24