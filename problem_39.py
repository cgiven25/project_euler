# The problem: https://projecteuler.net/problem=39
# Another way to phrase the question: For which perimeter p <= 1000 is there the most pythagorean triples?
import math

max_triples = 3
max_p = 120
for p in range(12, 1001):
	current_triples = 0
	for a in range(2, math.ceil(p/3)):
		if (p**2 - 2*p*a) % (2*p - 2*a) == 0:
			current_triples += 1
	if current_triples > max_triples:
		max_triples = current_triples
		max_p = p
print(max_p, max_triples)
