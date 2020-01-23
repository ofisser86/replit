from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
def capitalise_my_list(li):
    return li.capitalize()
print(list(map(capitalise_my_list, my_pets)))
print([item.capitalize() for item in my_pets])

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
print(list(zip(my_strings, my_numbers[::-1])))
# Second solution 
# my_numbers.reverse()
# print(list(zip(my_strings, my_numbers)))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
def over_50(item):
    return item > 50

print(list(filter(over_50, scores)))
#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
#
#For better readability use for loop insteed of reduce
#
def accum(acc, item):
    return acc + item


#print(reduce(accum, my_numbers, 0) + reduce(accum, scores, 0))
print(reduce(accum, my_numbers + scores, 0)) 