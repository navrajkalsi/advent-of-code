min = 0
max = 99
index = 50
answer = 0

with open('input.txt', 'r') as input:

    for line in input.readlines():
        line = line.strip()

        # move = 0 - int(line[1:]) if line[0] == 'L' else int(line[1:])

        # new_index = index + move

        # if new_index in range(min, max+ 1):
        #     if new_index == 0:
        #         answer+= 1

        # elif new_index > max:
        #     increment = False if index == 0 else True
        #     while new_index > max:
        #         answer += 1 if increment == True else 0
        #         increment = True
        #         overflow = new_index - max
        #         new_index = min + overflow - 1

        # elif new_index < min:
        #     increment = False if index == 0 else True
        #     while new_index < min:
        #         answer += 1 if increment == True else 0
        #         increment = True
        #         overflow = min - new_index
        #         new_index = max - overflow + 1

        # print(f"Line: {line}, Index: {index}, New Index: {new_index}, Answer: {answer}")

        # index = new_index

        for i in range(0, int(line[1:])):
            index = index + 1 if line[0] == 'R' else index - 1

            if index == max + 1:
                index = min
            elif index == min - 1:
                index = max

            if index == 0:
                answer += 1


print(answer)
