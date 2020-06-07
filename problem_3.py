# The problem: https://projecteuler.net/problem=3
# Scavenged my prime_factorize problem from RSA code and used it to output exactly what the question asked.

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

print(prime_factorize(600851475143))