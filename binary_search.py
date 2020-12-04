import random

pos = -1


def search(list, n):
    l = 0
    u = len(list) - 1

    while l < u:
        mid = (l + u) // 2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid
            else:
                u = mid


user_search = int(input("Enter the number you want to search \n>>>"))
my_list = list(range(1, 100, 2))

list1 = list(range(2, 110, 2))
if search(list1, user_search):
    print("Found at", pos)
else:
    print("It's not found")
