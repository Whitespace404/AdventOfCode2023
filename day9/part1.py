with open("input.txt", "r") as f:
    lines = [line.rstrip("\n") for line in f.readlines()]

ans = 0

for line in lines:
    differences_matrix = []

    terms = [int(p) for p in line.split()]
    differences_matrix.append(terms)

    while True:
        current_row_differences = []

        for i in range(len(terms) - 1):
            difference_between_terms = terms[i + 1] - terms[i]
            current_row_differences.append(difference_between_terms)

        differences_matrix.append(current_row_differences)

        if current_row_differences.count(0) == len(current_row_differences):
            break

        terms = current_row_differences

    differences_matrix.reverse()
    differences_matrix[0].append(0)

    for current_row_index in range(len(differences_matrix) - 1):
        row_above = differences_matrix[current_row_index + 1]

        # Calculate the extrapolation by adding the last element of the next row with the last element of this row
        extrapolation = row_above[-1] + differences_matrix[current_row_index][-1]

        # Adding the extrapolation to the end of the list of the next list in our matrix
        differences_matrix[current_row_index + 1].append(extrapolation)

    ans += differences_matrix[-1][-1]


print(ans)
