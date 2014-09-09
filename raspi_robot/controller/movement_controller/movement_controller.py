
from abc import ABCMeta, abstractmethod


class MovementController(object):

    __metaclass__ = ABCMeta

    def __init__(self, speed_offset, steering_offset, max_speed):
        if speed_offset is not None:
            self.speed_offset = speed_offset
        else:
            self.speed_offset = 0

        if steering_offset is not None:
            self.steering_offset = steering_offset
        else:
            self.steering_offset = 0

        if max_speed is not None:
            self.max_speed = max_speed
        else:
            self.max_speed = 1

    @abstractmethod
    def move(self, move_dict):
        pass