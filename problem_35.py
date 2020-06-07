# The problem: https://projecteuler.net/problem=35
# Ok so I got the right answer but I think I did it kind of sloppily
# Basically, I reduced the testing space by checking if there was an even number in the prime.  If there is, it cannot be circular.
# Then, I shift each only-odd prime by 1 digit until I've checked everything, and if they are all prime then I add it to the list.
# After reading the discussions I could have also discluded "5" as a digit, because when it is at the end it will always be divisible by 5.

def prime_test(n):
	i = 2
	while i*i <= n:
		if (n % i) == 0:
			return False
		i += 1
	return True

primes = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]
circular = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]
for i in range(101, 1000000, 2):
	if i in circular:
		continue

	num_str = str(i)
	if not("0" in num_str or "2" in num_str or "4" in num_str or "6" in num_str or "8" in num_str):
		if prime_test(i):
			primes.append(i)
			is_circular = True
			new_num = num_str
			for j in range(len(num_str) - 1):
				new_num = new_num[-1] + new_num[:-1]
				if int(new_num) not in primes:
					if not prime_test(int(new_num)):
						is_circular = False
						break
					else:
						primes.append(int(new_num))
			if is_circular:
				circular.append(i)
print(len(set(circular)))