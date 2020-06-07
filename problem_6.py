# The problem: https://projecteuler.net/problem=6
# Python handles large numbers very well, so this is basically just exactly what the problem asked for.  No tricks

nums = [x for x in range(1, 101)]
nums_squares = [x**2 for x in nums]
print(sum(nums)**2 - sum(nums_squares))
