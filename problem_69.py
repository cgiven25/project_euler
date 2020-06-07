# The problem: https://projecteuler.net/problem=69
# See Euler's product formula: https://en.wikipedia.org/wiki/Euler%27s_totient_function
# Some people did this without code
#  To reduce the number of numbers that are relatively prime to n, we want to use the lowest prime factors possible.
#  So, just keep mutliplying the lowest primes until you get a number greater than 1m, then divide by the most recent multiple

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

def phi(n, factors):
	prod = n
	for factor in set(factors):
		prod *= (1-1/factor)
	return prod

max_val = 0
max_n = 0
# It makes sense that it would occur on an even number 
# (even numbers can have both odd and even factors, but odd numbers can only have odd factors)
for i in range(2, 1000000, 2):
	factors = prime_factorize(i)
	totient = phi(i, factors)
	if i / totient > max_val:
		max_val = i / totient
		max_n = i
print(max_n)