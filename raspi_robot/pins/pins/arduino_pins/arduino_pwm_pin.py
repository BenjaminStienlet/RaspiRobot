
from raspi_robot.pins.pins.arduino_pins.arduino_pin import ArduinoPin


class ArduinoPWMPin(ArduinoPin):

    def __init__(self, pid):
        pin = self.BOARD.get_pin('d:%s:p' % pid)
        super(ArduinoPWMPin, self).__init__(pid, pin)

    def write(self, value):
        self.pin.write(value/100.0)