while True:
    try:
        age = int(input("What is your age? "))
        10/age
        print(f"your age is {age}")
    except ValueError:
        print("Please enter only digts")
        continue
    except ZeroDivisionError:
        print("Do not write Zero age")
        break
    else:
        print('Thank you')
        #break
    finally:
        print('heloooo I am here')
    # Do not run untilof break statement works18

    print("Do not run because of breck statement")