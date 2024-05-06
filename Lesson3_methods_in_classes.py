# %%
class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y
        c = self.x + self.y
        return c

# %%


pt1 = Point()
pt2 = Point()
print(pt1.set_coords(1, 2))
print(pt2.set_coords(3, 4))
