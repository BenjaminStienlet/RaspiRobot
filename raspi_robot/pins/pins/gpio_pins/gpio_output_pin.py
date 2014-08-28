
import wiringpi2 as wiringpi

from raspi_robot.pins.pins.gpio_pins.gpio_pin import GPIOPin


class GPIOOutputPin(GPIOPin):
    def __init__(self, pid):
        super(GPIOOutputPin, self).__init__(pid)
        wiringpi.wiringPiSetupPhys()
        wiringpi.pinMode(pid, 1)

    def write(self, value):
        wiringpi.digitalWrite(self.pid, int(value))

    def read(self):
        pass
