with open("input.txt", "r") as f:
    lines = [i.rstrip("\n") for i in f.readlines()]


def get_load(lines):
    TOTAL_ROWS = len(lines)
    ans = 0

    for row_number, line in enumerate(lines):
        rows_under = TOTAL_ROWS - row_number

        number_of_rocks = line.count("O")

        ans += number_of_rocks * rows_under

    return ans


for row in range(len(lines)):
    for i in range(len(lines[0])):
        if i == ".":
            pass
