# change the pins to the correct ones

import RPi.GPIO as gpio
import time

#17, 27, 5 - left motor
# 23, 24, 6 - Right motor

# init means initialize

class robot():
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        gpio.setmode(gpio.BCM)
        gpio.setup(a, gpio.OUT)
        gpio.setup(b, gpio.OUT)
        gpio.setup(c, gpio.OUT)
        gpio.setup(d, gpio.OUT)
        gpio.setup(e, gpio.OUT)
        gpio.setup(f, gpio.OUT)
        self.pwm_left = gpio.PWM(e, 100)
        self.pwm_right = gpio.PWM(f, 100)



    def forward(self, time, speed):
        gpio.output(self.a, True)
        gpio.output(self.b, False)
        self.pwm_left.start(speed)
        gpio.output(self.c, False)
        gpio.output(self.d, True)
        self.pwm_right.start(speed)
        time.sleep(time)

    def reverse(self, time, speed):
        gpio.output(self.a, False)
        gpio.output(self.b, True)
        self.pwm_left.start(speed)
        gpio.output(self.c, True)
        gpio.output(self.d, False)
        self.pwm_right.start(speed)
        time.sleep(time)


robot1 = robot(17, 27, 23, 24, 5, 6)
robot1.forward(1.35, 50)

gpio.cleanup()

# 17,27,23,24