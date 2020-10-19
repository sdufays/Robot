import RPi.GPIO as gpio
import time

#17, 27, 5 - left motor
# 23, 24, 6 - Right motor

class robot():
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        gpio.setwarnings(False)
        gpio.setmode(gpio.BCM)
        gpio.setup(a, gpio.OUT)
        gpio.setup(b, gpio.OUT)
        gpio.setup(c, gpio.OUT)
        gpio.setup(d, gpio.OUT)
        gpio.setup(e, gpio.OUT)
        gpio.setup(f, gpio.OUT)
        self.pwm_left = gpio.PWM(e, 100)
        self.pwm_right = gpio.PWM(f, 100)

    def forward(self, tf, speed):
        gpio.output(self.a, True)
        gpio.output(self.b, False)
        gpio.output(self.c, False)
        gpio.output(self.d, True)
        self.pwm_left.start(speed*1.38)
        self.pwm_right.start(speed)
        time.sleep(tf)
        self.pwm_left.stop
        self.pwm_right.stop


    def reverse(self, tf, speed):
        gpio.output(self.a, False)
        gpio.output(self.b, True)
        gpio.output(self.c, True)
        gpio.output(self.d, False)
        self.pwm_left.start(speed*1.38)
        self.pwm_right.start(speed)
        time.sleep(tf)
        self.pwm_left.stop
        self.pwm_right.stop


robot1 = robot(17, 27, 23, 24, 5, 6)
robot1.forward(3.2, 15)

gpio.cleanup()
