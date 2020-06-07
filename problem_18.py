# The problem: https://projecteuler.net/problem=18
# Using Cody's algorithm

with open("problem_18.txt") as triangle_of_death:
	rows_start = triangle_of_death.read().strip("\n").split("\n")
	
rows = []
for i in range(len(rows_start)):
	rows.append([int(x) for x in rows_start[i].split(" ")])

for i in range(1, len(rows)):
	for j in range(len(rows[i])):
		if j == 0:
			rows[i][j] += rows[i-1][j]
		elif j == len(rows[i]) -1:
			rows[i][j] += rows[i-1][j-1]
		else:
			rows[i][j] += max([rows[i-1][j-1], rows[i-1][j]])
print(max(rows[len(rows) - 1]))