# The problem: https://projecteuler.net/problem=51
# Assume it falls within the first 25,000 primes

def prime_test(n):
	i = 2
	while i*i <= n:
		if (n % i) == 0:
			return False
		i += 1
	return True

primes = [11]
i = 11
while len(primes) < 25000:
	if prime_test(i):
		primes.append(i)
	i += 2

# Test a prime by selecting n asterisks, where n <= number of digits - 1
# Select digits to replace by these asterisks.
# Replace the digits with 0-9, seeing how many are prime.
# If there are not exactly 8 that are prime, select new positions.
# This solution: for each prime, there are 2**n - 2 positions for the asterisks
# 	for each position, we have to check 10 numbers for primality.
# (2**n - 2)*10*25,000.  Suppose an average length of 5, that gives us 75,000,000 prime tests.
# This would take forever.
# Come up with a different solution at some point 
for prime in primes:
	