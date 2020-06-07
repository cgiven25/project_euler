# The problem: https://projecteuler.net/problem=20
# Python is just great at handling large numbers. 
# It finished this in 0.03s

import math
print(sum(list(map(int, str(math.factorial(100))))))