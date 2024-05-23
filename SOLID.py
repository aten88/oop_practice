# S - single responsobility principe(Принцип единой ответственности)
# O - open/close responsobility principe(Принцип открытости/закрытости)
# L - Barbara Liskov substitution principe(Принцип подстановки Барбары Л)
# I - Interface segregation principe(Приницип разделения интерфейсов)
# D - Dependencies inversions principe(Принцип инверсии зависимостей)

from abc import abstractmethod


# ПРИНЦИП ЕДИНОЙ ОТВЕТСТВЕННОСТИ:
class BadAuto:
    def __init__(self, brand, model, color, wheels, fuel_type, fuel_amount):
        self.brand = brand
        self.model = model
        self.color = color
        self.wheels = wheels
        self.fuel_amount = fuel_amount
        self.fuel_type = fuel_type

    def change_wheel(self, tire_type):
        self.wheels = tire_type
        print(f'Установлена {tire_type} резина.')

    def fill_up(self, amount):
        self.fuel_amount += amount
        print(f'Заправлено {amount} литров.')


lada = BadAuto('LADA', 'KALINA', 'cherry', 'summary', 'gasoline', 30)
lada.change_wheel('winter')
lada.fill_up(30)
print(lada.__dict__)
# noqa Данный пример НАРУШАЕТ принцип единой ответственности т.к в классе BadAuto реализованы 2 метода которые имеют разное назначение.


# Лучшее решение:
class BestAuto:
    def __init__(self, brand, model, color, wheels, fuel_type, fuel_amount):
        self.brand = brand
        self.model = model
        self.color = color
        self.wheels = wheels
        self.fuel_type = fuel_type
        self.fuel_amount = fuel_amount


class ChangeWhell():
    @staticmethod
    def change_wheel(auto, tire_type):
        auto.wheels = tire_type
        print(f'Установлена {tire_type} резина.')


class FillUp():
    @staticmethod
    def fill_up(auto, fuel, amount):
        auto.fuel_amount += amount
        print(f'Заправлено {amount} литров {fuel}.')


bentley = BestAuto(
    'Bentley', 'Continental', 'black', 'summary', 'gasoline', 30
)

ChangeWhell.change_wheel(bentley, 'winter')
FillUp.fill_up(bentley, 'gasoline', 30)
print(bentley.__dict__)


# ПРИНЦИП ОТКРЫТОСТИ/ЗАКРЫТОСТИ:
class AutoEcologyClass:
    def check_eco_class(auto):
        if auto.fuel_type == 'gasoline':
            return f'{auto.brand} {auto.model} имеет 4 класс экологичности'
        elif auto.fuel_type == 'diesel':
            return f'{auto.brand} {auto.model} имеет 3 класс экологичности'
        elif auto.fuel_type == 'hybrid':
            return f'{auto.brand} {auto.model} имеет 5 класс экологичности'


print(AutoEcologyClass.check_eco_class(lada))

# noqa Данный пример отражает нарушение принципа ОТКРЫТОСТИ/ЗАКРЫТОСТИ т.к не позволяет расширять функционал метода без его изменения.


# Лучшее решение:
FUELS_TYPE = {
    'gasoline': 4,
    'diesel': 3,
    'hybrid': 5,
    'electric': 6,
}


def check_eco_class(auto):
    if auto.fuel_type not in FUELS_TYPE:
        raise ValueError(
            f'{auto.brand} {auto.model} имеет неизвестный тип топлива '
            f'{auto.fuel_type}'
        )
    return (
        f'{auto.brand} {auto.model} имеет '
        f'{FUELS_TYPE[auto.fuel_type]} класс экологичности'
    )


porshe = BestAuto(
    'Porshe', 'Taycan', 'white', 'summary', 'hybrid', 60
)
delorean = BestAuto(
    'DeLorean', 'DMC12', 'white', 'summary', 'nuclear', 1
)

print(check_eco_class(porshe))
# print(check_eco_class(delorean))


# ПРИНЦИП ПОДСТАНОВКИ БАРБАРЫ ЛИСКОВ:
class Vehicle:
    def get_vin(self):
        return '---'


class Car(Vehicle):
    def get_vin(self):
        return 'car_vin123456789'


class Truck(Vehicle):
    def get_vin(self):
        return 'truck_vin123456789'


def get_vin_info(vehicle: Vehicle):
    return vehicle.get_vin()


vehicle1 = Vehicle()
car1 = Car()
truck1 = Truck()

