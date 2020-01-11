def your_age():
    age = int(input("What is your age? "))
    if age != 33:
        your_age()
    return age


print(your_age())