
from abc import ABCMeta, abstractmethod

from raspi_robot.pins.pins.pin import Pin


class GPIOPin(Pin):
    __metaclass__ = ABCMeta

    def __init__(self, pid):
        super(GPIOPin, self).__init__(pid)

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, value):
        pass