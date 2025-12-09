answer = 1

debug = True

lines = []
source = 0
width = 0
beams = []

def follow_beam(row, col):
    if row < 0 or row >= len(lines) or col < 0 or col >= width:
        return;

    # if lines[row][col] != '^':
    #     beams.append([row, col])

    if lines[row][col] == '^':
        global answer
        answer += 1
        follow_beam(row + 1, col - 1)
        follow_beam(row + 1, col + 1)
    else:
        follow_beam(row + 1, col)

with open('input.txt', 'r') as input:
    lines = [line.strip() for line in input.readlines()]

width = len(lines[0])
source = lines[0].find('S')

if debug: 
    print("Lines:")
    for line in lines:
        print(line)
    print(f"\nWidth: {width}, Num of Lines: {len(lines)}")

follow_beam(0, source)

# for row, line in enumerate(lines):
#     for col, char in enumerate(line):
#         if [row, col] in beams:
#             print('|', end='')
#         else:
#             print(char, end='')
#     print()

print(f"\n\n{answer}")
