import itertools

answer = 0

debug = True

machines = []
indicators = []
button_wirings = []
joltages = []

def get_lights(permut): # takes in one elm from permutation and returns what lights will be light
    last = permut[0]
    if len(permut) > 1:
        for i in range(1, len(permut)):
            last = list(set(last)^set(permut[i])) # using disjoint in sets to remove common elms
    return last

with open('input.txt', 'r') as input:
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
    buttons_pressed = 1
    while buttons_pressed < length: 
        permuts = list(itertools.permutations(button_wirings[index], buttons_pressed))
        found = False
        found_permut = []
        for permut in permuts:
            if get_lights(permut) == lights:
                found = True
                found_permut = permut
                break
        if found:
            if debug:
                print(f'Number of buttons pressed: {buttons_pressed}\nButtons pressed: {found_permut}')
            answer += buttons_pressed
            break
        buttons_pressed += 1

print(f'\nAnswer: {answer}')
