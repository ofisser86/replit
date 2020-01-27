def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        tmp = a 
        a = b
        b = tmp + b  

for i in fib(21):
    print(i)

# using list
def fib2(number):
    result = []
    a = 0
    b = 1
    for i in range(number):
        result.append(a)
        tmp = a 
        a = b
        b = tmp + b 
    return result 

for i in fib(21):
    print(i)

print(fib2(21))

