def my_sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'something went wrong errors is {err}')

my_sum(1, '2')


def my_sum2(num1, num2):
    try:
        return num1/num2
    except (TypeError, ZeroDivisionError) as err:
        print(f'something went wrong errors is {err}')

my_sum(1, '2')
my_sum2(1, 0)