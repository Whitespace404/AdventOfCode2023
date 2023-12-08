import sys

sys.path.append("../")
import utils

answer = 0

lines = utils.get_lines_input("input.txt")

superiority = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

fives = set()  # AAAAA
fours = set()  # AAAA0
full_house = set()  # AAA00
threes = set()  # AAA01
twos = set()  # AA001
ones = set()  # AA012
highs = set()  # A0123


def custom_sort(old_list):
    hands = [i[0] for i in old_list]
    return sorted(hands, key=lambda word: [superiority.index(c) for c in word])


for line in lines:
    hand, rank = line.split(" ")
    counts = []
    for card in hand:
        counts.append(hand.count(card))

    config = "".join(str(i) for i in counts)

    if config == "55555":  # AAAAA
        fives.add((hand, rank))
    elif config == "44441":  # AAAA0
        fours.add((hand, rank))
    elif config == "33322":  # AAA00
        full_house.add((hand, rank))
    elif config == "33311":  # AAA01
        threes.add((hand, rank))
    elif config == "22221":  # AA001
        twos.add((hand, rank))
    elif config == "22111":  # AA012
        ones.add((hand, rank))
    elif config == "11111":  # A0123
        highs.add((hand, rank))

    print(custom_sort(fives))
