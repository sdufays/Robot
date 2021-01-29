from flask import Flask, escape, request, render_template, Response
from robotClass import robot
import time
import picamera
import cv2
import socket
import io

app = Flask(__name__)
rc = robot()
vc = cv2.VideoCapture(0)

#fwd 3, right 0.75, fwd 1.75, rev 0.8, right 0.75, fwd 3.05
@app.route('/stream')
def index(): 
   """Video streaming .""" 
   return render_template('index.html') 
def gen(): 
   """Video streaming generator function.""" 
   while True: 
       rval, frame = vc.read() 
       cv2.imwrite('pic.jpg', frame) 
       yield (b'--frame\r\n' 
              b'Content-Type: image/jpeg\r\n\r\n' + open('pic.jpg', 'rb').read() + b'\r\n') 
@app.route('/video_feed') 
def video_feed(): 
   """Video streaming route. Put this in the src attribute of an img tag.""" 
   return Response(gen(), 
                   mimetype='multipart/x-mixed-replace; boundary=frame') 


@app.route('/')
def home():
    return render_template("home.html")

# move the robot fwd
@app.route('/fwd', methods=['POST'])
def fwd():
    rc.forward(0.1, 30)
    return render_template("home.html")

# move the robot rev
@app.route('/rev', methods=['POST'])
def rev():
    rc.reverse(0.1, 30)
    return render_template("home.html")

# move the robot left
@app.route('/left', methods=['POST'])
def left():
    rc.left(0.05)
    return render_template("home.html")

# move the robot right
@app.route('/right', methods=['POST'])
def right():
    rc.right(0.05)
    return render_template("home.html")

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

app.run(host= '0.0.0.0', port=8080)
