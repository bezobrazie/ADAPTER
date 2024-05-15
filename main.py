from abc import abstractmethod, ABC


class Unit(ABC):
    def __init__(self):
        self.health = 100


class IStriker(ABC):
    @abstractmethod
    def attack(self, target: Unit) -> None:
        ...


class Warrior(Unit, IStriker):
    def attack(self, target: Unit):
        target.health -= 6


class Zealot(Unit, IStriker):
    def attack(self, target: Unit):
        target.health -= 8


class Mario(Unit):

    def attackJump(self):
        print('Mamamia!')
        return 3
