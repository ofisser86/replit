name = input('What is your name? --> ')
password = input("Enter your password here --> ")
pass_len = len(password) * '*'
print(f"{name}, your password {pass_len} is {len(password)} symbols long ")