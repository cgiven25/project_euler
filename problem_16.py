# The problem: https://projecteuler.net/problem=16
# Again, python is great with large numbers so this isn't hard to compute in Python.
# I'm not really sure how you would normally do this, unless there's some kind of pattern to the digits in powers of 2.
# One's digits have a repeating pattern of 2, 4, 8, 6. 
# Ten's digits have some kind of pattern but it's hard to trace

totSum = 0
for char in str(2**1000):
	totSum += int(char)
print(totSum)