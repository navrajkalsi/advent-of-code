min = 0
max = 99
index = 50
answer = 0

with open('input.txt', 'r') as input:

    for line in input.readlines():
        line = line.strip()

        move = 0 - int(line[1:]) if line[0] == 'L' else int(line[1:])

        new_index = index + move

        # if new_index > max or new_index < min:
        #     print(f"Line: {line}, Index: {index}, New Index: {new_index}, Answer: {answer}")

        if new_index in range(min, max+ 1):
            answer += 1 if new_index == 0 else 0 # increment if the new index is 0

        elif new_index > max:
            increment = False if index == 0 else True # dealt with in if
            while new_index > max:
                answer += 1 if increment == True else 0 # increment whenever there is overflow & not already at 0 and only once in every cycle
                increment = True
                overflow = new_index - max
                new_index = min + overflow - 1

        elif new_index < min:
            increment = False if index == 0 else True
            while new_index < min:
                answer += 1 if increment == True else 0
                increment = True
                overflow = min - new_index
                new_index = max - overflow + 1

        print(f"Line: {line}, Index: {index}, New Index: {new_index}, Answer: {answer}")

        index = new_index

print(answer)
