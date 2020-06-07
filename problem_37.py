# The problem: https://projecteuler.net/problem=37
# I learned more about truncatable primes: https://oeis.org/A020994
# This also told me the answer but I now know a way to find them.
# It makes sense that each digit string containing the first or last digit must be prime.

def prime_test(n):
	if n == 1:
		return False
	i = 2
	while i*i <= n:
		if (n % i) == 0:
			return False
		i += 1
	return True

truncatable = []
i = 23
while len(truncatable) != 11:
	if prime_test(i):
		for n in range(1, len(str(i))):
			# see if the digit string of length n is prime
			if not(prime_test(int(str(i)[:n])) and prime_test(int(str(i)[-n:]))):
				break
			if n == len(str(i)) - 1:
				truncatable.append(i)
	i += 2
print(sum(truncatable))