# The problem: https://projecteuler.net/problem=23
# This one was tricky, and my solution is slow and probably sloppy.
# It's a brute force algorithm.  First, it calculates all abundant numbers 28110 or below.
# Then, for each number 1 <= n < 28123, I go through each abundant number and see if that i - that number is in abundant.
# If it is, then the number can be written as a sum of two abundant numbers.

def sum_factors(n):
	factors = prime_factorize(n)
	sum_factors = 1
	if len(factors) != 1:
		for fac in set(factors):
			sum_factors *= (fac**(factors.count(fac) + 1) - 1)//(fac-1)
		return sum_factors - n
	return sum_factors

def prime_factorize(n):
	factors = []
	i = 2
	# If i > sqrt(n), "i" can't be a factor we haven't already hit
	while i*i <= n:
		# If "i" is not a factor, increment it and try again
		# Otherwise, add it to the list of factors and divide n by i
		if n % i:
			i += 1
		else:
			n //= i
			factors.append(i)
	# If the remaning factor is not 1, then add it to the list of factors
	if n > 1:
		factors.append(n)
	return factors

abundant = [12]
# start at 13 because we know 12 is abundant, 
for i in range(13, 28123 - 12):
	if sum_factors(i) > i:
		abundant.append(i)

totSum = 0
for i in range(1, 28123, 1):
	if i % 2 == 0 and i > 46:
		continue
	summable = False
	for num in abundant:
		if num >= i:
			break
		if (i - num) in abundant: 
			summable = True
			break
	if not summable:
		totSum += i
print(totSum)
