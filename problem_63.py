# The problem: https://projecteuler.net/problem=63
# This is a very simple problem, I just need to find an upper bound
# Number of digits of an integer n is ceil(log n)
# I'm just gonna do some testing to identify where I can stop, if it all.
# Using the test results, 21 is the largest exponent which can have this property.
# I am assuming that all larger exponents will fail (but tbh I don't really know why)

def test():
	k = 1
	while True:
		i = 1
		while len(str(i**k)) != k:
			i += 1
			# If we get a length greater than the exponent, but never equal, we hit the bound
			if len(str(i**k)) > k:
				return i, k
		k += 1

nums = 0
for n in range(1, 22):
	j = 0
	while len(str(j**n)) <= n:
		j += 1
		if len(str(j**n)) == n:
			nums += 1
print(nums)