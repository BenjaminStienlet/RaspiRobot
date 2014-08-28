
from raspi_robot.pins.pin_layout.pin_layout import PinLayout
from raspi_robot.pins.pins.gpio_pins.gpio_input_pin import GPIOInputPin
from raspi_robot.pins.pins.gpio_pins.gpio_output_pin import GPIOOutputPin
from raspi_robot.pins.pins.gpio_pins.gpio_pwm_pin import GPIOPWMPin
from raspi_robot.pins.pins.gpio_pins.gpio_servo_pin import GPIOServoPin


class GPIOPinLayout(PinLayout):

    def create_input_pin(self, pid):
        return GPIOInputPin(pid)

    def create_output_pin(self, pid):
        return GPIOOutputPin(pid)

    def create_servo_pin(self, pid):
        return GPIOServoPin(pid)

    def create_pwm_pin(self, pid):
        return GPIOPWMPin(pid)