# first solution
# def highest_even(li):
#     tmp = sorted(li)
#     if tmp[len(tmp) - 1] % 2 == 0:
#         return tmp[-1]
#     else:
#         return tmp[-2]
#=====================================
# second solution
# def highest_even(li):
#     tmp = [item for item in li if item % 2 == 0 ]
#     return max(tmp)
#============================= 
#    return max([item for item in li if item % 2 == 0 ])
#
#===================================
# Third solution 
# def highest_even(li):
#     tmp = 0
#     for i in li:
#         if i % 2 == 0 and i > tmp:
#             tmp = i
#     return tmp
#=====================================
# forth solution
# def highest_even(li):
#   evens = []
#   for item in li:
#     if item % 2 == 0:
#       evens.append(item)
#   return max(evens)

def highest_even(li):
  evens = []
  for item in li:
    if item % 2 == 0:
      evens.append(item)

  evens.sort(reverse=True)
  return evens[0]
  #return sorted(evens,reverse=True)[0]


print(highest_even([10,1,2,3,4,8]))


# list_of_num = [10, 2, 3, 4, 11]
# print(highest_even(list_of_num))