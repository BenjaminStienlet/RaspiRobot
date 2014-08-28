
import threading
import time


class DistanceMonitor(object):

    _lock = threading.Lock()

    def __init__(self, trig_pin, echo_pin):
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin

        # Trigger duration
        self.trig_duration = 0.0001

        # Timeout on echo signal
        self.int_timeout = 2100

        # Speed of sound in m/s
        self.v_snd = 340.29

        self.time_between_measurements = 0.06

    def _get_one_value(self):
        with self._lock:
            self.trig_pin.write(1)
            time.sleep(self.trig_duration)
            self.trig_pin.write(0)

            countdown_high = self.int_timeout
            while self.echo_pin.read() == 0 and countdown_high > 0:
                countdown_high -= 1

            if countdown_high > 0:
                echo_start = time.time()

                countdown_low = self.int_timeout
                while self.echo_pin.read() == 1 and countdown_low > 0:
                    countdown_low -= 1

                echo_end = time.time()
                echo_duration = echo_end - echo_start

            time.sleep(self.time_between_measurements)

            if countdown_high > 0 and countdown_low > 0:
                return echo_duration * self.v_snd * 50
            else:
                return -1

    def get_value(self):
        measurements = []
        for i in range(10):
            distance = self._get_one_value()
            if distance > 0:
                measurements.append(distance)

        length = len(measurements)
        middle = int(length / 2)
        if length == 0:
            return -1
        if length % 2 != 0:
            return measurements[middle]
        else:
            return (measurements[middle-1] + measurements[middle]) / 2