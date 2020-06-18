# The problem: https://projecteuler.net/problem=81
# This reminds me of the one Cody solved.
# For each cell in the matrix, add the max of the right element and the one below.
# If the right isn't available, you must go down, and if you can't go down, you must go right.

matrix = []
with open("problem_81.txt") as matrix_file:
	lines = matrix_file.read().split("\n")
	for line in lines:
		matrix.append(list(map(int, line.split(","))))

matrix = [[131, 673, 234, 103, 18], [201, 96, 342, 965, 150],
		  [630, 830, 746, 422, 111], [537, 699, 497, 121, 956],
		  [805, 723, 524, 37, 331]]
for r in range(len(matrix)):
	for c in range(len(matrix)):
		if (r, c) == (0, 0):
			continue
		else:
			# 