import random


class Creature:

    def __init__(self, name, level=10):
        self.name = name
        self.level = level

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level

    def __repr__(self):
        return f"Creature: {self.name} of level {self.level}"


class Wizard(Creature):
    def __init__(self, name, level):
        super().__init__(name, level)

    def attack(self, creature):
        print(f'{self.name} attacks {creature.name}!')

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print(f'You roll {my_roll}...')
        print(f"{creature.name} rolls {creature_roll}")

        if my_roll >= creature_roll:
            print(f'{self.name} has handily triumphed over {creature.name}')
            return True
        else:
            print(f'{self.name} has been DEFEATED!!!!')


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        """Return a defensive roll. Uses base get_defensive_roll(), divided by 2"""
        return super().get_defensive_roll() / 2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breathes_fire):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breathes_fire = breathes_fire

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breathes_fire else 1
        scale_modifier = self.scaliness / 10

        return base_roll * fire_modifier * scale_modifier