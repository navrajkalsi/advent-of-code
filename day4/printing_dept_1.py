answer = 0
max_rolls = 3
adjacent_pos = 8
input_grid = []
answer_grid = []

def print_grid(grid):
    for line in grid:
        print(line)

def accessible(row_num, col_num):
    adjacent_rolls = 0
    for row in range(-1, 2):
        if row_num + row < 0 or row_num + row > len(input_grid):
            continue
        for col in range(-1, 2):
            if col_num + col < 0 or col_num + col > len(input_grid[0]):
                continue

with open('demo.txt', 'r') as input:
    for line in input:
        input_grid.append(input.readline().strip())

for row_num, rolls in enumerate(input_grid):
    for col_num, roll in enumerate(rolls):
        print(f"row_num: {row_num}, col_num: {col_num}, roll: {roll}")

print_grid(input_grid)
