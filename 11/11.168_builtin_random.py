from random import random, shuffle, randint, choice, choices

print(random())
print(randint(1, 100))
print(choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
my_list = [5, 9, 7, 3, 6, 4, 5, 7, 8, 9, 1, 2, 3]
shuffle(my_list)
print(my_list)