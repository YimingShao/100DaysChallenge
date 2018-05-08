import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level


    def defensive_roll(self):
        roll = random.randint(1, 12)
        return roll * self.level


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breath_fire):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breath_fire=breath_fire

    def defensice_roll(self):
        roll = super().defensive_roll()
        value = roll * self.scaliness
        if self.breath_fire:
            value = value * 2

        return value


class Wizard(Creature):

    def attack(self, creature):
        my_roll = self.defensive_roll()
        their_roll = creature.defensive_roll()

        return my_roll >= their_roll


