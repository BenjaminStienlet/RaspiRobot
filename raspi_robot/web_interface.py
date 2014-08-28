
from threading import Thread
from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


class WebInterface(object):

    socketio = SocketIO(app)

    namespace = "/robot"

    def __init__(self, robot):
        print "starting SocketIO"
        socketio_thread = Thread(target=self.socketio.run, args=(app, ), kwargs={"host": "0.0.0.0", "port": 8081})
        socketio_thread.start()
        print "socketIO started"

        self.robot = robot

    @socketio.on('connect', namespace=namespace)
    def connect(self):
        self.send_angle()

    @socketio.on('set_angle', namespace=namespace)
    def test_message(self, message):
        self.robot.tilt_servo.angle = int(message)
        self.send_angle()

    def send_angle(self):
        self.socketio.emit('set_angle', self.robot.tilt_servo.angle)