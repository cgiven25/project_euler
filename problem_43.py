# The problem: https://projecteuler.net/problem=43
# This is worded kind of strangely - I assume they mean the following:
# 	Each substring (starting at the second digit) of length 3 is divisible by an increasing prime
# Some limitations:
# the 4th digit must be even (cuts out half of the numbers)
# the 6th digit must be 5 or 0 (cuts out 4/5 of the numbers)
from itertools import permutations

pandigitals = permutations("0123456789")
totalSum = 0
for p in pandigitals:
	if int("".join(p[7:])) % 17:
		continue
	if int("".join(p[6:-1])) % 13:
		continue
	if int("".join(p[5:-2])) % 11:
		continue
	if int("".join(p[4:-3])) % 7:
		continue
	if int("".join(p[3:-4])) % 5:
		continue
	if int("".join(p[2:-5])) % 3:
		continue
	if int("".join(p[1:-6])) % 2:
		continue
	totalSum += int("".join(p))
print(totalSum)