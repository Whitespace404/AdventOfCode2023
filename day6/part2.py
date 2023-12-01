time_by_distance = eval(open("input.txt").readlines()[1].rstrip("\n"))

answer = 1

for duration, record_distance in time_by_distance.items():
    possible_press_durations = []
    for i in range(duration):
        remaining_time = duration - i
        distance_travelled = i * remaining_time

        if distance_travelled >= record_distance:
            possible_press_durations.append(i)

    answer *= len(possible_press_durations)

print(answer)
