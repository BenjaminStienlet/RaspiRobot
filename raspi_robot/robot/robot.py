
from abc import ABCMeta, abstractmethod


class Robot(object):

    __metaclass__ = ABCMeta

    def __init__(self, movement_controller, camera_controller):
        self.movement_controller = movement_controller
        self.camera_controller = camera_controller