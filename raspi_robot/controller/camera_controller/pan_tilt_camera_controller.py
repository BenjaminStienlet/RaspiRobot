
import time

from threading import Thread

from raspi_robot.controller.camera_controller.pan_camera_controller import PanCameraController


class PanTiltCameraController(PanCameraController):

    SERVO_ANGLE_INC_PS = 40
    SERVO_TIME_INTERVAL = 0.2
    SERVO_MULTIPLIER = 2

    def __init__(self, pan_servo, tilt_servo, pan_offset=0, tilt_offset=0):
        super(PanTiltCameraController, self).__init__(pan_servo, pan_offset)
        self.tilt_servo = tilt_servo
        self.tilt_offset = tilt_offset
        self.tilt_angle_diff = 0

        def tilt_servo_function():
            while self.tilt_servo_thread_is_alive:
                target_angle = self.tilt_servo_neutral_angle + self.tilt_angle_diff * self.tilt_servo_interval
                if self.tilt_servo.angle != target_angle:
                    if abs(target_angle - self.tilt_servo_neutral_angle) > abs(self.tilt_angle_diff * self.tilt_servo_interval):
                        multiplier = self.SERVO_MULTIPLIER
                    else:
                        multiplier = 1
                    if target_angle < self.tilt_servo.angle:
                        angle = self.tilt_servo.angle - multiplier * self.SERVO_ANGLE_INC_PS * self.SERVO_TIME_INTERVAL
                        if angle < target_angle:
                            angle = target_angle
                    else:
                        angle = self.tilt_servo.angle + multiplier * self.SERVO_ANGLE_INC_PS * self.SERVO_TIME_INTERVAL
                        if angle > target_angle:
                            angle = target_angle
                    self.tilt_servo.angle = angle
                time.sleep(self.SERVO_TIME_INTERVAL)

        self.tilt_servo_thread_is_alive = True
        self.tilt_servo_thread = Thread(target=tilt_servo_function)
        self.tilt_servo_thread.start()

    def move(self, move_dict):
        super(PanTiltCameraController, self).move(move_dict)
        self.tilt_angle_diff = move_dict["F"] - move_dict["B"]

    @property
    def tilt_servo_offset(self):
        return self._tilt_offset

    @tilt_servo_offset.setter
    def tilt_servo_offset(self, tilt_offset):
        self._tilt_offset = tilt_offset
        self.tilt_servo_neutral_angle = self.tilt_servo.neutral_angle + tilt_offset * min(
            self.tilt_servo.max_angle - self.tilt_servo.neutral_angle,
            self.tilt_servo.neutral_angle - self.tilt_servo.min_angle)
        self.tilt_servo_interval = min(self.tilt_servo.max_angle - self.tilt_servo_neutral_angle,
                                      self.tilt_servo_neutral_angle - self.tilt_servo.min_angle)

    def stop(self):
        super(PanTiltCameraController, self).stop()
        self.tilt_servo_thread_is_alive = False

