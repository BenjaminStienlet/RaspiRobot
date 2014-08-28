
import wiringpi2 as wiringpi

from raspi_robot.pins.pins.gpio_pins.gpio_pin import GPIOPin


class GPIOPWMPin(GPIOPin):

    DEFAULT_VALUE = 0
    MAX_VALUE = 100

    def __init__(self, pid, default_value=None, max_value=None):
        super(GPIOPWMPin, self).__init__(pid)

        if default_value is None:
            self.default_value = self.DEFAULT_VALUE
        else:
            self.default_value = default_value

        if max_value is None:
            self.max_value = self.MAX_VALUE
        else:
            self.max_value = max_value

        wiringpi.wiringPiSetupPhys()
        wiringpi.softPwmCreate(pid, self.default_value, self.max_value)

    def write(self, value):
        wiringpi.softPwmWrite(self.pid, int(value))

    def read(self):
        pass