
from abc import ABCMeta, abstractmethod


class Pin(object):
    __metaclass__ = ABCMeta

    def __init__(self, pid):
        self.pid = pid

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, value):
        pass