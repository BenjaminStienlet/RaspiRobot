
class Servo(object):

    MIN_ANGLE = 0       #24
    MAX_ANGLE = 1023    #158

    def __init__(self, pin, angle=0):
        self.pin = pin
        self._angle = 0
        self.angle = angle

    def turn_left(self, angle):
        self.angle -= angle

    def turn_right(self, angle):
        self.angle += angle

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, angle):
        if angle < self.MIN_ANGLE:
            angle = self.MIN_ANGLE
        if angle > self.MAX_ANGLE:
            angle = self.MAX_ANGLE

        self._angle = angle
        self.pin.write(self.angle)
