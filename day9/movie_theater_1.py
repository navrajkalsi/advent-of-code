answer = 0

debug = True

cols_start = 10
rows_start = 10
cols = 0
rows = 0
tiles = []

def calc_area(first, second):
    return (second[0] - first[0] + 1) * (second[1] - first[1] + 1)

with open('demo.txt', 'r') as input:
    tiles = [line.strip().split(',') for line in input.readlines()]

for index, tile in enumerate(tiles): # converting to ints
    col = int(tile[0])
    row = int(tile[1])

    if col > cols:
        cols = col
    if row > rows:
        rows = row
    if col < cols_start:
        cols_start = col
    if row < rows_start:
        rows_start = row

    tiles[index] = [col, row]

cols += cols_start + 1
rows += rows_start + 1

# sorting by row and then col so area will always be positive
tiles.sort(key=lambda tile: (tile[1], tile[0]))

if debug:
    print("Input grid:")
    for row in range(rows):
        for col in range(cols):
            if [col, row] in tiles:
                print('#', end='')
            else:
                print('.', end='')
        print()

answer_tiles = []
for index, first in enumerate(tiles):
    for second in tiles[(index + 1):]:
        area = calc_area(first, second)
        if area > answer:
            answer = area
            answer_tiles = [first, second]

if debug:
    print("\nAnswer grid:")
    for row in range(rows):
        for col in range(cols):
            if row in range(answer_tiles[0][1], answer_tiles[1][1]) and col in range(answer_tiles[0][0], answer_tiles[1][0]):
                print('0', end='')
            elif [col, row] in tiles:
                print('#', end='')
            else:
                print('.', end='')
        print()

print(f"\nAnswer: {answer}")
