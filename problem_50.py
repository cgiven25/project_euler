# The problem: https://projecteuler.net/problem=50
# This is kind of a bad solution.
# Basically, I start by finding all the primes below 1 million.
# Then, I create a window with the provided max (which was 21).
# 	I slide the window across the list of primes, and see if the sum is in the list.
# 	If it is, update the max window and max prime, and then increment the window
#		since we don't need to check for smaller windows anymore.

def prime_test(n):
	i = 2
	while i*i <= n:
		if (n % i) == 0:
			return False
		i += 1
	return True

# Takes like 5 seconds
primes = [i for i in range(3, 1000000, 2) if prime_test(i)]
primes.insert(0, 2)

max_window = 21
max_prime = 953
for prime in primes[::-1]:
	less_than_list = primes[:primes.index(prime)]
	if len(less_than_list) < max_window:
		continue
	else:
		window = max_window + 1
		while sum(primes[:window]) < prime:
			for i in range(len(less_than_list) - window + 1):
				if sum(primes[i:i+window]) > prime:
					break
				if sum(primes[i:i+window]) == prime:
					max_window = window
					max_prime = prime
					print(max_window, max_prime)
					break
			window += 1
print(max_window, max_prime)