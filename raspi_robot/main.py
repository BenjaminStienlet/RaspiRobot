
from tornado.wsgi import WSGIContainer
from tornado.web import Application, FallbackHandler
from tornado.websocket import WebSocketHandler
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from raspi_robot.web_interface import WebInterface, app
from raspi_robot.web_socket_handlers.log_handler import LogHandler
from raspi_robot.robot import Robot
from raspi_robot.log import Log


robot = Robot()


def main():
    try:
        web_interface = WebInterface(robot)

        wsgi_app = WSGIContainer(app)

        application = Application([(r'/servo', ServoHandler), (r'/camera_servo', CameraServoHandler),
                                   (r'/motor', MotorHandler), (r'/log', LogHandler),
                                   (r'.*', FallbackHandler, {'fallback': wsgi_app})])

        # (r'/motor', MotorHandler, {'robot': robot})
        # class MotorHandler(WebSocketHandler):
        #   def __init__(self, *args, **kwargs):
        #       self.robot = kwargs.pop('robot')

        Log.instance().add_info_message('info')
        Log.instance().add_check_message('check')
        Log.instance().add_warning_message('warning')
        Log.instance().add_error_message('error')

        print "starting HTTP server"
        http_server = HTTPServer(application)
        http_server.listen(8080)
        IOLoop.instance().start()

    except (KeyboardInterrupt, SystemExit):
        print "exit"
        Log.instance().add_warning_message('Closing the application')


class ServoHandler(WebSocketHandler):

    def open(self):
        print 'WS servo: new connection'
        self.send_angle()

    def on_message(self, message):
        robot.steer_servo.angle = int(message)
        print 'WS servo: message received %s' % message
        self.send_angle()

    def on_close(self):
        print 'WS servo: connection closed'

    def send_angle(self):
        self.write_message(str(robot.steer_servo.angle))


class CameraServoHandler(WebSocketHandler):

    def open(self):
        print 'WS camera servo: new connection'
        self.send_angle()

    def on_message(self, message):
        robot.tilt_servo.angle = int(message)
        print 'WS camera servo: message received %s' % message
        self.send_angle()

    def on_close(self):
        print 'WS camera servo: connection closed'

    def send_angle(self):
        self.write_message(str(robot.tilt_servo.angle))


class MotorHandler(WebSocketHandler):

    def open(self):
        print 'WS motor: new connection'
        self.send_speed()

    def on_message(self, message):
        robot.motor.speed = int(message)
        print 'WS motor: message received %s' % message
        self.send_speed()

    def on_close(self):
        print 'WS motor: connection closed'

    def send_speed(self):
        self.write_message(str(robot.motor.speed))
