from flask import Flask, escape, request, render_template, Response
from robotClass import robot
import time
import cv2

app = Flask(__name__)
rc = robot()

#fwd 3, right 0.75, fwd 1.75, rev 0.8, right 0.75, fwd 3.05

@app.route('/')
def home():
    return render_template("home.html")

# move the robot fwd
@app.route('/fwd')
def fwd():
    rc.forward(0.1, 30)
    return 'moved fwd!'

# move the robot rev
@app.route('/rev')
def rev():
    rc.reverse(0.1, 30)
    return 'moved rev!'

# move the robot left
@app.route('/left')
def left():
    rc.left(0.05)
    return 'moved left!'

# move the robot right
@app.route('/right')
def right():
    rc.right(0.05)
    return 'moved right!'

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

@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

def gen():
    camera = cv2.VideoCapture(0)

    while True:
        ret, img = camera.read()

        if ret:
            frame = cv2.imencode('.jpg', img)[1].tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        else:
            break


app.run(host= '0.0.0.0', port=8080)
