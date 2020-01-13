amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

amazon_cart[0] = 'laptop'
new_cart = amazon_cart # copy with [:] or amazon_cart.copy()
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)
print(id(amazon_cart))
print(id(new_cart))