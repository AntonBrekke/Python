class Point:
    def __init__(self, x, y):
        self.coor = (x, y)
        # self._x = x
        # self._y = y

    def get_coordinates(self):
        return self.coor #self._x, self._y

# Intended usage (Vil funke når vi endrer fra self._x og self._y til self.coor)
p0 = Point(3,4)
x0, y0 = p0.get_coordintes()
print(x0,y0)

# Unintended usage (Vil ikke funke for endringen)
p1 = Point(0,1)
x1 = p1._x
y1 = p1._y
print(x1,y1)
