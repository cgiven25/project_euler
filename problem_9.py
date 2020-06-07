# The problem: https://projecteuler.net/problem=9
# Looking back, I actually wasted time using algebra on this problem
# Not manipulating anything, you could still just calculate c^2, and then c by taking the square root.
# And then, just see if a + b + c = 1000.  Whoops.

import math

for a in range(1000):
	for b in range(1000):
		if (2000*a + 2000*b - 2*a*b) == 1000000:
			print(a*b*(math.sqrt(a**2 + b**2)))