from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 0

sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')
