
from abc import ABCMeta, abstractmethod


class MotorController(object):

    __metaclass__ = ABCMeta

    def __init__(self, speed_offset, steering_offset):
        self.speed_offset = speed_offset
        self.steering_offset = steering_offset
        self.max_speed = 1

    @abstractmethod
    def move(self, move_dict):
        pass