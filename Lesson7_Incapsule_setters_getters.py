from accessify import private


class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y

    @private
    @classmethod
    def check_value(cls, value):
        return type(value) in (int, float)

    def set_coords(self, x, y):
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Invalid coordinates")

    def get_coords(self):
        return self.__x, self.__y


pt = Point(1, 2)
pt.set_coords(10, 20)
print(pt.get_coords())
print(pt.check_value(5))
