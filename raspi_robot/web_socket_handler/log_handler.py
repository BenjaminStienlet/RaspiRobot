
import json

from tornado.websocket import WebSocketHandler

from raspi_robot.log import Log


class LogHandler(WebSocketHandler):

    def open(self):
        self.opened = True
        Log.instance().add_info_message('WS log: new connection')
        Log.instance().register_observer(self)
        self.update()

    def on_message(self, message):
        Log.instance().add_check_message('WS log: message received %s' % message)
        self.update()

    def on_close(self):
        self.opened = False
        Log.instance().remove_observer(self)
        Log.instance().add_warning_message('WS log: connection closed')

    def update(self):
        if self.opened:
            msg = Log.instance().get_messages(self)
            if msg is not None:
                self.write_message(json.dumps(msg))