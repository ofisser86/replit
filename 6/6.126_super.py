class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Sign in user')
    # will be override later in other subclass
    def attack(self):
        print('do nothing')

class Wiard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        # User.attack(self)
        print(f'Wizard with name {self.name} attack by {self.power} power')




wizard1 = Wiard('Merlin', 77, 'merlin@ukr.net')

wizard1.attack()
print(wizard1.email)
