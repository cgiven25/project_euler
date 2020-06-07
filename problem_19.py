# The problem: https://projecteuler.net/problem=19
# A simple utilization of Zeller's congruence: https://en.wikipedia.org/wiki/Zeller%27s_congruence
# Once you work out the year changes (Zeller's algorithm is a bit confusing), it's just following steps. 

sundays = 0

year = 1900
month = 13
# Go from January 1901 to December 2000
while not(year == 2000 and month == 13):
	# Zeller's congruence
	q = 1
	K = year % 100
	J = year // 100
	result = (q + 13*(month + 1)//5 + K + K // 4 + J // 4 - 2*J) % 7
	if result == 1:
		sundays += 1
	# set up for next iteration
	if month == 14:
		month = 3
		year += 1
	else:
		month += 1
print(sundays)