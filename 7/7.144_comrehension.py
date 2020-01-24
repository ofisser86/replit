# my_tuple = '{}'.format(item for item in range(10))
# my_tuple2 = (2, 3, 5, 71) 
# print(item for item in range(10))
# print(my_tuple2)
my_dict = {key: key*2 for key in [1, 2, 3]}
print(my_dict)
my_list = ['a', 'v', 'v', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = {item for item in my_list if my_list.count(item) > 1 }
print(list(duplicates))