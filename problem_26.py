# The problem: https://projecteuler.net/problem=26
# I looked up repeating decimal sequences and learned about full reptend primes:
# https://mathworld.wolfram.com/FullReptendPrime.html

def full_reptend_test(n):
	if prime_test(n):
		if 10**(n-1) % n == 1:
			for i in range(1, n-1):
				if 10**(i) % n == 1:
					return False
			return True
	return False

def prime_test(n):
	i = 2
	while i*i <= n:
		if (n % i) == 0:
			return False
		i += 1
	return True

maxNum = 7
for i in range(11, 1000):
	if full_reptend_test(i):
		maxNum = i
print(maxNum)