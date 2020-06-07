# The problem: https://projecteuler.net/problem=38
# There are 9! 1 to 9 pandigital numbers.
# Testing all of them for this property would be difficult. 
# However, we can cut off all numbers less than 918273645, since that was given in the example.
# There are still a bit more than 7! (5040) left, but that reduced our search space by a lot.
# The crux of this problem was figuring out that the integer to test had to be 4 digits long.

from itertools import permutations

pandigitals = ["9" + "".join(p) for p in permutations("12345678") if int("9" + "".join(p)) > 918273645]
largest = 0
for num in pandigitals:
	test_num = int(num[:4])
	num_remaining = num.lstrip(str(test_num))
	if test_num * 2 == int(num_remaining):
		largest = num
print(pandigitals)
# print(largest)
