import random

print('--------------------------------------------------')
print("                   GUESS THAT NUMBER GAME")
print('--------------------------------------------------')
print()

the_number = random.randint(0, 100)
guess = 0

while guess != the_number:
    guess = int(input('Guess a number between 0 and 100: '))
    if guess < the_number:
        print(f"{guess} was too low")
    elif guess > the_number:
        print(f"{guess} was too high")
    else:
        print('you win')
