"""
Invoke this test with the following arguments:
python raspi_robot.test.motor_test start end time continuous(0/1)
e.g. python -m raspi_robot.test.servo_test 0 100 2 0
"""

import sys
import time

from raspi_robot.robot.robot_4wd import Robot4WD


def test():
    arg = map(lambda x: float(x.strip("'")), sys.argv[1:])

    motor = Robot4WD().motor

    if arg[3]:
        for i in range(int(arg[0]), int(arg[1])+1):
            print "speed: %s" % i
            motor.angle = i
            time.sleep(arg[2])
    else:
        motor.speed = int(arg[0])
        print "speed: %s" % motor.speed
        time.sleep(arg[2])
        motor.speed = int(arg[1])
        print "speed: %s" % motor.speed

    motor.speed = 0


if __name__ == '__main__':
    test()