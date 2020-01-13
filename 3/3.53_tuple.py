my_tuple = (1, 2, 3, 3, 4, 5)
x, y, z, *other = (7, 8, 9, 10, 11)
print(my_tuple)
print(x)
print(z)
print(other) # !!!! other is a list

print(3 in my_tuple)

print(my_tuple.count(3)) # count of elementsn, not all elem in tuple
print(my_tuple.index(3)) # return index of given element

print(len(my_tuple))    # length of tuple