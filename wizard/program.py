import random
import time
from actors import Wizard, Creature, SmallAnimal, Dragon


def main():
    print_header()
    game_loop()


def print_header():
    print('--------------------------------------------------')
    print("                   WIZARD GAME APP")
    print('--------------------------------------------------')
    print()


def game_loop():

    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
       SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 75, True),
        Creature('Evil Wizard', 1000),
        Creature('Vermicious Knid', 13),
    ]

    hero = Wizard('Wizrobe', 75)

    while True:
        active_creature = random.choice(creatures)
        print(f'A {active_creature.name} of level {active_creature.level} has appeared from a dark and foggy forest...')
        cmd = input('Do you [a]ttack, [r]un away, or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print(f'{hero.name} runs and hides taking time to recover.')
                time.sleep(2)
                print(f'{hero.name} has been revitalized!')
        elif cmd == 'r':
            print(f'\n{hero.name} runs away!')
        elif cmd == 'l':
            print(f'\n{hero.name} looks around and sees:')

            for c in creatures:
                print(f'* A level {c.level} {c.name}')
        else:
            print('OK, exiting game... bye!')
            break


if __name__ == '__main__':
    main()