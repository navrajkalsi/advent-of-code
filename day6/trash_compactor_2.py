answer = 0

debug = False

numbers = []
operators = ""

with open('input.txt', 'r') as input:
    lines = [line.replace('\n', '') for line in input.readlines()]

    numbers.extend(lines[:-1])
    operators = lines[-1]

if debug:
    print("Numbers:")
    for num in numbers:
        print(num)
    print(f"\nOperators:\n{operators}\n")

empty_cols = [] # space col indices between problems
for index in range(len(operators)):
    operator = operators[index]
    if (operator == '*' or operator == '+') and index != 0:
        empty_cols.append(index - 1)

longest_line = len(max(numbers, key=len))

operator = operators[0]
sub_answer = 0 if operator == '+' else 1
for index in range(longest_line + 1):
    if index in empty_cols:
        answer += sub_answer
        operator = operators[index + 1]
        sub_answer = 0 if operator == '+' else 1
        continue
    if index == longest_line:
        answer += sub_answer
        break

    num = ""
    for line in numbers:
        if len(line) <= index:
            continue
        num += line[index]
    num = int(num)
    if operator == '*':
        sub_answer *= num
    elif operator == '+':
        sub_answer += num

print(answer)
