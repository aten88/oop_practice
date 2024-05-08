class Point:
    color = 'red'
    circle = 2

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print(f'Удаление обьекта {self}')

    def set_coords(self, x, y):
        self.x = x
        self.y = y
        return self.x + self.y

    def get_coords(self):
        return self.x, self.y


pt = Point()

print(pt.__dict__)
