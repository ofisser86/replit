#OOP
print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('hi'))
print(type([]))
print(type(()))
print(type({}))
class MyClass():
    surname = ''
    def __init__(self, name):
        self.name = name
    
    def my_age(self, age):
        my_age = age + 10
        return my_age



man = MyClass("Didi")
age = man.my_age(23)

print(man.name, age)


