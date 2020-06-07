# The problem: https://projecteuler.net/problem=10
# Not pretty, but still only takes 12 seconds.  
# Using a sieve-type thing before checking each number that falls through the sieve could make this faster, probably

def prime_test(n):
	i = 2
	while i*i <= n:
		if (n % i) == 0:
			return False
		i += 1
	return True

i = 3
p_sum = 2
while i < 2000000:
	if prime_test(i):
		p_sum += i
	i += 2
print(p_sum)