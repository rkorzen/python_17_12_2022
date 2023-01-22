"""
Stwórz klasę abstrakcyjną 'Shape' z metodami 'get_area()' i 'get_perimeter()'.
Stwórz klasy dziedziczące "Circle", "Rectangle" i "Square", które implementują metody z klasy abstrakcyjnej "Shape".
Stwórz kilka obiektów klas dziedziczących i wywołaj metody "get_area()" i "get_perimeter()" dla każdego z nich.
Wypisz wyniki na ekranie.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        ...

    @abstractmethod
    def get_perimeter(self):
        ...

    # @staticmethod
    # @abstractmethod
    # def costam():
    #     pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side**2

    def get_perimeter(self):
        return self.side * 4


s = Square(1)
