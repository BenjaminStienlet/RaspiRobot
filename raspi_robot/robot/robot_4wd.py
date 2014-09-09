
from raspi_robot.component.servo import Servo
from raspi_robot.component.motor import Motor
from raspi_robot.pin.pin_layout.gpio_pin_layout import GPIOPinLayout
from raspi_robot.robot.robot import Robot
from raspi_robot.controller.movement_controller.motor_servo_movement_controller import MotorServoMovementController


class Robot4WD(Robot):

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

        movement_controller = MotorServoMovementController(self.motor, self.steer_servo)
        camera_controller = None

        super(Robot4WD, self).__init__(movement_controller, camera_controller)