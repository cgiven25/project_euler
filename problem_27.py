# The problem: https://projecteuler.net/problem=27
# I just guessed that a and b had to be primes
# And then I brute forced it

def prime_test(n):
	i = 2
	while i*i <= n:
		if (n % i) == 0:
			return False
		i += 1
	return True

primes = [2]
for n in range(3, 1000):
	if prime_test(n):
		primes.append(n)

maxLen = 0
max_a, max_b = 0, 0
for a in primes:
	for b in primes:
		for sign in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
			n = 0
			result = n**2 + a*sign[0]*n + b*sign[1]
			while prime_test(result) and result > 0:
				n += 1
				result = n**2 + a*sign[0]*n + b*sign[1]
			if n > maxLen:
				maxLen = n 
				max_a, max_b = sign[0]*a, sign[1]*b
print(maxLen, max_a, max_b)
