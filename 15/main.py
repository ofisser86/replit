def do_staff(num=0):
    try:
        if num or num == 0:
            return int(num) + 5
        else:
            return 'plese enter a number'
    except ValueError as err:
        return err