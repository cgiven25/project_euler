# The problem: https://projecteuler.net/problem=42
# First I did some analysis on the file.  The longest word has 14 letters, so a max score of 26*14=364
# So I just need to calculate the triangular numbers up to 364
# After calculating those, it's pretty similar to the word score one

words = []
with open("problem_42.txt") as word_file:
	words = word_file.read().lower().replace("\"", "").split(",")

triangular = [1]
i = 2
while max(triangular) < 364:
	triangular.append((i*(i+1))//2)
	i += 1

triangular_words = 0
for word in words:
	score = 0
	for letter in word:
		score += ord(letter) - 96
	if score in triangular:
		triangular_words += 1
print(triangular_words)
