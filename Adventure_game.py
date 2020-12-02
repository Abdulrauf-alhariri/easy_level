import time

answer = input('Whould you like to play? (Yes/ no) ')

if answer.lower().strip() == 'yes':
    answer = input('you reach a crossroad, would you right or left?')

    if answer.lower().strip() == 'left':
        answer = input(
            'To the right you see a monster and to the left a beatiful woman? Where to go?').lower()
        if answer == 'right':
            answer = input('you reach a monster, would you (run/ attack)? ')

            if answer == 'attack':
                print('Bad choice, you lose.')

            else:
                print('Clever, good choice')
                answer = input('you see a car and a plane. What to take? ')
                if answer == 'plane':
                    print("Bad choice, you can't fly. The sky is full of monsters")

                    print('Take the car, and go the further you can')
                elif answer == 'car':
                    print("Run a7oi ammer!!")
                    time.sleep(3)
                    print("Look out! The monster is straight behind your car")
                    time.sleep(1)
                    print("Shhhhh", "The car is down, you should survive on feets")
                    print('')
                    print("Good luck, brother")
        elif answer == 'left':
            print("ya 7arof, mozah hä!")
            print('')
            answer = input(
                "Do you want to whish anything from the mozah or just go to her? (whish/go):").lower()
            if answer == 'whish':
                print("Bad choice, it will make you a whish")
                print('Good luck bby😉, if you still alive!')
            else:
                print('Ya 7arof')
                print('')
                print("Your dead")

    else:
        print("Lucky, you passed succesfuly the monster, keep going and you'll find the treasure")

else:
    print("That's so bad")
