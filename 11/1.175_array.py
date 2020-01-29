from array import array
import sys

ar = array('i', [1, 2, 3])
li = [1, 2, 3]
print(sys.getsizeof(ar))
print(sys.getsizeof(li)) 