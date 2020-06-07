# The problem: https://projecteuler.net/problem=47
# Should be simple because I have a prime factorize function somewhere

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

consecutive = 0
num = 647
while consecutive < 4:
	if len(set(prime_factorize(num))) == 4:
		consecutive += 1
	else:
		consecutive = 0
	if consecutive == 4:
		print(num - 3)
		break
	num += 1		