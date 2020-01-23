my_list = [item for item in range(15) ]
def muliply_by2(item):
    return item * 2

def only_odd(item):
    return item % 2 - 1


print(list(map(muliply_by2, my_list))) # does not change the list, create new
print(list(filter(only_odd, my_list)))
print(my_list)