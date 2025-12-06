answer = 0

debug = False

numbers = []
operators = []

with open('input.txt', 'r') as input:
    lines = [line.strip().split() for line in input.readlines()]

    for line in lines[:-1]:
        numbers.append([int(num) for num in line])
    operators = lines[-1]

if debug:
    print(f"Numbers: {numbers}\n")
    print(f"Operators: {operators}\n")

for index, operator in enumerate(operators):
    if operator == '*':
        product = 1
        for line in numbers:
            product *= line[index]
        answer += product

    elif operator == '+':
        sum = 0
        for line in numbers:
            sum += line[index]
        answer += sum

print(answer)
