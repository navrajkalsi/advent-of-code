answer = 0

debug = False

cols_start = 10
rows_start = 10
cols = 0
rows = 0
red_tiles = []
green_tiles = []
tiles = [] # list of both red and green

def calc_area(first, second):
    return (second[0] - first[0] + 1) * (second[1] - first[1] + 1)

def verify_tiles(first, second): # verify if all the tiles in the area are red or green
    for row in range(first[1], second[1] + 1):
        for col in range(first[0], second[0] + 1):
            if [col, row] not in tiles:
                return False
    return True

with open('input.txt', 'r') as input:
    red_tiles = [line.strip().split(',') for line in input.readlines()]

for index, tile in enumerate(red_tiles): # converting to ints
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

    red_tiles[index] = [col, row]

cols += cols_start + 1
rows += rows_start + 1

# sorting by row and then col
red_tiles.sort(key=lambda tile: (tile[1], tile[0]))

# red tiles
if debug:
    print("Input grid with red tiles:")
    for row in range(rows):
        for col in range(cols):
            if [col, row] in red_tiles:
                print('#', end='')
            else:
                print('.', end='')
        print()

# green tiles at periphery
for index, first in enumerate(red_tiles):
    for second in red_tiles[(index + 1):]:
        if second[0] == first[0]: # cols match
            for row in range(first[1] + 1, second[1]):
                green_tiles.append([first[0], row])
        if second[1] == first[1]: # rows match
            for col in range(first[0] + 1, second[0]):
                green_tiles.append([col, first[1]])

if debug:
    print("\nInput grid with red & green tiles, only at periphery:")
    for row in range(rows):
        for col in range(cols):
            if [col, row] in red_tiles:
                print('#', end='')
            elif [col, row] in green_tiles:
                print('X', end='')
            else:
                print('.', end='')
        print()

tiles = red_tiles + green_tiles
# sorting by row and then col, so that I always get higher col at last
tiles.sort(key=lambda tile: (tile[1], tile[0]))

# now fill green tiles where enclosed
for row in range(rows):
    row_tiles = [] # tiles on the same row, if more than 2, fill the gap between
    for tile in tiles:
        if tile[1] == row:
            row_tiles.append(tile)

    if len(row_tiles) >= 2:
        for col in range(row_tiles[0][0] + 1, row_tiles[-1][0]):
            green_tiles.append([col, row])

tiles = red_tiles + green_tiles

print("done")
exit()

# sorting by row and then col, so that area will always be positive
tiles.sort(key=lambda tile: (tile[1], tile[0]))

if debug:
    print("\nInput grid with red & green tiles, with gaps filled:")
    for row in range(rows):
        for col in range(cols):
            if [col, row] in red_tiles:
                print('#', end='')
            elif [col, row] in green_tiles:
                print('X', end='')
            else:
                print('.', end='')
        print()

answer_tiles = []
for index, first in enumerate(red_tiles):
    for second in red_tiles[(index + 1):]:
        area = calc_area(first, second)
        if area > answer:
            valid = verify_tiles(first, second)
            if valid == False:
                continue
            answer = area
            answer_tiles = [first, second]

if debug:
    print("\nAnswer grid:")
    for row in range(rows):
        for col in range(cols):
            if row in range(answer_tiles[0][1], answer_tiles[1][1] + 1) and col in range(answer_tiles[0][0], answer_tiles[1][0]):
                print('0', end='')
            elif [col, row] in tiles:
                print('#', end='')
            else:
                print('.', end='')
        print()

print(f"\nAnswer: {answer}")
