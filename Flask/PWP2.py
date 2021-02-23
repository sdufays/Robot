from flask import Flask, escape, request, render_template, Response
from robotClass import robot
import time
import picamera
import socket
import io
import logging
import datetime
import os
import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera

if os.path.exists("loggingfile.txt"):
  os.remove("loggingfile.txt")

app = Flask(__name__)
from camera_pi import Camera
rc = robot()

with open("loggingfile.txt", "w+") as loggingfile:
    logFormatter = logging.Formatter("%(asctime)s [%(levelname)-5.5s] %(message)s")
    rootLogger = logging.getLogger()
    fileHandler = logging.FileHandler("loggingfile.txt")
    fileHandler.setFormatter(logFormatter)
    consoleHandler = logging.StreamHandler()
    rootLogger.addHandler(consoleHandler)
    rootLogger.addHandler(fileHandler)

#fwd 3, right 0.75, fwd 1.75, rev 0.8, right 0.75, fwd 3.05
# cap = cv2.VideoCapture(0)

@app.route('/log_stream')
def log_stream():
    with open("loggingfile.txt", "r") as loggingfile:
        return "".join(loggingfile.readlines()[-25:])

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('home.html')

camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(320, 240))

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
    image = frame.array
    rawCapture.truncate()
    rawCapture.seek(0)
    if process(rawCapture):
        break

@app.route('/video_feed')
def video_feed():
    #cap = cv2.VideoCapture('http://192.168.1.101:8080/')
    while(True):
        #ret, frame = cap.read()
        cv2.imshow('frame',image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    #cap.release()
    cv2.destroyAllWindows()

# move the robot fwd
@app.route('/fwd', methods=['GET'])
def fwd():
    rc.forward(0.1, 30)
    return ""

# move the robot rev
@app.route('/rev', methods=['GET'])
def rev():
    rc.reverse(0.1, 30)
    return ""

# move the robot left
@app.route('/left', methods=['GET'])
def left():
    rc.left(0.05)
    return ""

# move the robot right
@app.route('/right', methods=['GET'])
def right():
    rc.right(0.05)
    return ""

# run the predetermined course
@app.route('/run')
def run():
    a = request.args.get('a')
    b = request.args.get('b')
    c = request.args.get('c')
    d = request.args.get('d')
    e = request.args.get('e')
    f = request.args.get('f')
    rc.forward(float(a), 15)
    time.sleep(0.5)
    rc.right(float(b))
    time.sleep(0.5)
    rc.forward(float(c), 15)
    time.sleep(0.5)
    rc.reverse(float(d), 15)
    time.sleep(0.5)
    rc.right(float(e))
    time.sleep(0.5)
    rc.forward(float(f), 15)
    return "robot work yes"

app.run(host= '0.0.0.0', port=8080, debug=True, threaded=True)
# cap.release()
# cv2.destroyAllWindows()
