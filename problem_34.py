# The problem: https://projecteuler.net/problem=34
# Apparently the brute force solution is not that bad
# Upper bound found by the same method as the fifth-powers problem

import math

totSum = 0
for i in range(10, 2540160):
	num_str = str(i)
	num_sum = 0
	for digit in num_str:
		num_sum += math.factorial(int(digit))
	if num_sum == i:
		totSum += i
print(totSum)