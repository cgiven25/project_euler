# The problem: https://projecteuler.net/problem=2
# Solution is pretty self-explanatory: Generate the fibonacci sequence until a value exceeds 4,000,000 and add all even terms.
i = 1
j = 2
fib_sum = 0
while j < 4000000:
	fib_sum += j if j % 2 == 0 else 0
	j = i + j
	i = j - i
print(fib_sum)