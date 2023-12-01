# Couldn't get part 2.

with open("input.txt", "r") as f:
    a = f.readlines()

words = [i.rstrip("\n") for i in a]

numbers_words = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

reversed_numbers_words = {
    "eno": 1,
    "owt": 2,
    "eerht": 3,
    "ruof": 4,
    "evif": 5,
    "xis": 6,
    "neves": 7,
    "thgie": 8,
    "enin": 9,
}

answer = 0
number_names = numbers_words.keys()

for word in words:
    imp = []
    holder = ""

    for letter in word:
        for name in number_names:
            if name in holder:
                imp.append(name)
                holder = ""

        holder += letter

    if imp:
        word = word.replace(imp[0], str(numbers_words.get(imp[0]))).replace(
            imp[-1], str(numbers_words.get(imp[-1]))
        )

    print(word)

    first_digit = 0
    last_digit = 0
    for i in word:
        if i.isdigit():
            first_digit = int(i)
            break
    for j in word[::-1]:
        if j.isdigit():
            last_digit = int(j)
            break

    n = str(first_digit) + str(last_digit)
    n = int(n)

    answer += n
print(answer)
