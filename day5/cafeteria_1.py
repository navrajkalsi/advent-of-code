answer = 0 # fresh
fresh_ids = []

debug = False

ranges = []
ids = []

with open('input.txt', 'r') as input:
    lines = [line.strip() for line in input.readlines()]
    blank_line = -1

    for index, line in enumerate(lines):
        if line == '':
            blank_line = index
            break

    ranges.extend(lines[:blank_line])
    ids.extend(lines[(blank_line + 1):])

if debug:
    print(f"Ranges: {ranges}\nIDs: {ids}")

for id in ids:
    id = int(id)
    for rng in ranges:
        lower_index = int(rng.split('-')[0])
        upper_index = int(rng.split('-')[1]) + 1
        if id in range(lower_index, upper_index):
            fresh_ids.append(id)
            answer += 1
            break

print(f"Fresh IDs: {fresh_ids}\n")
print(answer)
