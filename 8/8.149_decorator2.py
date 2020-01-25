def my_dcorator(func):
    def wrap_func(*arg, **kwargs):
        print('*******')
        func(*arg, **kwargs)
        print('*******')
        
    return wrap_func

@my_dcorator
def hello(greating, emoji):
    print(greating, emoji)

hello('kjkj', ':-)')
