# The problem: https://projecteuler.net/problem=58
# Diagonals are 2*i apart, where i is the layer they are on
def prime_test(n):
	i = 2
	while i*i <= n:
		if (n % i) == 0:
			return False
		i += 1
	return True

numPrimes = 8
totalNums = 13
i = 4
prevNum = 49
while numPrimes/totalNums >= .1:
	for j in range(4):
		newNum = prevNum + 2*i
		if prime_test(newNum):
			numPrimes += 1
		totalNums += 1
		prevNum = newNum
	i += 1
print(2*(i-1) + 1)
