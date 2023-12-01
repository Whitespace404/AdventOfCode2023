import sys

sys.path.append("../")

import utils

lines = utils.get_lines_input("input.txt")

answer = 0
for line in lines:
    draws = line.partition(":")[2].split(";")

    r, g, b = [], [], []
    for draw in draws:
        n_cube = draw.lstrip(" ").rstrip(" ").split(",")

        for d in n_cube:
            n, c = d.lstrip(" ").split(" ")

            print(n, c)
            if c.startswith("r"):
                r.append(int(n))
            elif c.startswith("g"):
                g.append(int(n))
            elif c.startswith("b"):
                b.append(int(n))

    power = max(r) * max(g) * max(b)

    answer += power

print(answer)
