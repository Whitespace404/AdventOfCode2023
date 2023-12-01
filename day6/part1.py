# I initially had hardcoded the inputs, but had to
# obfuscate them because AoC inputs are not licenced for reproduction or distribution.
# see https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs for details.

time_by_distance = eval(open("input.txt").readlines()[0].rstrip("\n"))

# however the following line shows what the dictionary will
# look like after I read it from the file
# (using the sample inputs, of course)

# time_by_distance = {7: 9, 15: 40, 30: 200}

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
