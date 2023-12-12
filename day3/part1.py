import sys

sys.path.append("../")

import utils
import pprint

lines = utils.get_lines_input("input.txt")

symbols_locations = []

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if not lines[i][j].isdigit() and lines[i][j] != ".":
            symbols_locations.append((i, j))

numbers_with_locations = []

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j].isdigit():
            numbers_with_locations.append((lines[i][j], (i, j)))

pprint.pprint(numbers_with_locations, indent=4)
