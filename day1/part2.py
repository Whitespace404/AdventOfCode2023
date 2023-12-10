class Found(Exception):
    pass


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

reversed_numbers = {
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

for word in words:
    print("=" * 30)
    evaluator = ""
    leftmost = ""
    rightmost = ""

    try:
        for character in word:
            evaluator += character
            if character.isdigit():
                leftmost = character
                print(leftmost)
                raise Found

            for number in numbers_words.keys():
                if number in evaluator:
                    leftmost = numbers_words.get(number)
                    print(leftmost)
                    raise Found

    except Found:
        evaluator = ""
        for character in word[::-1]:
            if character.isdigit():
                rightmost = character
                print(rightmost)
                break
            evaluator += character

            for number in reversed_numbers.keys():
                if number in evaluator:
                    rightmost = reversed_numbers.get(number)
                    print(rightmost)
                    break
            else:
                continue  # only real use of continue anywhere tbh lol
            break

    N = str(leftmost) + str(rightmost)
    answer += int(N)

print(answer)
