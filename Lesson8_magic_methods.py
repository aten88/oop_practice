class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattribute__(self, item):
        if item == 'x':
            raise ValueError('Доступ к атрибуту "X" запрещен!')
        else:
            print("Сработал __getattribute__")
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError(
                f'Создание атрибута с именем {key} запрещено!'
            )
        else:
            return object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item == 'x':
            raise AttributeError(
                f'Удаление атрибута с именем {item} запрещено!'
            )
        else:
            object.__delattr__(self, item)


pt1 = Point(1, 2)
pt2 = Point(10, 20)
del pt1.x
