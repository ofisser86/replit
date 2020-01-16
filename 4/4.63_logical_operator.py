print('a' > 'A')
# True beacause
print(ord('a'), ord('A'))
# ============================
print('a' >'b')
# False beacause
print(ord('a'), ord('b'))

a = 'a'
b = 'a'
c = 'A'
print(id(a))
print(id(b))
print(id('a'))
print(id(c))
print(id('A'))