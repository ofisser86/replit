while True:
    try:
        age = int(input("What is your age? "))
        10/age
        print(f"your age is {age}")
    except ValueError:
        print("Please enter only digts")
    except ZeroDivisionError:
        print("Do not write Zero age")
    else:
        break