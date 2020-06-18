# The problem: https://projecteuler.net/problem=99
# An easy way would be if the largest number is just the largest exponent
# That's wrong, fair enough
# Idea -- look at the number of digits of the base, multiple by number of digits of exp
# 	Largest result is the biggest
#   Also wrong
# Ok I'm gonna do some analysis
# 	Smallest base: 334
#   Largest base: 999665
# 	Smallest exponent: 500894
#	Largest exponent: 1190800
# It is noteworthy that 334 and 1190800 occur on the same line.
# Ok fine I will use log rules
# Num digits is floor(log n) + 1
# n = a^b, so log(a^b) = b log(a)
# So, # digits = floor(b log(a)) + 1
# I didn't get the right answer the first time, but there was another number with the same number of digits
# So, I just tried the other one and it worked.
import math

nums = []
with open("problem_99.txt") as prob_99_file:
	lines = prob_99_file.read().split("\n")
	for line in lines:
		line = line.split(",")
		nums.append((int(line[0]), int(line[1])))

max_digits = 0
max_i = 0
i = 1
for num in nums:
	num_digits = math.floor(num[1] * math.log(num[0], 10)) + 1
	if num_digits > max_digits:
		max_digits = num_digits
		max_i = i
	elif num_digits == max_digits:
		print(i, num_digits, "here")
	i += 1
print(max_digits, max_i)