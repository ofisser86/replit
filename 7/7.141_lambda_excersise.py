my_list = [2, 3, 5]
print(list(map(lambda item: item*item, my_list)))
print([item * item for item in my_list])

# List sorting with lambda
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
# My solution 
print(list(map(lambda item: sorted(item, reverse=True), a)))
print([sorted(item, reverse=True) for item in a])
# True solution
a.sort(key=lambda item: item[1])
print(a)