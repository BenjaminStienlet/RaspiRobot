
from raspi_robot.pin.pin_layout.pin_layout import PinLayout
from raspi_robot.pin.pin.arduino_pin.arduino_input_pin import ArduinoInputPin
from raspi_robot.pin.pin.arduino_pin.arduino_output_pin import ArduinoOutputPin
from raspi_robot.pin.pin.arduino_pin.arduino_servo_pin import ArduinoServoPin
from raspi_robot.pin.pin.arduino_pin.arduino_pwm_pin import ArduinoPWMPin


class ArduinoPinLayout(PinLayout):

    def create_input_pin(self, pid):
        return ArduinoInputPin(pid)

    def create_output_pin(self, pid):
        return ArduinoOutputPin(pid)

    def create_servo_pin(self, pid):
        return ArduinoServoPin(pid)

    def create_pwm_pin(self, pid):
        return ArduinoPWMPin(pid)