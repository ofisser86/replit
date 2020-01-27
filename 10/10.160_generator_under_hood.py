def special_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator) 
            print(next(iterator)*5)
        except StopIteration:
            break

#special_for_loop([1,2,3])

# build own generator
class MyGen:
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num

        raise StopIteration

g = MyGen(1, 10)
for i in g:
    print(i)

# try g(1, 2) to get raise
# next(g)
# next(g)
# print(next(g))