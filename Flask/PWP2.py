from flask import Flask, escape, request
from robotClass import robot
import time

app = Flask(__name__)
rc = robot()

#fwd 3, right 0.75, fwd 1.75, rev 0.8, right 0.75, fwd 3.05

@app.route('/')
def menu():
    return "http://192.168.1.116:8080/run?a=3&b=0.7&c=1.9&d=0.8&e=0.7&f=3.15"

# move the robot fwd
@app.route('/fwd')
def fwd():
    rc.forward(1, 15)
    return 'moved fwd!'

# move the robot rev
@app.route('/rev')
def rev():
    rc.reverse(1, 15)
    return 'moved rev!'

# move the robot left
@app.route('/left')
def left():
    a = request.args.get('a')
    rc.left(float(a))
    return 'moved left!'

# move the robot right
@app.route('/right')
def right():
    a = request.args.get('a')
    rc.right(float(a))
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



app.run(host= '0.0.0.0', port=8080)
