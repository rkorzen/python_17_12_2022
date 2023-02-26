from abc import ABC, abstractmethod


class Food:
    calories: int = 100


class Animal(ABC):
    @abstractmethod
    def eat(self, food: Food) -> None:
        pass

    @abstractmethod
    def move(self) -> None:
        ...

    @abstractmethod
    def sleep(self) -> None:
        """Sleep - usually to get energy"""

    def voice(self):
        print(self.sound)


class Dog(Animal):
    energy = 100
    sound = "Bark"

    def eat(self, food: Food) -> None:
        self.energy += food.calories

    def move(self) -> None:
        print("Dog is running")
        self.energy -= 1

    def sleep(self) -> None:
        self.energy += 10
        print("Dog sleep")


class Doberman(Dog):
    energy = 120


def xxx(x: int):
    pass


def yyy():
    pass


# print(xxx + yyy)

print(xxx.__annotations__)
print(xxx.__name__)
