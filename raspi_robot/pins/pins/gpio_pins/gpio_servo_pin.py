
import os

from raspi_robot.pins.pins.gpio_pins.gpio_pin import GPIOPin


class GPIOServoPin(GPIOPin):
    """
    =================================================
                      SERVOBLASTER
    =================================================

    The driver creates a device file, /dev/servoblaster,
    in to which you can send commands.
    The command format is:

        <servo-number>=<servo-position>

    =================================================

      Servo number    GPIO number   Physical number
          0               4             7
          1              17             11
          2              18             12
          3             21/27           13
          4              22             15
          5              23             16
          6              24             18
          7              25             22

    =================================================
    """

    def __init__(self, pid):
        super(GPIOServoPin, self).__init__(pid)

    def write(self, value):
        command = "echo %d=%d > /dev/servoblaster" % (self.pid, value)
        os.system(command)

    def read(self):
        pass