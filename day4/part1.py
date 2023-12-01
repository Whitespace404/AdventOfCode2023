import sys

sys.path.append("../")

import utils

lines = utils.get_lines_input("input.txt")


def get_ints(line):
    out = []
    num = ""
    for c in line + " ":
        if c.isdigit():
            num += c
        elif c == " ":
            out.append((num))
            num = ""

    return [i for i in out if i.isdigit()]


answer = 0

powers_of_two = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
for line in lines:
    game_id_winning_cards, your_cards = line.split("|")
    game_id = game_id_winning_cards.split(":")[0].lstrip("Card ")
    winning_cards = get_ints(game_id_winning_cards.split(":")[1])
    cards = get_ints(your_cards)

    winners = 0
    for card in winning_cards:
        if cards.count(card) > 0:
            winners += 1

    power_sum = powers_of_two[winners]

    answer += power_sum

print(answer)
