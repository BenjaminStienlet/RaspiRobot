
from raspi_robot.pins.pins.arduino_pins.arduino_pin import ArduinoPin


class ArduinoOutputPin(ArduinoPin):

    def __init__(self, pid):
        pin = self.BOARD.get_pin('d:%s:o' % pid)
        super(ArduinoOutputPin, self).__init__(pid, pin)