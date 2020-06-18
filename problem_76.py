# The problem: https://projecteuler.net/problem=76
# I stole this and it really doesn't make sense to me.
# It is wrong for numbers less than 100.

ways = {0: 1}

for i in range(1, 100):
	for j in range(i, 101):
		try:
			ways[j] += ways[j - i]
		except KeyError:
			ways[j] = ways[j - i]
	try:
		print(ways[5])
	except KeyError:
		print(1)
print(ways[100])