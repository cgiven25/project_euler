# The problem: https://projecteuler.net/problem=4
# Generate all products of three-digit numbers, reverse them and see if they are the same

palindromes = []
for i in range(100, 1000):
	for j in range(100, 1000):
		if str(i*j)[::-1] == str(i*j):
			palindromes.append(i*j)
print(max(palindromes))