#example clean code for function

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     elif num % 2 != 0:
#         return False

def is_even(num):
    return num % 2 == 0


print(is_even(10))

my_list = ["apple", "banana", "cherry", 'kiwi', 'pear', 'melon']
my_tuple = ("apple", "banana", "cherry", 'kiwi', 'pear', 'melon')
print(my_list[2:5])
print(my_tuple[2:5])