# 10! total orderings: 3,628,800
# 9! for each starting digit (362,880)
# This means that the starting digit will be 2.
# Take the smallest permutation starting with 2.
#   This is 2013456789.  This is the 725,761th permutation.
# (this is where I did things wrong but if you subtract accurately it should work out)
# 1,000,000 - 725,760 = 274,240.
# Since we know the starting digit is 2, we can consider the 9 possibilites for the second digit.
# The problem: https://projecteuler.net/problem=24
# I had the right idea for this one, but cheated a little bit because I couldn't get the right answer after a few attempts.
# The corret reasoning is below

# There are 8! permutations of the last 8 digits.  8! = 40,320.
# ceil(274,240 / 40,320) = 7, so 7 is the second digit.
# This leaves us 32,320 permutations until we are done.
# 7! = 5040.
# We are left with 2 7 8 _ _ _ _ _ _ _, with 2080 permutations left
# 6! = 720
# We are left with 2 7 8 3 _ _ _ _ _ _, with 640 permutations left
# 5! = 120
# We are left with 2 7 8 3 9 _ _ _ _ _, with 40 permutations left
# 4! = 24
# We are left with 2 7 8 3 9 1 _ _ _ _, with 16 permutations left
# 3! = 6
# We are left with 2 7 8 3 9 1 5 _ _ _, with 4 permutations left
# 2! = 4
# We are left with 2 7 8 3 9 1 5 4 6 0 as our final answer