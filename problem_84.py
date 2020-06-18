# The problem: https://projecteuler.net/problem=84
# A data structures problem, kind of
# Idea -- just play for like 100,000 rolls
# This worked the first time, but the squares 24 and 15 are very close in probability.
# 500,000 rolls seems to fix this for the most part.
import random
import math

# Move to next railroad, utility, or back 3 spaces 
def move_next(movement):
	global square
	if movement == "R":
		if square == 7:
			return 15
		elif square == 22:
			return 25
		elif square == 36:
			return 5
	elif movement == "U":
		if square in [7, 36]:
			return 12
		elif square == 22:
			return 28
	elif movement == "B":
		return square - 3

def process_community_chest():
	global square
	card = next(community_chest)
	if card == -1:
		return square
	else:
		return card

def process_chance():
	global square
	card = next(chance)
	if card == -1:
		return square
	else:
		try:
			return card[0](card[1])
		except TypeError:
			return card

def process_go_to_jail():
	return 10

event_squares = {2: process_community_chest, 33: process_community_chest, 7: process_chance, 22: process_chance, 36: process_chance, 30: process_go_to_jail}

# Set up Community Chest/Chance decks
community_chest_cards = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 10]
chance_cards = [-1, -1, -1, -1, -1, -1, 0, 10, 11, 24, 39, 5, (move_next, "R"), (move_next, "R"), (move_next, "U"), (move_next, "B")]
random.shuffle(community_chest_cards)
random.shuffle(chance_cards)
community_chest = (community_chest_cards[i % 16] for i in range(100000))
chance = (chance_cards[i % 16] for i in range(100000))

landing_spots = {i:0 for i in range(40)}

square = 0
NUM_ROLLS = 250000
previous_rolls = [-1, -2, -3]
for i in range(NUM_ROLLS):
	roll = random.randint(1, 4) + random.randint(1, 4)
	previous_rolls.insert(0, roll)
	del previous_rolls[3]
	if len(set(previous_rolls)) == 1:
		square = 10
	else:
		square = (square + roll) % 40
		if square in event_squares:
			square = event_squares[square]()
		landing_spots[square] += 1

card_freq = list(landing_spots.keys())
card_freq.sort(key = lambda c: landing_spots[c], reverse=True)
print(card_freq[0:3])