from main import Mario, IStriker, Unit, Warrior, Zealot


class MarioStrikerAdapter(Mario, IStriker):

    def __init__(self, mario: Mario):
        super().__init__()
        self.mario = mario

    def attack(self, target: Unit) -> None:
        target.health -= self.mario.attackJump()


if __name__ == "__main__":

    warrior = Warrior()
    zealot = Zealot()
    mario = Mario()

    mario_adaptee = MarioStrikerAdapter(mario)

    warrior.attack(zealot)
    mario_adaptee.attack(warrior)

    warrior.attack(mario_adaptee)
    zealot.attack(mario_adaptee)
