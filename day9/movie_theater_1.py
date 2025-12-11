answer = 0

tiles = []

def calc_area(first, second):
    return (second[0] - first[0] + 1) * (second[1] - first[1] + 1)

with open('input.txt', 'r') as input:
    tiles = [line.strip().split(',') for line in input.readlines()]

for index, tile in enumerate(tiles): # converting to ints
    tiles[index] = [int(tile[0]), int(tile[1])]

# sorting by row and then col so area will always be positive
tiles.sort(key=lambda tile: (tile[1], tile[0]))

for index, first in enumerate(tiles):
    for second in tiles[(index + 1):]:
        area = calc_area(first, second)
        if area > answer:
            answer = area

print(f"Answer: {answer}")
