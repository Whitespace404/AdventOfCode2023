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

cards_by_copies = {i: 1 for i in range(1, 205)}
n_cards_by_copies = cards_by_copies.copy()
iterations = 0

while (all([True for a in n_cards_by_copies.values() if a == 1])) and iterations != 0:
    for line in lines:
        game_id_winning_cards, your_cards = line.split("|")
        game_id = game_id_winning_cards.split(":")[0].lstrip("Card ")

        winning_cards = get_ints(game_id_winning_cards.split(":")[1])
        cards = get_ints(your_cards)

        cards_won = 0
        for card in winning_cards:
            if cards.count(card) > 0:
                cards_won += 1

        for c in range(1, cards_won):
            print("Game ID", int(game_id) + c)
            print(cards_won)


print(sum(cards_by_copies.values()))

print(answer)
