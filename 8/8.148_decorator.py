def my_dcorator(func):
    def wrap_func():
        print('*******')
        func()
        print('*******')
    return wrap_func

@my_dcorator
def hello():
    print('hellllllo')

hello()
# can use without @my_dcorator
hello2 = my_dcorator(hello)
hello2()
# bad for readability, but still works
my_dcorator(hello)()