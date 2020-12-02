import random


def system(choicese):
    chocie = random.choice(choicese)
    return chocie


def user(choicese):
    print("1. Rock")
    print("")
    print("2. Paper ")
    print("")
    print("3. Scissor ")
    print("\n")

    choice = input("Enter the nr of your choice? ")

    if choice == "1":
        choice = choicese[0]

    elif choice == "2":
        choice = choicese[1]

    else:
        choice = choicese[2]
    return choice


def play():
    user_points = 0
    system_points = 0
    choicese = ["Rock", "Paper", "Scissor"]
    round = 1
    print("Rock vs Paper vs Scissor")
    print("")
    rounds = int(input("How many rounds? "))
    print("\n")

    while round <= rounds:
        round += 1
        system_choice = system(choicese)
        user_choice = user(choicese)

        if user_choice == "Rock" and system_choice == "Scissor":
            user_points += 1

        elif user_choice == "Paper" and system_choice == "Rock":
            user_points += 1

        elif user_choice == "Scissor" and system_choice == "Paper":
            user_points += 1

        elif user_choice == system_choice:
            round -= 1
            print("Try again!")

        else:
            system_points += 1

        print("\n")
        print(f"System choice: {system_choice} vs {user_choice}")
        print(f"User: {user_points} and System: {system_points}")


def main():
    play()

    while input("Do you want to play again?(yes/ no): ").upper() == "YES":
        print("")
        play()


if __name__ == "__main__":
    main()
