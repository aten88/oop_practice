class Point:
    """Класс со свойствами и координатами."""
    color = 'red'
    circle = 2

    def print_color(self):
        return self.color

    class SubPoint:
        inject_attr = 10


a = Point()
b = Point()

a.color = 'green'
a.circle = 4

print(a.print_color())
print(b.print_color())
print(a.__dict__)
print(b.__dict__)

Point.coordinate_x = 0
Point.coordinate_y = 180

setattr(Point.SubPoint, 'inject_attr', 90)

print(Point.coordinate_x)
print(Point.SubPoint.inject_attr)
print(getattr(Point.SubPoint, 'inject_attra', False))

# del Point.coordinate_x
# delattr(Point, 'coordinate_y')

print(hasattr(Point, 'coordinate_x'))
print(hasattr(Point, 'coordinate_y'))
print(Point.__dict__)
print(Point.__doc__)
