
from abc import ABCMeta
from pyfirmata import Arduino

from raspi_robot.pins.pins.pin import Pin


class ArduinoPin(Pin):
    __metaclass__ = ABCMeta

    BOARD = Arduino('/dev/ttyACM0')

    def __init__(self, pid, pin):
        super(ArduinoPin, self).__init__(pid)
        self.pin = pin

    def read(self):
        return self.pin.read()

    def write(self, value):
        self.pin.write(value)
