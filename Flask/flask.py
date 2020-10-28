from flask import Flask
from robotClass import robot


app = Flask(__name__)

rc = robot()

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return escape(name)


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
