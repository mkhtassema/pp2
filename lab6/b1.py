from functools import reduce
from operator import mul
f =[1,2,3,4]
c = reduce(mul,f)
print(c)
