answer = 0
banks = []
turn_on = 12 # batteries to turn on

# looks like no battey is of 0 joltage

debug = False

with open('input.txt', 'r') as input:
    banks = input.readlines()
    for i, bank in enumerate(banks):
        banks[i] = bank.strip()

for bank in banks:
    if debug:
        print(f"Processing bank: {bank}")

    # no battery should be of zero joltage
    largest = [] # turn_on largest nums
    largest_index = []
    bank_len = len(bank)
    joltage = ""

    for i in range(turn_on):
        largest.append(0)
        largest_index.append(-1)
        lower_index = 0 if len(largest_index) == 1 else largest_index[i-1] + 1
        upper_index = bank_len - turn_on + i + 1 # max num of indices to enumerate to find the max digit
        seg = bank[lower_index:upper_index]

        if debug:
            print(f"Segment: {seg}")

        for index, battery in enumerate(seg):
            battery = int(battery)
            if battery > largest[i]:
                largest_index[i] = index + lower_index
                largest[i] = battery

        if debug:
            print(f"Largest: {largest[i]} at index: {largest_index[i]}")

        joltage += str(largest[i])

    if debug:
        print(f"Joltage: {joltage}")

    answer += int(joltage)

print(answer)
