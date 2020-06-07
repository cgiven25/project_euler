# The problem: https://projecteuler.net/problem=49
# This problem is rough.
# Idea: Generate all 4-digit primes.  I will start there to see how long my solution will take.
# 	There are 1061. Not that bad.
# Now, start with a prime.  Subtract 10,000 by that prime.  Divide the result by 2.
# 	That is the upper limit for the sequence incrementation.
# Try all possible incrementations.  The increment must be even, since the prime will be odd.
# 	If the next number is not prime, go to the next incrementation
#   If it is, try the next one.
#   If the next number is also prime, then we found the sequence

def prime_test(n):
	i = 2
	while i*i <= n:
		if (n % i) == 0:
			return False
		i += 1
	return True

primes = []
for i in range(1000, 10000):
	if prime_test(i) and i not in [1487, 4817, 8147]:
		primes.append(i)

for prime in primes:
	for j in range(2, (10000-prime)//2, 2):
		current_seq = [prime]
		if set(str(prime + j)) == set(str(prime)) and prime_test(prime + j):
			current_seq.append(prime + j)
		else:
			continue
		if set(str(prime + 2*j)) == set(str(prime)) and prime_test(prime + 2*j):
			current_seq.append(prime + 2*j)
			print("{}{}{}".format(*current_seq))
			break
		else:
			continue