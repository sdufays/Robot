from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180

sleep(5)
camera.capture('/home/pi/image.jpg')
