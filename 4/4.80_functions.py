def my_sum(num1, num2):
    return num1 + num2

total = my_sum(10, 7)
print(f'sum is {total}')


def bar1(num1, num2):
    def bar2(n1, n2):
        return n1 + n2
    return bar2(num1, num2)


total_for_bar = bar1(10, 4)
print(total_for_bar)

print(print('Hi'))