# The problem: https://projecteuler.net/problem=54
# This is basically a data structure problem.
# How can I organize the hands in such a way that they are easy to score?
# My first 10% problem completed! :)

from collections import Counter

CARD_VALUES = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
			   "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
HAND_VALUES = {"HC": 1, "OP": 2, "TP": 3, "TK": 4, "ST": 5, "FL": 6,
			   "FH": 7, "FK": 8, "SF": 9}

# Return verdict on hand quality, as well as the card values for breaking ties
def determine_hand(cards, player):
	suits = Counter([card[1] for card in cards])
	values = Counter(sorted([CARD_VALUES[card[0]] for card in cards]))
	value_counter = values.most_common(5)

	# Check for straight and flush
	flush = len(set(suits)) == 1
	straight = sorted(values.elements()) == list(range(min(values), max(values) + 1))

	# Check for pair-like hands
	four_of_a_kind = (value_counter[0][1] == 4, value_counter[0][0])
	three_of_a_kind = (value_counter[0][1] == 3, value_counter[0][0])
	pairs = [value_counter[i][0] for i in range(len(value_counter)) if value_counter[i][1] == 2]

	if straight and flush:
		return "SF", max(values)
	if four_of_a_kind[0]:
		return "FK", four_of_a_kind[1]
	if three_of_a_kind[0] and len(pairs) == 1:
		return "FH", three_of_a_kind[1]
	if flush:
		return "FL", max(values)
	if straight:
		return "ST", max(values)
	if three_of_a_kind[0]:
		return "TK", three_of_a_kind[1]
	if len(pairs) == 2:
		return "TP", [max(pairs), min(pairs), value_counter[2][0]]
	if len(pairs) == 1:
		remaining_cards = list(reversed(list(values)))
		remaining_cards.remove(pairs[0])
		remaining_cards.insert(0, pairs[0])
		return "OP", remaining_cards
	else:
		return "HC", list(reversed(list(values)))

with open("problem_54.txt") as poker_file:
	hands = poker_file.read().strip("\n").split("\n")

poker_hands = []
for hand in hands:
	new_hand = hand.split(" ")
	poker_hands.append([new_hand[:5], new_hand[5:]])

p1_wins = 0
for match in poker_hands:
	p1_hand = determine_hand(match[0], 1)
	p2_hand = determine_hand(match[1], 2)
	if p1_hand[0] != p2_hand[0]:
		p1_wins += 1 & (HAND_VALUES[p1_hand[0]] > HAND_VALUES[p2_hand[0]])
	# Settle ties
	else:
		if p1_hand[0] in ["SF", "FK", "FH", "FL", "ST", "TK"]:
			p1_wins += 1 & (p1_hand[1] > p2_hand[1])
		else:
			i = 0
			while True:
				if p1_hand[1][i] != p2_hand[1][i]:
					p1_wins += 1 & (p1_hand[1][i] > p2_hand[1][i])
					break
				i += 1
print(p1_wins)