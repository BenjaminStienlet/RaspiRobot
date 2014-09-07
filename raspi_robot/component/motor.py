class Motor(object):

    MIN_SPEED = -100
    MAX_SPEED = 100

    def __init__(self, enable_pin, orientation_pins, speed=0):
        self.enable_pin = enable_pin
        self.orientation_pins = orientation_pins
        self._speed = 0
        self.speed = speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        if speed < self.MIN_SPEED:
            speed = self.MIN_SPEED
        if speed > self.MAX_SPEED:
            speed = self.MAX_SPEED

        self._speed = speed
        self.enable_pin.write(abs(self.speed))      # /100.0 removed -> arduino_pwm_pin

        if self.speed >= 0:
            self.orientation_pins[0].write(1)
            self.orientation_pins[1].write(0)
        else:
            self.orientation_pins[0].write(0)
            self.orientation_pins[1].write(1)