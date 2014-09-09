
import json

from tornado.websocket import WebSocketHandler

from raspi_robot.log import Log


class MovementHandler(WebSocketHandler):

    def __init__(self, *args, **kwargs):
        self.robot = kwargs.pop('robot')
        super(MovementHandler, self).__init__(*args, **kwargs)

    def open(self):
        Log.instance().add_info_message('WS movement: new connection')

    def on_message(self, message):
        Log.instance().add_check_message('WS movement: message received %s' % message)
        move_dict = json.loads(message)
        self.robot.movement_controller.move(move_dict)

    def on_close(self):
        Log.instance().add_warning_message('WS movement: connection closed')