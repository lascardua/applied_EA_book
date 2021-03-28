# https://www.geeksforgeeks.org/python-all-possible-n-combination-tuples/?ref=rp
# Python3 code to demonstrate working of
# All possible N combination tuples
# Using list comprehesion + product()
from itertools import product

A = [1,2,3]

# initialize N
N = 3

# # All possible N combination tuples of A
# # Using list comprehesion + product()
# res = [ele for ele in product(A, repeat = N)]
#
# # printing result
# for i in res:
#     print(i)

# minha abordagem
import numpy as np
lilica = np.zeros((N**2,2))
res = product(A, repeat = 2)

id_ele = 0
for elem in res:
    lilica[id_ele] = elem
    id_ele = id_ele + 1

print(lilica)


print('combinations ------------------------------------')
from itertools import combinations
res = combinations(A,2)
for elem in res:
    print(elem)

print('combinations_with_replacement --------------------')
from itertools import combinations_with_replacement as cr
res = cr(A,2)
for elem in res:
    print(elem)

print('permutations ------------------------------------')
from itertools import permutations as pm
res = pm(A,2)
for elem in res:
    print(elem)