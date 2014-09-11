
import time

from threading import Thread

from raspi_robot.controller.movement_controller.movement_controller import MovementController


class MotorServoMovementController(MovementController):
    """
    This class is a movement controller for a car which uses a motor and a servo.

    Attributes:
    * motor
    * servo
    * speed_offset: float [-1, 1]
    * steering_offset: float [-1, 1]
    * max_speed: float [0, 1]
    """

    MOTOR_SPEED_INC_PS = 30
    MOTOR_TIME_INTERVAL = 0.2

    SERVO_ANGLE_INC_PS = 40
    SERVO_TIME_INTERVAL = 0.2
    SERVO_MULTIPLIER = 2

    def __init__(self, motor, servo, speed_offset=0, steering_offset=0, max_speed=1):
        self.motor = motor
        self.servo = servo

        #TODO: change function for offset
        self.speed_offset = speed_offset
        self.steering_offset = steering_offset
        self.max_speed = max_speed

        self.speed_diff = 0
        self.angle_diff = 0

        def motor_function():
            while self.motor_thread_is_alive:
                target_speed = self.speed_diff * self.motor.MAX_SPEED * self.max_speed
                if self.motor.speed != target_speed:
                    if target_speed < self.motor.speed:
                        speed = self.motor.speed - self.MOTOR_SPEED_INC_PS * self.MOTOR_TIME_INTERVAL
                    else:
                        speed = self.motor.speed + self.MOTOR_SPEED_INC_PS * self.MOTOR_TIME_INTERVAL
                    if abs(speed) > abs(target_speed):
                        speed = target_speed
                    self.motor.speed = speed
                time.sleep(self.MOTOR_TIME_INTERVAL)

        self.motor_thread_is_alive = True
        self.motor_thread = Thread(target=motor_function)
        self.motor_thread.start()

        def servo_function():
            while self.servo_thread_is_alive:
                target_angle = self.servo_neutral_angle + self.angle_diff * self.servo_interval
                if self.servo.angle != target_angle:
                    if abs(target_angle - self.servo_neutral_angle) > abs(self.angle_diff * self.servo_interval):
                        multiplier = self.SERVO_MULTIPLIER
                    else:
                        multiplier = 1
                    if target_angle < self.servo.angle:
                        angle = self.servo.angle - multiplier * self.SERVO_ANGLE_INC_PS * self.SERVO_TIME_INTERVAL
                        if angle < target_angle:
                            angle = target_angle
                    else:
                        angle = self.servo.angle + multiplier * self.SERVO_ANGLE_INC_PS * self.SERVO_TIME_INTERVAL
                        if angle > target_angle:
                            angle = target_angle
                    self.servo.angle = angle
                time.sleep(self.SERVO_TIME_INTERVAL)

        self.servo_thread_is_alive = True
        self.servo_thread = Thread(target=servo_function)
        self.servo_thread.start()

    def move(self, move_dict):
        self.speed_diff = move_dict["F"] - move_dict["B"]
        self.angle_diff = move_dict["R"] - move_dict["L"]

    def stop(self):
        self.motor_thread_is_alive = False
        self.servo_thread_is_alive = False

    @property
    def steering_offset(self):
        return self._steering_offset

    @steering_offset.setter
    def steering_offset(self, steering_offset):
        self._steering_offset = steering_offset
        self.servo_neutral_angle = self.servo.neutral_angle + steering_offset * min(self.servo.max_angle -
                                                                                    self.servo.neutral_angle,
                                                                                    self.servo.neutral_angle -
                                                                                    self.servo.min_angle)
        self.servo_interval = min(self.servo.max_angle - self.servo_neutral_angle,
                                  self.servo_neutral_angle - self.servo.min_angle)

