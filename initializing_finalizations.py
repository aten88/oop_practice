class Point:
    color = 'red'
    circle = 2

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __del__(self):
        print(f'Удаление обьекта {self}')

    def set_coords(self, x, y):
        self.x = x
        self.y = y
        print('Вызов метода set_coords')

    def get_coords(self):
        return self.x, self.y


pt = Point(0, 0)

c = 5 + pt.x
