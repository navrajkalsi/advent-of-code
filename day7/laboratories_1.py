answer = 0

debug = True

lines = []
width = 0
beams = []

with open('demo.txt', 'r') as input:
    lines = [line.strip() for line in input.readlines()]

width = len(lines[0])
beams = [lines[0].find('S')]

if debug:
    print("Lines:")
    for line in lines: print(line)
    print(f"\nWidth: {width}, Source at: {beams[0]}\n\n{lines[0]}", end="")

for line in lines[1:]:
    new_beams = []
    for index, char in enumerate(line):
        if index in beams:
            if char != '^':
                new_beams.append(index)
                continue
            if index != 0 and index - 1 not in new_beams:
                new_beams.append(index - 1)
            if index != width - 1 and index + 1 not in new_beams:
                new_beams.append(index + 1)
            answer += 1

    beams = new_beams

    if debug:
        print()
        for index in range(width):
            if index in beams:
                print("|", end="")
            else:
                print(line[index], end="")

print(f"\n\n{answer}")
