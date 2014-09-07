from abc import ABCMeta, abstractmethod


class CameraController(object):

    __metaclass__ = ABCMeta

    def __init__(self, horizontal_offset, vertical_offset):
        self.horizontal_offset = horizontal_offset
        self.vertical_offset = vertical_offset
        self.max_speed = 1

    @abstractmethod
    def move(self, move_dict):
        pass