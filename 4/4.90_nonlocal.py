# Scope - what variables do I have access to?
# nonlocal is refer to Parent scope
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)
outer()

#1 - start with local
#2 - Parent local?
#3 - global
#4 - built in python functions

#Avoid to use global and nonlocal
my-var = 5
print(my-var)