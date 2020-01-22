class User():
    def sign_in(self):
        print('Sign in user')

class Wiard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Wizard with name {self.name} attack by {self.power} power')

class Archer(User):
    def  __init__(self, name, arrow):
        self.name = name
        self.arrow = arrow

    def how_namy_arrows(self):
        print(f'Archer {self.name} attack with {self.arrow} arrows')
    
    def run_fast(self):
        print('run fast with power')


class Hybrioid(Wiard, Archer):
    def __init__(self, name, power, arrow):
        Archer.__init__(self, name, arrow)
        Wiard.__init__(self, name, power)

hb1 = Hybrioid('humanoid', -5, 10)
print(hb1.run_fast())
print(hb1.attack())
print(hb1.how_namy_arrows())
print(hb1.sign_in())