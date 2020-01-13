basket = [1, 2, 3, 4, 5, 'hello']
new_basket = basket.copy() # create a new list

# adding
second_basket = basket.insert(0, 100) # do not copy, only modify existing list!!!
# basket.insert(0, 100)
# second_basket = basket[:]
# print(basket)
# print(second_basket)

print(id(basket))
print(id(new_basket))
print("this is second basket ->", second_basket)
print(id(second_basket))
print(new_basket) 

print('hello' in basket)
print('h' in basket)
# add 100 in index o
print('h' in basket[6][0])