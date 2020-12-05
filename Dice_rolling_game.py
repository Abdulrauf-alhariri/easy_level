import random


dice_2 = random.randint(1, 6)
answer = input('would you roll the dice? (Yes/ NO): ').lower()

if answer == 'yes':
    while answer == 'yes':
        dice_1 = random.randint(1, 6)
        answer = input(
            f'you got {dice_1}, do you want to roll the dice again? ').lower()

        if answer == 'no':
            print('Thats bad')
            break

else:
    print("That's bad")
