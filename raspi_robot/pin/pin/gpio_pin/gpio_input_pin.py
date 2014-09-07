
import wiringpi2 as wiringpi

from raspi_robot.pin.pin.gpio_pin.gpio_pin import GPIOPin


class GPIOInputPin(GPIOPin):

    def __init__(self, pid):
        super(GPIOInputPin, self).__init__(pid)
        wiringpi.wiringPiSetupPhys()
        wiringpi.pinMode(pid, 0)

    def write(self, value):
        pass

    def read(self):
        return wiringpi.digitalRead(self.pid)
