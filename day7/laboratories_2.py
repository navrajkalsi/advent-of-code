answer = 0

debug = True

lines = []
length = 0
source = 0
width = 0
beams = []

# recursive approach
def follow_beam(row, col):
    if row < 0 or row >= length or col < 0 or col >= width:
        if row == length:
            global answer
            answer += 1
        return;

    if lines[row][col] != '^':
        beams.append([row, col])

    if lines[row][col] == '^':
        follow_beam(row + 1, col - 1)
        follow_beam(row + 1, col + 1)
    else:
        follow_beam(row + 1, col)

with open('input.txt', 'r') as input:
    lines = [line.strip() for line in input.readlines()]

width = len(lines[0])
length = len(lines)
source = lines[0].find('S')

if debug: 
    print("Lines:")
    for line in lines:
        print(line)
    print(f"\nWidth: {width}, Num of Lines: {length}")

follow_beam(0, source)

# for row, line in enumerate(lines):
#     for col, char in enumerate(line):
#         if [row, col] in beams:
#             if row == 0 and col == source:
#                 print('S', end='')
#             else:
#                 print('|', end='')
#         else:
#             print(char, end='')
#     print()

print(f"\n\n{answer}")
