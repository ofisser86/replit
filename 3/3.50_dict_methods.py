user = {
    'cart': [1, 2, 3],
    'store': 'phone',
    'age': 22
}
# try get name, if None get Didi as default, don`t modify the dict
print(user.get('name', 'Didi')) 
print(user)
# another way to create dict
user2 = dict(name='John', age=33, surname='Doy')
print(user2)