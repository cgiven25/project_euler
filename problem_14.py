# The problem: https://projecteuler.net/problem=14
# This is the most naive interpretation possible, but it's not THAT bad to brute force.
# It took 20 seconds to arrive at the correct answer.
# To improve this, I would probably have to research the Collatz sequence more.
# Large improvements would probably require some method that can skip a part of the sequence without losing the number of steps

longest_num = 0
longest_seq = 0
for i in range(2, 1000000):
	n = i
	seq_len = 0
	while n != 1:
		seq_len += 1
		if n % 2:
			n = 3*n + 1
		else:
			n = n / 2
	if seq_len > longest_seq:
		longest_seq = seq_len
		longest_num = i
print(longest_num)