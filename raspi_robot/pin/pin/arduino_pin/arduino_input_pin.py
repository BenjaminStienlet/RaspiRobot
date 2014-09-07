
from raspi_robot.pin.pin.arduino_pin.arduino_pin import ArduinoPin


class ArduinoInputPin(ArduinoPin):

    def __init__(self, pid):
        pin = self.BOARD.get_pin('d:%s:i' % pid)
        super(ArduinoInputPin, self).__init__(pid, pin)