print(get_vin_info(truck1))

# noqa В данных классах НАСЛЕДНИКАХ мы переопределяем метод СУПЕРКЛАССА чтобы в дальнейшем при обращении к методу СУПЕРКЛАССА
# noqa происходило обращение по цепочке вниз и вызову метода аналога внутри дочернего класса.


# Пример плохой реализации:
def get_vin_number(vehicle):
    if isinstance(vehicle, Vehicle):
        return '---'
    if isinstance(vehicle, Car):
        return 'car_vin123456789'

# noqa В данном примере мы вынуждены дополнять метод условиями с явным указанием класса сущности.


# ПРИНЦИП РАЗДЕЛЕНИЯ ИНТЕРФЕЙСОВ:
'''
В данном примере соблюден принцип разделения интерфейсов. Класс Transport
определяет общие методы start_engine и stop_engine, которые реализуются в
его наследниках Car и MotoBike. Это позволяет каждому из них иметь
собственную реализацию этих методов, соответствующую их специфике
(например, для запуска двигателя в машине используется кнопка "push_start",
а в мотоцикле - "kick_starter").
'''


class Transport:
    def start_engine(self, engine_state, action_for_start):
        pass

    def stop_engine(self, engine_state, action_for_stop):
        pass


class Car(Transport):
    def start_engine(self, engine_state, action_for_start):
        if action_for_start == 'push_start':
            engine_state = 'working'
            return print(f'Двигатель {engine_state}')
        else:
            raise Exception('Не удалось запустить двигатель')

    def stop_engine(self, engine_state, action_for_stop):
        if action_for_stop == 'push_stop':
            engine_state = 'stopped'
            return print(f'Двигатель {engine_state}')
        else:
            raise Exception('Не удалось остановить двигатель')


class MotoBike(Transport):

    def start_engine(self, engine_state, action_for_start):
        if action_for_start == 'kick_starter':
            engine_state = 'working'
            return print(f'Двигатель {engine_state}')
        else:
            raise Exception('Не удалось запустить двигатель')

    def stop_engine(self, engine_state, action_for_stop):
        if action_for_stop == 'stop_fuel':
            engine_state = 'stopped'
            return print(f'Двигатель {engine_state}')
        else:
            raise Exception('Не удалось остановить двигатель')


car1 = Car()
motobike1 = MotoBike()

car1.start_engine('stopped', 'push_start')
car1.stop_engine('working', 'push_stop')
motobike1.start_engine('stopped', 'kick_starter')
motobike1.stop_engine('working', 'stop_fuel')


# ПРИНЦИП ИНВЕРСИИ ЗАВИСИМОСТЕЙ:
# Пример ПЛОХОЙ реализации
class BadLamp():
    def turn_on(self):
        print('Лампа включена')

    def turn_off(self):
        print('Лампа выключена')


class BadPowerSwitch:
    def __init__(self, bad_lamp: BadLamp):
        self.bad_lamp = bad_lamp
        self.work = False

    def toggle(self):
        if self.work:
            self.bad_lamp.turn_off()
            self.work = False
        else:
            self.bad_lamp.turn_on()
            self.work = True


bad_lamp = BadLamp()
bad_switch = BadPowerSwitch(bad_lamp)
bad_switch.toggle()
bad_switch.toggle()


# Пример ХОРОШЕЙ реализации:
class Switchable:
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class Lamp(Switchable):
    def turn_on(self):
        print('Лампа включена')

    def turn_off(self):
        print('Лампа выключена')


class Radio(Switchable):
    def turn_on(self):
        print('Радио включено')

    def turn_off(self):
        print('Радио выключено')


class GoodPowerSwitch:
    def __init__(self, item: Switchable):
        if not isinstance(item, Switchable):
            raise Exception('Объект не является наследником Switchable')
        self.item = item
        self.work = False

    def toggle(self):
        if self.work:
            self.item.turn_off()
            self.work = False
        else:
            self.item.turn_on()
            self.work = True


radio = Radio()
switch = GoodPowerSwitch(radio)
switch.toggle()
switch.toggle()
lamp = BadLamp()
switch_lamp = GoodPowerSwitch(lamp)
switch_lamp.toggle()
switch_lamp.toggle()
'''
В данном примере Класс GoodPowerSwitch зависит от класса абстракции
Switchable тоесть данный класс может работать со всеми сущностями наследниками
класса Switchable
'''
