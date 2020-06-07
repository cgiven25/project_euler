# The problem: https://projecteuler.net/problem=52
# Assumption: If the numbers have different length, it is invalid
# The answer is actually a permutation of the number provided.
# The answer is the repeating sequence of 1/7 (142857).

x = 0
while True:
	x += 1
	nums = [str(x), str(2*x), str(3*x), str(4*x), str(5*x), str(6*x)]
	if len(nums[0]) != len(nums[-1]):
		continue
	if set(nums[0]) == set(nums[1]) == set(nums[2]) == set(nums[3]) == set(nums[4]) == set(nums[5]):
		print(x)
		break
