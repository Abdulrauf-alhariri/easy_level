

def leap_year():
    divisible_4 = 4
    divisible_400 = 400
    divisible = False
    year = int(input("Check if it is a leap year: "))

    if year % divisible_4 == 0 or year % divisible_400 == 0:
        return True

    else:
        return False


def fibonacci():
    nterms = int(input("How many terms: "))
    nr1, nr2 = 0, 1
    count = 0

    if nterms <= 0:
        print("Please enter a positiv number!")

    elif nterms == 1:
        print(nr1)

    else:
        print("Fibonacci sequense:")
        while count <= nterms:
            print(nr1)
            nth = nr1 + nr2
            nr1 = nr2
            nr2 = nth
            count += 1


if __name__ == "__main__":
    print(leap_year())
