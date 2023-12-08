instructions = open("input.txt").readline()

lines = [line.rstrip("\n") for line in open("input.txt")][2:]

loops = 0


def get_node(loc):
    for line in lines:
        if line.split(" = ")[0] == loc:
            return line.split(" = ")
        else:
            print(loc)


running = True
current_node = ("BBB", "BBB")

while running:
    for letter in instructions:
        if letter == "R":
            new_node = get_node(current_node[0])[1]
            current_node = new_node
        else:
            new_node = get_node(current_node[0])[1]
            current_node = new_node

    loops += 1

    if get_node(current_node[0]) == "ZZZ":
        running = False

get_node("ZZZ")
answer = loops * len(lines)
