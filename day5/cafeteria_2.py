answer = 0 # total fresh ids

debug = True

ranges = []

with open('input.txt', 'r') as input:
    for line in input.readlines():
        line = line.strip()
        if line == '':
            break

        line = line.split('-')
        ranges.append([int(line[0]), int(line[1]) + 1])

if debug:
    print(f"Ranges: {ranges}\n")

ranges.sort(key=lambda rng: rng[0])

if debug:
    print(f"Sorted ranges: {ranges}\n")

new_ranges = []
index = 0
while index < len(ranges):
    rng = ranges[index]
    min = rng[0]
    max = rng[1]
    index += 1

    while index < len(ranges):
        if ranges[index][0] > max: # cannot merge ranges
            break
        if max < ranges[index][1]: # only change max if the new max will be greater
            max = ranges[index][1]
        index += 1

    new_ranges.append([min, max])

if debug:
    print(f"New ranges: {new_ranges}\n")

for rng in new_ranges:
    answer += rng[1] - rng[0]

# simplifying ranges
print(answer)
