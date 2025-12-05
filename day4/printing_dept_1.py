answer = 0
max_rolls = 3
adjacent_pos = 8
input_grid = []
answer_grid = []

debug = False

def print_grid(grid):
    for line in grid:
        print(line)

def accessible(row_num, col_num):
    adjacent_rolls = 0
    for row in range(-1, 2):
        if row_num + row < 0 or row_num + row >= len(input_grid):
            continue

        for col in range(-1, 2):
            if row == 0 and col == 0:
                continue
            if col_num + col < 0 or col_num + col >= len(input_grid[0]):
                continue
            if input_grid[row_num + row][col_num + col] == '@':
                adjacent_rolls += 1
            if adjacent_rolls > max_rolls:
                break

        if adjacent_rolls > max_rolls:
            break

    return adjacent_rolls <= max_rolls

with open('input.txt', 'r') as input:
    input_arr = input.readlines()
    for line in input_arr:
        input_grid.append(line.strip())

for row_num, rolls in enumerate(input_grid):
    answer_row = []
    for col_num, roll in enumerate(rolls):
        if debug:
            print(f"row_num: {row_num}, col_num: {col_num}, roll: {roll}")

        if roll != '@':
            answer_row.append(roll)
        elif accessible(row_num, col_num):
            answer += 1
            answer_row.append('X')
        else:
            answer_row.append('@')

    answer_row_str = ""
    for roll in answer_row:
        answer_row_str += roll
    answer_grid.append(answer_row_str)

    if debug:
        print(f"Answer row: {answer_row_str}")

print_grid(answer_grid)
print()
print(answer)
