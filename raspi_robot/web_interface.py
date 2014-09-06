
from threading import Thread
from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit

import socket


app = Flask(__name__)

ip_addr = socket.gethostbyname(socket.getfqdn())

@app.route('/')
def index():
    return render_template('index.html', ip_addr=ip_addr)

@app.route('/log.html')
def log():
    return render_template('log.html', ip_addr=ip_addr)

@app.route('/settings.html')
def settings():
    return render_template('settings.html', ip_addr=ip_addr)


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