with open("input.txt", "r") as f:
    a = f.readlines()

words = [i.rstrip("\n") for i in a]

answer = 0
for word in words:
    first_digit, last_digit = 0, 0
    for character in word:
        if character.isdigit():
            first_digit = int(character)
            break
    for character in word[::-1]:
        if character.isdigit():
            last_digit = int(character)
            break

    n = str(first_digit) + str(last_digit)

    answer += int(n)

print(answer)
