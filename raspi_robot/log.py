import threading
import inspect

from time import gmtime, strftime


class Log(object):

    __singleton_lock = threading.Lock()
    __singleton_instance = None
    __messages = []
    __observers = {}

    @classmethod
    def instance(cls):
        if not cls.__singleton_instance:
            with cls.__singleton_lock:
                if not cls.__singleton_instance:
                    cls.__singleton_instance = cls()
        return cls.__singleton_instance

    def __add_message(self, msg_type, msg):
        time = strftime("%H:%M:%S", gmtime())
        frm = inspect.stack()[2]
        mod = inspect.getmodule(frm[0])
        if msg is not None:
            message = {'type': msg_type, 'time': time, 'module': mod.__name__, 'description': msg}
            self.__messages.append(message)
            for observer in self.__observers.keys():
                self.__observers[observer].append(message)

    def add_info_message(self, msg):
        self.__add_message('info', msg)

    def add_warning_message(self, msg):
        self.__add_message('warning', msg)

    def add_error_message(self, msg):
        self.__add_message('error', msg)

    def add_check_message(self, msg):
        self.__add_message('check', msg)

    def get_messages(self, observer):
        if len(self.__messages) == 0:
            return None
        msg = self.__observers[observer]
        self.__observers[observer] = []
        return msg

    def register_observer(self, observer):
        if (observer is not None) and (not observer in self.__observers):
            self.__observers[observer] = self.__messages

    def remove_observer(self, observer):
        if observer is not None:
            del self.__observers[observer]

    def notify_observers(self):
        for observer in self.__observers:
            observer.update()