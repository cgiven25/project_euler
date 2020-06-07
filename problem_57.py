# The problem: https://projecteuler.net/problem=57
# This is a precision problem
from fractions import Fraction
from sys import setrecursionlimit

# idk how this works really but this fixed an error
setrecursionlimit(100000)

bigger_numerator = 0

def get_iteration(i, n=0):
	if i == 0:
		return 1 + n
	return get_iteration(i - 1, Fraction(1, (2+n)))

for i in range(1, 1001):
	frac = get_iteration(i)
	if len(str(frac.numerator)) > len(str(frac.denominator)):
		bigger_numerator += 1
	print(bigger_numerator)

print(bigger_numerator)