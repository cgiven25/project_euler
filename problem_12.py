# The problem: https://projecteuler.net/problem=12
# Given a prime factorization of primes p1^k1, p2^k2, etc...
# 	The number of factors is (k1+1)(k2+1)...(kn+1)
#   This comes from the idea that when you are choosing to multiply factors, you have a certain number of choices.
#   Suppose 2^3 is a factor.  You could include a single 2, two 2's, or three 2's.  You could also include zero 2's, making 4 choices.

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

num_divisors = 1
prev_num = 28
i = 8
while num_divisors <= 500:
	num_divisors = 1
	num = prev_num + i
	factors = prime_factorize(num)
	for f in set(factors):
		num_divisors *= (factors.count(f) + 1)  
	i += 1
	prev_num = num
print(prev_num)