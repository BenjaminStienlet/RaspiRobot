
from abc import ABCMeta, abstractmethod


class PinLayout(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_input_pin(self, pid):
        pass

    @abstractmethod
    def create_output_pin(self, pid):
        pass

    @abstractmethod
    def create_servo_pin(self, pid):
        pass

    @abstractmethod
    def create_pwm_pin(self, pid):
        pass
