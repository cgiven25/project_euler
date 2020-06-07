# The problem: https://projecteuler.net/problem=44
# Idea - the first pair found with this property is the smallest
# I'll try generating 100 terms, and then just checking each pair
# 	It's not in the first 100
# 	Nor in the first 1000
#	The correct answer was found in the 1000 - 10000 range

pentagonal = [n*(3*n - 1)//2 for n in range(1000, 10000)]
for i in range(len(pentagonal) - 1):
	for j in range(i+1, len(pentagonal)):
		if (pentagonal[i] + pentagonal[j] in pentagonal) and (pentagonal[j] - pentagonal[i] in pentagonal):
			print(pentagonal[j] - pentagonal[i])
			exit()