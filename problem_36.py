# The problem: https://projecteuler.net/problem=36
# I can probably just brute-force this.

palindromes = [i for i in range(1, 1000000) if str(i) == str(i)[::-1] and bin(i)[2:][::-1] == bin(i)[2:]]
print(sum(palindromes))