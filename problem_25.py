# The problem: https://projecteuler.net/problem=25
# This one is pretty easy -- just generate the Fibonacci sequence until one of them has more than 1000 digits.

i = 1
j = 2
index = 3
while len(str(j)) < 1000:
	j = j + i
	i = j - i 
	index += 1

print(index)