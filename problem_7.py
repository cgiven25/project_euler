# The problem: https://projecteuler.net/problem=7
# 10,001 primes are not that hard to generate in any programming language.
# The only thing worth explaining is the bounds on the prime_test loop.
# If a factor is identified early, it has a larger pair.  The only way a factor doesn't have a pair is if n is a perfect square.
# By only checking up to sqrt(n), we can save time because if n does not have a factor in this lower section, then it has no pair either.

def prime_test(n):
	i = 2
	while i*i <= n:
		if (n % i) == 0:
			return False
		i += 1
	return True

i = 3
p = 1
while p < 10001:
	if prime_test(i):
		p += 1
	i += 2
print(i - 2)