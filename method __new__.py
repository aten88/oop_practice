class Point:
    def __new__(cls, *args, **kwargs):
        print('вызов __new__ для ' + str(cls))
        return super().__new__(cls)

    def __init__(self, x, y):
        print('вызов __init__ для ' + str(self))
        self.x = x
        self.y = y


pt = Point(1, 2)
print(pt)


# Пример паттерна Singleton


class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port

        def connect(self):
            print(f'Соединение с БД:{self.user}, {self.password}, {self.port}')

        def close(self):
            print('Закрытие соединения с БД.')

        def read(self):
            print('Чтение данных из БД.')

        def write(self):
            print('Запись данных в БД.')


db = DataBase('root', '1234', '8080')
db2 = DataBase('root2', '5678', '4040')
print(id(db), id(db2))
