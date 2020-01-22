class PlayerCharacter():
    membership = True

    def __init__(self, name='anonim', age=0):
        if age > 18:
            self.name = name
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')


#player1 = PlayerCharacter('Nata', 22)
player1 = PlayerCharacter() # error beacuse init does not work

print(player1.shout())