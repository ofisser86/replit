total1 = 0

def my_count():
    global total1
    total1 += 1
    return total1


my_count()
my_count()
print(my_count())

# maybe better way to do this

total2 = 0

def my_count2(total2):
    total2 += 1
    return total2


print(my_count2(my_count2(my_count2(total2))))