class PlayerCharacter():
    membership = True

    def __init__(self, name='anonim', age=0):
        if age > 18:
            self.name = name
            self.age = age

    @classmethod
    def add_some_things1(cls, num1, num2):
        return num1 + num2
    
    @classmethod
    def add_some_things2(cls, num1, num2):
        return cls('Teddy', num1 + num2)    # create object


    # Cannot use cls
    @staticmethod
    def my_static_method(num3, num4):
        return num3 + num4

print(PlayerCharacter.add_some_things1(5, 2))
print(PlayerCharacter.add_some_things2(5, 2))
print(PlayerCharacter.my_static_method(9, 11))
