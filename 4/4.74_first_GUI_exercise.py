picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
# TODO: have to change variable i and j to row and pixel for better understanding
# fill = '*'
# empty = ''
# for row in picture:
#     for pixel in row:
#         if pixel:
#             print(fill, end='')
#         else:
#             print(empty, end='')
#     print()



for i in picture:
    for j in i:
        if j == 0:
            print(' ', end='')
        elif j == 1:
            print('*', end='')
    print()