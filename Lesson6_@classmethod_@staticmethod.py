class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_coords(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x*x + y*y


v = Vector(1, 2)
print(Vector.get_coords(v))
print(Vector.validate(5))
