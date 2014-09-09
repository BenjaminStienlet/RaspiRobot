
import time

from tornado.wsgi import WSGIContainer
from tornado.web import Application, FallbackHandler
from tornado.websocket import WebSocketHandler
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from raspi_robot.web_interface import WebInterface, app
from raspi_robot.web_socket_handler.log_handler import LogHandler
from raspi_robot.web_socket_handler.movement_handler import MovementHandler
from raspi_robot.robot.robot_4wd import Robot4WD
from raspi_robot.log import Log


robot = Robot4WD()


def main():
    try:
        WebInterface(robot)

        wsgi_app = WSGIContainer(app)

        application = Application([(r'/movement', MovementHandler, {'robot': robot}), (r'/log', LogHandler),
                                   (r'.*', FallbackHandler, {'fallback': wsgi_app})])

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
        time.sleep(2)
