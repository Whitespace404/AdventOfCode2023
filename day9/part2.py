with open("input.txt", "r") as f:
    lines = [line.rstrip("\n") for line in f.readlines()]

ans = 0

for line in lines:
    differences_matrix = []
    travers = []
    running = True

    terms = list(
        reversed([int(p) for p in line.split()])
    )  # same as part 1 except this is reversed
    differences_matrix.append(terms)
    it = terms.copy()

    while running:
        this = []
        for i in range(len(terms) - 1):
            dif = terms[i + 1] - terms[i]
            this.append(dif)
        differences_matrix.append(this)

        if this.count(0) == len(this):
            running = False

        terms = this

    travers = list(reversed(differences_matrix))

    travers[0].append(0)

    for R in range(len(travers) - 1):  # 0 1
        x = travers[R + 1]
        travers[R + 1].append(x[-1] + travers[R][-1])

    ans += travers[-1][-1]


print(ans)
