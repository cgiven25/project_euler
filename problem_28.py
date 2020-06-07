# The problem: https://projecteuler.net/problem=28
# I noticed a pattern in the diagonals -- each diagonal is 2*i apart, where i is the "layer" they're on.  Besides 1, there are 4 diagonals in each layer.
# There are 500 layers (the center digit in a row and then 500 on each side, so 500 layers besides the 1 in the center)

totSum = 1
prevNum = 1
for i in range(1, 501):
	for j in range(4):
		totSum += prevNum + 2*i
		prevNum += 2*i
print(totSum)