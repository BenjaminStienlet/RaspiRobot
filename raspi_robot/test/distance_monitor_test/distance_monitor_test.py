"""
Invoke this test with the following arguments:
python raspi_robot.test.distance_monitor_test amount_of_measurements time_between_measurements
"""

import sys
import time

from raspi_robot.robot import Robot


def test():
    arg = map(lambda x: float(x.strip("'")), sys.argv[1:])

    robot = Robot()

    for i in range(int(arg[0])):
        measurement = robot.distance_monitor.get_value()
        print "value: %s" % measurement
        time.sleep(arg[1])


if __name__ == '__main__':
    test()