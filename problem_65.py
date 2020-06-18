# The problem: https://projecteuler.net/problem=65
# Very similar to problem 57
# This one is really 

from fractions import Fraction

j = 2
coefficients = [1, 2]
for i in range(1, 99):
	if not i % 3:
		coefficients.append(j*2)
		j += 1
	else:
		coefficients.append(1)

# used to verify that it was working, setting to 100 runs the actual problem
test_num = 100
frac = 0
for i in range(test_num, 1, -1):
	frac = Fraction(1, frac + coefficients[i-2])
frac = 2 + frac

print(sum(map(int, str(frac.numerator))))