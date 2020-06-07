# The problem: https://projecteuler.net/problem=13
# Large numbers are really easy for python.  I can just compute the sum and print the first 10 digits.
# This would normally work by just adding the first 10 digits of each number and discarding carries past the 10th digit.

totSum = 0
with open("problem_13.txt") as nums_file:
	nums = nums_file.read().split("\n")
	for num in nums:
		totSum += int(num)
print(str(totSum)[:10])