# array = [1,2,3,4,5]
# array_1 = []
# for i in array:
#     array_1.append(i**2)
#
# print(array_1)
#
# ar = [i**2 for i in range(1,40) if i%2 ==2]
# print(ar)
#
# ao = [x*2 if x % 2 == 0 else x+1 for x in range (2,40)]
# print(ao)

# w = [x+y for x in range (1,6) for y in range (2,8)]
# print(w)

import random
print(random.randint(0,23))

r = [random.randint(10,45) for i in range (15)]
print(r)
print(len(r))

print(random.random())