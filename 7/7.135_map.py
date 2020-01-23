my_list = [1, 2, 3, 4, 5]
def muliply_by2(item):
    return item * 2

print(list(map(muliply_by2, my_list))) # does not change the list, create new
print(my_list)