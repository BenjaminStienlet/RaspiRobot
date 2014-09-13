
import time

from threading import Thread

from raspi_robot.controller.camera_controller.camera_controller import CameraController


class PanCameraController(CameraController):

    SERVO_ANGLE_INC_PS = 40
    SERVO_TIME_INTERVAL = 0.2
    SERVO_MULTIPLIER = 2

    def __init__(self, pan_servo, pan_offset=0):
        self.pan_servo = pan_servo
        self.pan_offset = pan_offset
        self.pan_angle_diff = 0

        def pan_servo_function():
            while self.pan_servo_thread_is_alive:
                target_angle = self.pan_servo_neutral_angle + self.pan_angle_diff * self.pan_servo_interval
                if self.pan_servo.angle != target_angle:
                    if abs(target_angle - self.pan_servo_neutral_angle) > abs(self.pan_angle_diff * self.pan_servo_interval):
                        multiplier = self.SERVO_MULTIPLIER
                    else:
                        multiplier = 1
                    if target_angle < self.pan_servo.angle:
                        angle = self.pan_servo.angle - multiplier * self.SERVO_ANGLE_INC_PS * self.SERVO_TIME_INTERVAL
                        if angle < target_angle:
                            angle = target_angle
                    else:
                        angle = self.pan_servo.angle + multiplier * self.SERVO_ANGLE_INC_PS * self.SERVO_TIME_INTERVAL
                        if angle > target_angle:
                            angle = target_angle
                    self.pan_servo.angle = angle
                time.sleep(self.SERVO_TIME_INTERVAL)

        self.pan_servo_thread_is_alive = True
        self.pan_servo_thread = Thread(target=pan_servo_function)
        self.pan_servo_thread.start()

    def move(self, move_dict):
        self.pan_angle_diff = move_dict["R"] - move_dict["L"]

    @property
    def pan_servo_offset(self):
        return self._pan_offset

    @pan_servo_offset.setter
    def pan_servo_offset(self, pan_offset):
        self._pan_offset = pan_offset
        self.pan_servo_neutral_angle = self.pan_servo.neutral_angle + pan_offset * min(
            self.pan_servo.max_angle - self.pan_servo.neutral_angle,
            self.pan_servo.neutral_angle - self.pan_servo.min_angle)
        self.pan_servo_interval = min(self.pan_servo.max_angle - self.pan_servo_neutral_angle,
                                      self.pan_servo_neutral_angle - self.pan_servo.min_angle)

    def stop(self):
        self.pan_servo_thread_is_alive = False

