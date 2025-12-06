answer = 0

debug = False

numbers = []
operators = []

with open('input.txt', 'r') as input:
    lines = [line.strip().split() for line in input.readlines()]

    numbers.extend(lines[:-1])
    operators = lines[-1]

if debug:
    print(f"Numbers: {numbers}\n")
    print(f"Operators: {operators}\n")

for index, operator in enumerate(operators):
    if operator == '*':
        product = 1
        max_len = 0

        for line in numbers: # calculate max len
            if max_len < len(line[index]):
                max_len = len(line[index])

        for place in range(max_len): # nums will be inverted
            num = ""
            for line in numbers: # performing operation
                line = [num[::-1] for num in line]
                if len(line[index]) < place + 1:
                    continue
                num += line[index][place]
            product *= int(num)
        print(product)
        answer += product

    elif operator == '+':
        sum = 0
        max_len = 0

        for line in numbers:
            if max_len < len(line[index]):
                max_len = len(line[index])

        for place in range(max_len - 1, -1, -1):
            num = ""
            for line in numbers:
                if len(line[index]) < place + 1:
                    continue
                num += line[index][place]
            sum += int(num)
        print(sum)
        answer += sum

print(answer)
