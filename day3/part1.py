# half baked spagetti code
# there's got to be a better way to do this which i dont see unfortunately

import sys

sys.path.append("../")

import utils

lines = utils.get_lines_input("input.txt")

answer = 0

for line in range(len(lines)):
    digits = []
    digit_holder = ""

    for character in range(len(lines[line])):
        x = lines[line][character]
        if x != "." and not x.isdigit():
            print(x, "triggered")
            surrounding_chars = []
            try:
                surrounding_chars = [
                    lines[line - 1][character - 1],
                    lines[line - 1][character],
                    lines[line - 1][character + 1],
                    lines[line][character - 1],
                    lines[line][character + 1],
                    lines[line + 1][character - 1],
                    lines[line + 1][character],
                    lines[line + 1][character + 1],
                ]
            except:
                pass

            for s in surrounding_chars:
                if s.isdigit():
                    pass

            print(surrounding_chars)
            quit()
