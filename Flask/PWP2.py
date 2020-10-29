from flask import Flask, escape, request
from robotClass import robot


app = Flask(__name__)

rc = robot()

@app.route('/')
def menu():
    print("192.168.1.116:8080/fwd")
    print("192.168.1.116:8080/rev")
    print("192.168.1.116:8080/left")
    print("192.168.1.116:8080/right")


# move the robot fwd
@app.route('/fwd')
def fwd():
    # rc.fwd(10)
    return 'moved fwd!'

# move the robot rev
@app.route('/rev')
def rev():
    # rc.rev(10)
    return 'moved rev!'

# move the robot left
@app.route('/left')
def left():
    # rc.left(10)
    return 'moved left!'

# move the robot right
@app.route('/right')
def right():
    # rc.right(10)
    return 'moved right!'



app.run(host= '0.0.0.0', port=8080)
