
from raspi_robot.controller.movement_controller.movement_controller import MovementController


class MotorServoMovementController(MovementController):

    move_motor_step = 10
    move_servo_step = 10

    def __init__(self, motor, servo, speed_offset=None, steering_offset=None, max_speed=None):
        super(MotorServoMovementController, self).__init__(speed_offset, steering_offset, max_speed)
        self.motor = motor
        self.servo = servo

    def move(self, move_dict):
        move_motor = move_dict["F"] - move_dict["B"]
        move_servo = move_dict["R"] - move_dict["L"]

        self.servo.angle += self.move_servo_step * move_servo
        self.motor.speed += self.move_motor_step * move_motor

        print "motor speed: %s, servo angle: %s" % (self.motor.speed, self.servo.angle)