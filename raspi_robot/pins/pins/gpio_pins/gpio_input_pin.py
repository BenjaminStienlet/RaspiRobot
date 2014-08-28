
import wiringpi2 as wiringpi

from raspi_robot.pins.pins.gpio_pins.gpio_pin import GPIOPin


class GPIOInputPin(GPIOPin):

    def __init__(self, pid):
        super(GPIOInputPin, self).__init__(pid)
        wiringpi.wiringPiSetupPhys()
        wiringpi.pinMode(pid, 0)

    def write(self, value):
        pass

    def read(self):
        return wiringpi.digitalRead(self.pid)
