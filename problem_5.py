# The problem: https://projecteuler.net/problem=5
# This is basically finding the lcm 20 times in a row.
# lcm(a, b) = a*b/gcd(a, b)
# The problem asks for a number that is evenly divisible by 1-20, so it must be a multiple of each of these
# At each iteration, we guarantee that n is a multiple of i, and it's the least common multiple

import math

n = 1
for i in range(1, 21):
	n = int(n*i/math.gcd(n, i))
print(n)