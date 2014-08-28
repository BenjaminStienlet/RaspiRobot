"""
Invoke this test with the following arguments:
python raspi_robot.test.servo_test start end time continuous(0/1)
e.g. python -m raspi_robot.test.servo_test 24 158 0.1 1
"""

import sys
import time

from raspi_robot.robot import Robot


def test():
    arg = map(lambda x: float(x.strip("'")), sys.argv[1:])

    servo = Robot().tilt_servo

    if arg[3]:
        for i in range(int(arg[0]), int(arg[1])+1):
            print "angle: %s" % i
            servo.angle = i
            time.sleep(arg[2])
    else:
        servo.angle = int(arg[0])
        time.sleep(arg[2])
        servo.angle = int(arg[1])


if __name__ == '__main__':
    test()