import sys

sys.path.append("../")

import utils

lines = utils.get_lines_input("input.txt")

valid_ids = []

for line in lines:
    draws = line.partition(":")[2].split(";")
    good = True
    for draw in draws:
        n_cube = draw.lstrip(" ").rstrip(" ").split(",")

        print(n_cube)
        for d in n_cube:
            r, g, b = 0, 0, 0
            n, c = d.lstrip(" ").split(" ")
            if c.startswith("r"):
                if int(n) > r:
                    r += int(n)
            elif c.startswith("g"):
                if int(n) > g:
                    g += int(n)
            elif c.startswith("b"):
                if int(n) > b:
                    b += int(n)

            if r > 12 or g > 13 or b > 14:
                good = False

    if good:
        valid_ids.append(int(line.partition(":")[0].split(" ")[-1]))

print(sum(valid_ids))
