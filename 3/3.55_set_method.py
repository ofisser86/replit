my_set = {1, 2, 3, 4, 5,}
your_set = {4, 5, 6, 7, 8, 9, 10}

print(my_set.difference(your_set)) # only told difference
print(my_set)
print(your_set.difference(my_set))

# print(my_set.discard(5)) modify set, by discard 5
# print(my_set)

# print(my_set.difference_update(your_set)) # remove difference
# print(my_set)

print(my_set.intersection(your_set)) # intersection of set
print(my_set & your_set) # the same as above

print(my_set.isdisjoint(your_set)) # чи є щось спільне, спробуй my_set = {4, 5}
print()

print(my_set.issubset(your_set)) # if ALL elements try my_set = {4, 5}
print(my_set.issuperset(your_set)) 
print(your_set.issuperset(my_set))

print()
print(my_set.union(your_set)) # return new set from two nd remove duplicates
print(my_set | your_set) # the same as above
