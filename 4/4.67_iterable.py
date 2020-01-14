user = {
    'name': 'Didi',
    'age': 33,
    'can_run': True
}

for item in user:
    print(item)

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

# like unpacking the tuple
for key, value in user.items():
    print(key, value) 