# The problem: https://projecteuler.net/problem=53
# Python brute force gang

from math import factorial

greater = 0
for n in range(23, 101):
	for r in range(n):
		if (factorial(n)/(factorial(r)*factorial(n-r))) > 1000000:
			greater += 1
print(greater)