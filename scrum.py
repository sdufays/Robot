import RPi.GPIO as gpio
import time

R1 = 17 #forward
R2 = 27 #reverse
R3 = 5 #enable
L1 = 23
L2 = 24
L3 = 6
L_MULT = 1.5
pins = [R1, R2, R3, L1, L2, L3]

class robot():
    def __init__(self):
        gpio.setwarnings(False)
        gpio.setmode(gpio.BCM)
        for i in pins:
            gpio.setup(i, gpio.OUT)
            gpio.output(i, gpio.LOW)
        self.LPWM = gpio.PWM(L3, 100)
        self.RPWM = gpio.PWM(R3, 100)

    def __del__(self):
        gpio.cleanup()

    def forward(self, runtime, speed):
        gpio.output(L1, False)
        gpio.output(L2, True)
        gpio.output(R1, True)
        gpio.output(R2, False)
        self.LPWM.start(speed*L_MULT)
        self.RPWM.start(speed)
        time.sleep(runtime)
        self.LPWM.stop
        self.RPWM.stop

    def reverse(self, runtime, speed):
        gpio.output(L1, True)
        gpio.output(L2, False)
        gpio.output(R1, False)
        gpio.output(R2, True)
        self.LPWM.start(speed*L_MULT)
        self.RPWM.start(speed)
        time.sleep(runtime)
        self.LPWM.stop
        self.RPWM.stop
    
    def left(self):
        gpio.output(L1, True)
        gpio.output(L2, False)
        gpio.output(R1, True)
        gpio.output(R2, False)
        self.LPWM.start(15*L_MULT)
        self.RPWM.start(15)
        time.sleep(0.5)
    
    def right(self):
        gpio.output(L1, False)
        gpio.output(L2, True)
        gpio.output(R1, False)
        gpio.output(R2, True)
        self.LPWM.start(15*L_MULT)
        self.RPWM.start(15)
        time.sleep(0.5)


if __name__ == "__main__":
    robot1 = robot()
    robot1.forward(3.2, 15)
    del robot1
