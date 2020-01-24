from time import time

def performance(fc):
    def wrap_fn(*arg, **kwargs):
        t1 = time()
        result = fc(*arg, **kwargs)
        t2 = time()
        print(f'func took { t2 - t1} s')
        return result

    return wrap_fn

@performance
def hello():
    for i in range(100000000):
        i*5
# Practice - difference between creating a list
@performance
def my_list():
    li = []
    for item in range(10000000):
        li.append(item)
    return li

@performance
def list_comp():
    li = [item for item in range(10000000)]
    return li

# @performance
# def list_on_fly():
#     li = list('1234567890')
#     return li

my_list()
list_comp()
# list_on_fly()
# print(list_on_fly())