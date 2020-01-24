def my_dcorator(func):
    def wrap_func(*arg, **kwargs):
        print('*******')
        res = func(*arg, **kwargs)
        print('*******')
        return res
    return wrap_func

@my_dcorator
def hello(greating, emoji):
    print(greating, emoji)

hello('kjkj', ':-)')
