import itertools

answer = 0

debug = False

machines = []
indicators = []
button_wirings = []
joltages = []

with open('demo.txt', 'r') as input:
    machines = [line.strip() for line in input.readlines()]

for machine in machines:
    sections = machine.split(' ')
    indicators.append(sections[0][1:-1])

    button_wiring = sections[1:-1]
    for index, schematic in enumerate(button_wiring):
        schematic = schematic[1:-1].split(',')
        for sub_index, sub_schematic in enumerate(schematic):
            schematic[sub_index] = int(schematic[sub_index])
        button_wiring[index] = schematic
    button_wirings.append(button_wiring)

    tmp_joltages = sections[-1][1:-1].split(',')
    for index, joltage in enumerate(tmp_joltages):
        tmp_joltages[index] = int(joltage)
    joltages.append(tmp_joltages)

if debug:
    print('Input machines:')
    for machine in machines:
        print(machine)
    print('\nIndicator lights:')
    for indicator in indicators:
        print(indicator)
    print('\nButton wirings:')
    for button_wiring in button_wirings:
        print(button_wiring)
    print('\nJoltages:')
    for joltage in joltages:
        print(joltage)

for index, machine in enumerate(machines):
    lights = [index for index, char in enumerate(indicators[index]) if char == '#']
    if debug:
        print(f'\nMachine num: {index}\nButtons to press: {lights}')

    length = len(button_wirings[index])
    for i in range(length):
        buttons_pressed = length - i # continuous button press
        for j in range(0, length - buttons_pressed + 1):
            combinations = list(itertools.product(buttons_pressed, j))

print(f'\nAnswer: {answer}')
