# Test your assumtions

class PlayerCharacter():
    membership = True

    def __init__(self, name, age):
        if age > 18:
            self.name = name
            self.age = age

    def test_my_assumtions(self):
        return self

    # need self
    # def test_my_assumtions2(num1, num2):
    #     return self.age + num1 + num2


#player1 = PlayerCharacter('Nata', 22)
player1 = PlayerCharacter('Avrora', 99) # error beacuse init does not work

# has the same id in memory. self is refer to the object
print(player1)
#print(player1.test_my_assumtions2(5,33))
