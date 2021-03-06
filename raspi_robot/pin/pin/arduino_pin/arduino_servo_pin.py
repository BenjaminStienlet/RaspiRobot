
from raspi_robot.pin.pin.arduino_pin.arduino_pin import ArduinoPin


class ArduinoServoPin(ArduinoPin):

    def __init__(self, pid):
        pin = self.BOARD.get_pin('d:%s:s' % pid)
        super(ArduinoServoPin, self).__init__(pid, pin)