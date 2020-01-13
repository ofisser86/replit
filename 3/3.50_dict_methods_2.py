user = {
    'cart': [1, 2, 3],
    'store': 'phone',
    'age': 22
}
user3 = user
user2 = user.copy() # different dict
print(id(user))
print(id(user2))
print(type(user.pop('age')))
print(user)
print(id(user3))