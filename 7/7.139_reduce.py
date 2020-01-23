my_list = [item for item in range(10) ]

from functools import reduce
def accumulator(acc, item):
    return acc + item



print('Reduce -->', reduce(accumulator, my_list, 0))  # like count the sum of list items - in this case

print(my_list)