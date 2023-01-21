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

from math import pi, sqrt

class Circle:
    def __init__(self, r=1):
        self.r = r
    @property
    def area(self):
        return self.r ** 2 * pi

    @area.setter
    def area(self, value):
        self.r = sqrt(value/pi)

    @property
    def perimeter(self):
        return 2 * pi * self.r

    @perimeter.setter
    def perimeter(self, value):
        self.r = value / (2 * pi)

    @property
    def r(self):  # print(c.r)
        return self.__r

    # @r.getter
    # def r(self):
    #     return self._r
    @r.setter
    def r(self, value): # c.r = 10
        if value < 0: raise ValueError("Promien nie moze byc mniejszy niz 0")
        self.__r = value

if __name__ == "__main__":
    c = Circle()
    assert c.r == 1
    assert c.area == pi
    assert c.perimeter == 2 * pi

    # c.r = -10

    c.area = 12

    assert c.r == sqrt(12/pi)
    print(vars(c))

