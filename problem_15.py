# The problem: https://projecteuler.net/problem=15
# I didn't have to write code for this one.  Instead, just consider the possible moves.
# You need 40 moves to get to the bottom-right.  20 of them will be to the right, 20 of them will be down.
# 40 choose 20 is the correct answer.  Out of 40 moves, choose 20 of them, and go right for those moves.  The rest will be down by default.
# The answer is 137846528820, produced from some website I found