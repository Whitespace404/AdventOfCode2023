with open("input.txt", "r") as f:
    words = f.read().split(",")


def hashify(word):
    hash_value = 0
    for char in word:
        hash_value += ord(char)
        hash_value *= 17
        hash_value %= 256

    return hash_value


boxes_by_lenses = dict()

for word in words:
    delimeter = "=" if "=" in word else "-"
    label = word.split(delimeter)[0]
    box_number = hashify(label)
    focal_length = word.split(delimeter)[1]

    lenses = boxes_by_lenses.get(box_number)

    if delimeter == "=":
        if lenses is not None:
            for slot_number in range(len(lenses) - 1):
                if boxes_by_lenses[box_number][slot_number][0] == label:
                    boxes_by_lenses[box_number][slot_number] = [label, focal_length]
                    break
            else:
                boxes_by_lenses[box_number].append([label, focal_length])
        else:
            boxes_by_lenses[box_number] = [[label, focal_length]]

    if delimeter == "-":
        if lenses is not None:
            for slot_number in range(len(lenses)):
                if boxes_by_lenses[box_number][slot_number][0] == label:
                    boxes_by_lenses[box_number].pop(slot_number)
                    break


ans = 0
for box in boxes_by_lenses:
    for slot_number, tup in enumerate(boxes_by_lenses[box], 1):
        focal_length = int(tup[1])

        focusing_strength = (1 + box) * slot_number * focal_length
        ans += focusing_strength

print(ans)
