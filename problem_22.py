# The problem: https://projecteuler.net/problem=22
# This one was pretty easy, just had to follow the instructions.

with open("problem_22.txt") as names_file:
	names = names_file.read().lower().replace("\"", "").split(",")
	names.sort()

score = 0
i = 1
for name in names:
	name_score = 0
	for char in name:
		name_score += ord(char) - 96
	name_score *= i
	score += name_score
	i += 1
print(score)