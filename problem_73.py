# The problem: https://projecteuler.net/problem=73
# I might just be able to brute force this?
# Yeah that was pretty fast.
import math

fracs = 0
for d in range(4, 12001):
	for n in range(d//3 + 1, d//2 + 1):
		if math.gcd(n, d) == 1:
			fracs += 1
print(fracs)