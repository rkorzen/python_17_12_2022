"""

Stwórz klasę Circle, która działa tak:


c = Circle()
c.radius # 1
c.diameter # 2
c.perimeter # 2 * Pi * 1
c.area      # pi * 1 ** 2

c.area = 5
c.perimeter = 10
c.radius # nowy promien

c.radius = 12


c = Cricle(-10)
ValueError


"""

from math import pi

class Circle:
    def __init__(self, r=1):
        self.r = r
    @property
    def area(self):
        return self.r ** 2 * pi

    @area.setter
    def area(self, value):

    @property
    def perimeter(self):
        return 2 * pi * self.r

