import random

answer = random.randint(1, 10)

def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('You are winner')
            return True
    else:
        print('hey bozo, I say 1~10')
        return False

if __name__ == "__main__":
    while True:
        try:
            guess = int(input('Guess a number 1~10:   '))
            if run_guess(guess, answer):
                break
        except ValueError:
            print('please enter a number')
            continue