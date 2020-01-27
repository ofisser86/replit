from time import time
def performance(fn):
    def wraper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f"it\'s took {t2-t1} s")
        return result
    return wraper

@performance
def long_time1():
    print('1')
    for i in range(100000000):
        i*5

@performance
def long_time2():
    print('2')
    for i in list(range(100000000)):
        i *5

long_time1()
long_time2()