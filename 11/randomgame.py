from random import randint
import sys


args = sys.argv
win_number = randint(int(args[1]), int(args[2]))
attempts = int(args[3])


for i in range(attempts):
    try:
        number = int(input(f"You have {attempts} attempts. Enter number between {args[1]} and {args[2]}: "))
        if int(args[1]) > number > int(args[2]):
            if number == win_number:
                print("Congrats, You guess the number")
                break
            elif i == int(args[3]) - 1 :
                print(f"Win number was --> {win_number}. Try again later")
                break
        else:
            print(f"Enter a number only between {args[1]} and {args[2]}")
            continue
        print(i)
        print(f'Keep trying..... Left {attempts - 1} trys')
        attempts -= 1
    except ValueError:
        print(f"Enter a number between {args[1]} and {args[2]}")
        continue