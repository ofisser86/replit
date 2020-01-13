my_set = {1, 2, 3, 3, 4, 5, 11, 5, 3, 7, 7,3, }
print(my_set) # all unique items
# print(my_set[0]) # it is error 
print(7 in my_set)

new_set = my_set.copy() # different sets
print(new_set)
print(id(my_set))
print(id(new_set))