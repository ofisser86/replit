user = {
    'cart': [1, 2, 3],
    'store': 'phone',
    'age': 22
}
# try get name, if None get Didi as default
print(user.get('name', 'Didi')) 

# another way to create dict
user2 = dict(name='John', age=33, surname='Doy')
print(user2)