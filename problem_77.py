# The problem: https://projecteuler.net/problem=77
# Idea: Similar to 76, but we can only go to the previous primes
# 1 is not prime, according to this problem (I agree)
# For a number n:
#	Go to the primes less than n - 1, and sum the ways those can be made
# 	This won't work, I don't currently have another idea

def prime_test(n):
	i = 2
	while i*i <= n:
		if (n % i) == 0:
			return False
		i += 1
	return True

# Get next prime number
primes = (i for i in range(5, 100000) if prime_test(i))

prime_ways = {2: 0, 3: 1}

ways = 0
n = 4
while ways <= 5000:
	ways = 0
	if max(prime_ways) < n:
		prime_ways[next(primes)] = 0
	for num in [prime for prime in prime_ways if prime < n - 1]:
		# print(num)
		ways += prime_ways[num]
	if n in prime_ways:
		prime_ways[n] = ways
	# print(prime_ways)
	n += 1
	print(prime_ways)