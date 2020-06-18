# The problem: https://projecteuler.net/problem=51
# Assume it falls within the first 25,000 primes
# I will use regex to do this
import re

def prime_test(n):
	i = 2
	while i*i <= n:
		if (n % i) == 0:
			return False
		i += 1
	return True

primes = ["2"]
i = 3
while len(primes) < 25000:
	if prime_test(i):
		primes.append(str(i))
	i += 2

# regex = re.compile("^56(?:.*.){2}3$")
regex = re.compile("^563$")
for prime in primes:
	if regex.match(prime):
		print(prime)