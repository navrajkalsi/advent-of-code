import itertools

answer = 0

debug = False

machines = []
indicators = []
button_wirings = []
joltages = []

def simplify_wirings(button_wirings, index): # remove any wiring that has any num more than index
    final = []
    for button_wiring in button_wirings:
        if max(button_wiring) >= index:
            continue
        final.append(button_wiring)

    return final

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
    levels = joltages[index]
    if debug:
        print(f'\nMachine num: {index}\nJolatge level counters: {levels}')

    # wirings = simplify_wirings(button_wirings[index], len(levels))
    wirings = button_wirings[index]
    length = len(wirings)
    buttons_requried = []
    for index, level in enumerate(levels):
        buttons_requried.extend([index for i in range(level)])

    button_presses = 1
    while True:
        print(button_presses)
        found = False
        for combinations in list(itertools.combinations_with_replacement(wirings, button_presses)):
            single = []
            for combination in combinations:
                single.extend(combination)
            if sorted(single) == buttons_requried:
                found = True
                break
        if found:
            if debug:
                print(f'Found button for joltage levels with {button_presses} button presses')
            answer += button_presses
            break
        button_presses += 1

print(f'\nAnswer: {answer}')
