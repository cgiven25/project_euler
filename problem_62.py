# The problem: https://projecteuler.net/problem=62
# Seems easy enough, I worry about time though
# I'm gonna try doing this in the standard library, may run into precision problems
# I'm also going to assume I can start above 405.  
# If I run across a cube but don't get 5 permutations which work, I can add it to "exclude"
# nevermind, there are 8! permutations 
# New idea - basically stolen - cube each number until a permutation of its digits appears 5 times.
# 	I'm still assuming I can start at 406
from itertools import permutations

cubes = {}
i = 406
while True:
	cube = sorted(list(str(i**3)))
	cubes[i] = cube
	# We have the answer, now just find the smallest cube in the list
	if list(cubes.values()).count(cube) == 5:
		cube_family = [num for num in cubes if cubes[num] == cube]
		print(min(cube_family)**3)
		break
	i += 1