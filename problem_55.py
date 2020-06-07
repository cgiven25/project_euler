# The problem: https://projecteuler.net/problem=55

lychrel = 0
for i in range(1, 10000):
	current_sum = i
	for j in range(50):
		current_sum += int(str(current_sum)[::-1])
		if str(current_sum) == str(current_sum)[::-1]:
			break
	if j == 49:
		lychrel += 1
print(lychrel)