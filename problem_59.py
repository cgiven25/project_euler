# The problem: https://projecteuler.net/problem=59
# I have trained for this
from collections import Counter
from itertools import permutations

with open("problem_59.txt") as ciphertext_file:
	ciphertext = ciphertext_file.read().strip("\n").split(",")
	ciphertext = list(map(int, ciphertext))

with open("problem_59_dict.txt") as dictionary_file:
	dictionary = dictionary_file.read().strip("\n").split("\n")

alphabet = "abcdefghijklmnopqrstuvwxyz"

for key in permutations(alphabet, 3):
	key_gen = (key[i % 3] for i in range(len(ciphertext)))
	plaintext = ""
	for char in ciphertext:
		key_val = ord(next(key_gen))
		plaintext += chr(char ^ key_val)
	plaintext_counter = Counter(plaintext).most_common()
	
	words = plaintext.split(" ")
	eng_words = 0
	for word in words:
		if word in dictionary:
			eng_words += 1
	if eng_words / len(words) >= .5:
		print(plaintext)
		total = 0
		for char in plaintext:
			total += ord(char)
		print(total)
		break