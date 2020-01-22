class User():
    def sign_in(self):
        print('Sign in user')
    # will be override later in other subclass
    def attack(self):
        print('do nothing')

class Wiard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'Wizard with name {self.name} attack by {self.power} power')

class Archer(User):
    def  __init__(self, name, arrow):
        self.name = name
        self.arrow = arrow

    def attack(self):
        print(f'Archer {self.name} attack with {self.arrow} arrows')


wizard1 = Wiard('Merlin', 77)
archer1 = Archer('Queen Archer', 159)

print(wizard1.attack())