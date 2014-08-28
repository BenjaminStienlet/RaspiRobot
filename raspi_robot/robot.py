
from raspi_robot.components.servo import Servo
from raspi_robot.components.motor import Motor
from raspi_robot.components.distance_monitor import DistanceMonitor
from raspi_robot.pins.pin_layout.gpio_pin_layout import GPIOPinLayout


class Robot(object):

    ###ARDUINO###
    # PAN_PID = 10
    # TILT_PID = 11
    #
    # TRIG_PID = 12
    # ECHO_PID = 13
    #
    # LEFT_MOTOR_ENABLE_PID = 3
    # LEFT_MOTOR_ORIENTATION_PID = (4, 5)
    # RIGHT_MOTOR_ENABLE_PID = 6
    # RIGHT_MOTOR_ORIENTATION_PID = (7, 8)
    #
    #
    # def __init__(self):
    #     self.pin_layout = GPIOPinLayout()
    #     self.pan_servo = Servo(self.pin_layout.create_servo_pin(self.PAN_PID))
    #     self.tilt_servo = Servo(self.pin_layout.create_servo_pin(self.TILT_PID))
    #
    #     self. distance_monitor = DistanceMonitor(self.pin_layout.create_output_pin(self.TRIG_PID),
    #                                              self.pin_layout.create_input_pin(self.ECHO_PID))
    #
    #     self.left_motor = Motor(self.pin_layout.create_pwm_pin(self.LEFT_MOTOR_ENABLE_PID),
    #                             (self.pin_layout.create_output_pin(self.LEFT_MOTOR_ORIENTATION_PID[0]),
    #                              self.pin_layout.create_output_pin(self.LEFT_MOTOR_ORIENTATION_PID[1])))
    #     self.right_motor = Motor(self.pin_layout.create_pwm_pin(self.RIGHT_MOTOR_ENABLE_PID),
    #                             (self.pin_layout.create_output_pin(self.RIGHT_MOTOR_ORIENTATION_PID[0]),
    #                              self.pin_layout.create_output_pin(self.RIGHT_MOTOR_ORIENTATION_PID[1])))

    ###RASPBERRY PI###
    STEER_PID = 0
    TILT_PID = 1

    LIGHTS_PID = 5

    MOTOR_ENABLE_PID = 12
    MOTOR_ORIENTATION_PID = (8, 10)

    def __init__(self):
        self.pin_layout = GPIOPinLayout()
        self.steer_servo = Servo(self.pin_layout.create_servo_pin(self.STEER_PID))
        self.tilt_servo = Servo(self.pin_layout.create_servo_pin(self.TILT_PID))

        self.motor = Motor(self.pin_layout.create_pwm_pin(self.MOTOR_ENABLE_PID),
                           (self.pin_layout.create_output_pin(self.MOTOR_ORIENTATION_PID[0]),
                            self.pin_layout.create_output_pin(self.MOTOR_ORIENTATION_PID[1])))