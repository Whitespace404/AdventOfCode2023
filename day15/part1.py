with open("input.txt", "r") as f:
    words = f.read().split(",")

ans = 0

for word in words:
    hash_value = 0
    for character in word:
        hash_value += ord(character)
        hash_value *= 17
        hash_value %= 256
    ans += hash_value

print(ans)
