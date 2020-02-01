def like_for(iterable):
    iterator = iter(iterable)
    

    
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
             print('Some exception here')
             break

my_list = [3, 1, 2, 6, 8, 7, 8, 9]

print(like_for(my_list))