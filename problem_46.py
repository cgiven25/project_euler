# The problem: https://projecteuler.net/problem=46
# Pretty naive solution, would be slow if the first counterexample was large

def prime_test(n):
	i = 2
	while i*i <= n:
		if (n % i) == 0:
			return False
		i += 1
	return True

num = 35
found = False
while not found:
	if prime_test(num):
		num += 2
		continue
	j = 1
	fail = True
	while 2*(j**2) < num:
		diff = num - 2*(j**2)
		# If the difference is prime, break
		if prime_test(diff):
			fail = False
			break
		j += 1
	if fail:
		print(num)
		break
	num += 2
	