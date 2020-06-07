# The problem: https://projecteuler.net/problem=1
# This solution is pretty self-explanatory

print(sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0]))