from time import time
#print(list(range(1000000)))
def performance(fn):
    def wraper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f"it\'s took {t2-t1} s")
        return result
    return wraper

@performance
def generator_function2(num):
    for i in range(num):
        yield i

# for item in generator_function2(100):
#     print(item)

g = generator_function2(10)
print(help(iter))
print(next(g))


# @performance
# def generator_function(num):
#     result = []
#     for i in range(num):
#         result.append(i)
#     return result


# print(generator_function(100))