from collections import defaultdict, OrderedDict, Counter

# ================Counter==============
li = [1, 2, 3, 5, 5, 4, 7, 8, 8, 8, 8,9, 1 ]
# get How many value in the list, return dict {'value': count}, ordered by count
print(Counter(li))


# ================defaultdict
d1 = defaultdict(int, {'a': 1, 'b':2, 'd': 5})
#create a default variable 0 based int
print(d1['c'])
d2 = defaultdict(lambda: 5, {'a': 1, 'b':2, 'd': 5})
#create a default variable 0 based on lambda (simply return 5)
print(d2['c'])
d3 = defaultdict(lambda: 'does not exist', {'a': 1, 'b':2, 'd': 5})
#create a default variable 0 based on lambda (simply return somestring)
print(d3['c'])

#================OrderDict

ordered_dict1 = OrderedDict()
ordered_dict1['a'] = 1
ordered_dict1['b'] = 2

ordered_dict2 = OrderedDict()
ordered_dict2['a'] = 1
ordered_dict2['b'] = 2

ordered_dict3 = OrderedDict()
ordered_dict3['b'] = 2
ordered_dict3['a'] = 1
# True
print(ordered_dict1 == ordered_dict2)
# False
print(ordered_dict1 == ordered_dict3)

