min = 0
max = 99
index = 50
answer = 0

with open('demo.txt', 'r') as input:

    for line in input.readlines():
        line = line.strip()

        move = 0 - int(line[1:]) if line[0] == 'L' else int(line[1:])

        new_index = index + move

        if new_index in range(min, max+ 1):
            pass
        elif new_index > max:
            while new_index > max:
                overflow = new_index - max
                new_index = min + overflow - 1
        elif new_index < min:
            while new_index < min:
                overflow = min - new_index
                new_index = max - overflow + 1

        index = new_index
        answer += 1 if index == 0 else 0

        print(f"Line: {line}, New Index: {new_index}")

print(answer)
