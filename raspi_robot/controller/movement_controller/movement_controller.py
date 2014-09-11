
from abc import ABCMeta, abstractmethod


class MovementController(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def move(self, move_dict):
        pass

    @abstractmethod
    def stop(self):
        pass