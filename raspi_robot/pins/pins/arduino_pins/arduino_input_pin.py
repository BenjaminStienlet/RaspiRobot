
from raspi_robot.pins.pins.arduino_pins.arduino_pin import ArduinoPin


class ArduinoInputPin(ArduinoPin):

    def __init__(self, pid):
        pin = self.BOARD.get_pin('d:%s:i' % pid)
        super(ArduinoInputPin, self).__init__(pid, pin)