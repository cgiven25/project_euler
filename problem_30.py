# The problem: https://projecteuler.net/problem=30
# I just used 1,000,000 as the upper bound, and then checked the discussions to see how they bounded it
# 9**5 = 59049.  6*59049 = 354294, so this is the largest 6-digit number than can be represented by a sum of fifth powers

digit_fifth_powers = []
for i in range(2, 354294):
	num_sum = 0
	for digit in str(i):
		num_sum += int(digit)**5
	if num_sum == i:
		digit_fifth_powers.append(i)
print(sum(digit_fifth_powers))