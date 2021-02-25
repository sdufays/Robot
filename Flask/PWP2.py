from flask import Flask, escape, request, render_template, Response
from robotClass import robot
import time
import picamera
import socket
import io
import logging
import datetime
import os

app=Flask(__name__)
from camera_pi import Camera
rc = robot()

# LOGGING STUFF
if os.path.exists("loggingfile.txt"):
  os.remove("loggingfile.txt")

with open("loggingfile.txt", "w+") as loggingfile:
    logFormatter = logging.Formatter("%(asctime)s [%(levelname)-5.5s] %(message)s")
    rootLogger = logging.getLogger()
    fileHandler = logging.FileHandler("loggingfile.txt")
    fileHandler.setFormatter(logFormatter)
    consoleHandler = logging.StreamHandler()
    rootLogger.addHandler(consoleHandler)
    rootLogger.addHandler(fileHandler)

outputFrame = None
vs = VideoStream(usePiCamera=1).start()
time.sleep(2.0)

def generate():
    global outputFrame
    while True:
        if outputFrame is None:
            continue
            # encode the frame in JPEG format
        (flag, encodedImage) = cv2.imencode(".jpg", outputFrame)
        # ensure the frame was successfully encoded
        if not flag:
            continue
        # yield the output frame in the byte format
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
            bytearray(encodedImage) + b'\r\n')

@app.route("/video_feed")
def video_feed():
	# return the response generated along with the specific media
	# type (mime type)
	return Response(generate(),
		mimetype = "multipart/x-mixed-replace; boundary=frame")

@app.route('/log_stream')
def log_stream():
    with open("loggingfile.txt", "r") as loggingfile:
        return "".join(loggingfile.readlines()[-25:])

#HOME HTML TEMPLATE
@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('home.html')

#CAMERA FUNCTIONS
def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @app.route('/video_feed')
# def video_feed():
#     """Video streaming route. Put this in the src attribute of an img tag."""
#     return Response(gen(Camera()),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')

# move the robot fwd
@app.route('/fwd', methods=['GET'])
def fwd():
    rc.forward(0.1, 30)
    return True

# move the robot rev
@app.route('/rev', methods=['GET'])
def rev():
    rc.reverse(0.1, 30)
    return True

# move the robot left
@app.route('/left', methods=['GET'])
def left():
    rc.left(0.05)
    return True

# move the robot right
@app.route('/right', methods=['GET'])
def right():
    rc.right(0.05)
    return True

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
