class PlayerCharacter():
    membership = True

    def __init__(self, name, age):
        if PlayerCharacter.membership:
            self.status = 'Expert'
        self.name = name
        self.age = age

    
    def run(self):
        print('done')
    
    def shout(self):
        print(f'my name is {self.name}') # can not use PlayerCharacter.name, only self.name


player1 = PlayerCharacter('Nata', 22)
player2 = PlayerCharacter('Did', 33)

player2.attack = 55

#print(player1.attack)
#print(player2.attack)


print(player1.shout())