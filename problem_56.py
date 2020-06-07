# The problem: https://projecteuler.net/problem=56
# This is a LUL PYTHON problem

max_sum = 0
for a in range(1, 101):
	for b in range(1, 101):
		num = a**b
		digital_sum = sum([int(digit) for digit in str(num)])
		if digital_sum > max_sum:
			max_sum = digital_sum
print(max_sum)