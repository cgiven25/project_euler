# The problem: https://projecteuler.net/problem=32
# This problem was mostly just about limiting the bounds.
# Because there can only be 9 digits total, the product must be 4 digits (you can't represent a 5 digit number with less than 6 digits (100 x 100 is the smallest 5 digit number))
# Many 4 digit numbers require 5 digits in the multiplicand/multiplier.  All 3 digit numbers would give you less than 9 digits total.

import math

def get_factors(n):
	factors = [(1, n)]
	for i in range(2, math.floor(n**.5)):
		if n % i == 0:
			factors.append((i, n//i))
	return factors

pandigital = []
for i in range(1000, 9999):
	for factor in get_factors(i):
		if set("".join(map(str, [*factor])) + str(i)) == set("123456789"):
			pandigital.append(i)
			break
print(sum(pandigital))