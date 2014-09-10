
class Servo(object):

    def __init__(self, pin, angle, min_angle, max_angle):
        self.pin = pin
        self._angle = 0
        self.min_angle = min_angle
        self.max_angle = max_angle
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
        if angle < self.min_angle:
            angle = self.min_angle
        if angle > self.max_angle:
            angle = self.max_angle

        self._angle = angle
        self.pin.write(self.angle)
