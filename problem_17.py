# The problem: https://projecteuler.net/problem=17
# This one is actually pretty self-explanatory.
# I think my code for this is garabage, I could probably do this faster by hand than it took to write this

transformation = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 
				  10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
				  18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy",
				  80: "eighty", 90: "ninety"}
num_letters = 0

def decode_two():
	pass

def decode_three():
	pass

for i in range(1, 1000):
	new_num = 0
	try:
		new_num += len(transformation[i]) 
	except KeyError:
		num = str(i)
		if len(num) == 2:
			new_num += len(transformation[int(num[0] + "0")]) + len(transformation[int(num[1])])
		elif len(num) == 3:
			new_num += 7 + len(transformation[int(num[0])])
			try:
				new_num += 3 + len(transformation[int(num[1] + num[2])])
			except KeyError:
				if num[2] + num[1] != "00":
					if num[2] != "0":
						new_num += 3 + len(transformation[int(num[2])])
					if num[1] != "0":
						new_num += len(transformation[int(num[1] + "0")])
					if num[1] != "0" and num[2] == "0":
						new_num += 3
	num_letters += new_num
print(num_letters + 11)