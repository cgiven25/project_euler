# The problem: https://projecteuler.net/problem=41
# I started by taking all the pandigitals from problem 38, and quickly realized there are no 9-digit pandigitals that start with 9.
# Actually, there are no 9-digit pandigitals at all.  Or 8-digit.
from itertools import permutations

def prime_test(n):
	i = 2
	while i*i <= n:
		if (n % i) == 0:
			return False
		i += 1
	return True

pandigitals = ["".join(p) for p in permutations("1234567")]
largest = pandigitals[0]
for num in pandigitals:
	if prime_test(int(num)):
		largest = num
print(largest)