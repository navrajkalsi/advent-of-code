import math

answer = 0

debug = True

lines = []
circuits = []

def get_distance(first, second):
    return math.sqrt((int(second[0]) - int(first[0])) ** 2 + (int(second[1]) - int(first[1])) ** 2 +
                     (int(second[2]) - int(first[2])) ** 2)

with open('demo.txt', 'r') as input:
    lines = [line.strip().split(',') for line in input.readlines()]

if debug:
    print("Junction Boxes:")
    for line in lines:
        print(line)

shortest_len = -1
shortest_boxes = []

for first in lines:
    for second in lines:
        if first == second:
            continue
        dist = get_distance(first, second)
        if shortest_len == -1 or dist < shortest_len:
            shortest_len = dist
            shortest_boxes = [first, second]

print(shortest_boxes)
print(answer)
