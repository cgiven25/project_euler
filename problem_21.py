# The problem: https://projecteuler.net/problem=21
# God this took me forever.
# I found a way to find the sum of the factors of a number by just the prime factorization: https://www.math.upenn.edu/~deturck/m170/wk3/lecture/sumdiv.html
# Once I found that, I just had to find all the amicable pairs.  I take the set because everything is added twice.

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

nums = {1: 1}
for i in range(2, 10000):
	factors = prime_factorize(i)
	sum_factors = 1
	for fac in set(factors):
		sum_factors *= (fac**(factors.count(fac) + 1) - 1)//(fac-1)
	nums[i] = sum_factors - i

amicables = []
for num in nums:
	try:
		if nums[nums[num]] == num and (nums[num] != num):
			amicables.append(num)
			amicables.append(nums[num])
	except KeyError:
		continue

print(sum(set(amicables)))