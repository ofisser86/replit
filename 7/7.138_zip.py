my_list = [item for item in range(4, 15) ]
your_list = [20, 30, 50]
their_list = [ 1, 2, 3]
def muliply_by2(item):
    return item * 2

def only_odd(item):
    return item % 2 - 1


print('Map list -->', list(map(muliply_by2, my_list)))  # does not change the list, create new
print('Filter list -->', list(filter(only_odd, my_list))) # filter
print('Zip list -->', list(zip(my_list, your_list, their_list))) # zip 
print(my_list)