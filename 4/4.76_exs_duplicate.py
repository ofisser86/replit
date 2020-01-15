some_list = ['a', 'b', 'c', 'd', 'b', 'd', 'n', 'n', 'n']
diff = []
for item in some_list:
    if some_list.count(item) >  1:
        if item not in diff:
                diff.append(item)

print(diff)