# The problem: https://projecteuler.net/problem=45
# This is very slow but works as you'd expect (~27s)

triangular = [n*(n+1)//2 for n in range(286, 100000)]
pentagonal = [n*(3*n-1)//2 for n in range(100000)]
hexagonal = [n*(2*n-1) for n in range(100000)]

for num in triangular:
	if num in pentagonal and num in hexagonal:
		print(num)
		break