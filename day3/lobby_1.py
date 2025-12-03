answer = 0
banks = []

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
    largest = [0, 0] # 2 largest nums
    largest_index = [-1, -1]

    for index, battery in enumerate(bank): # first largest
        battery = int(battery)
        if battery > largest[0]:
            largest[0] = battery
            largest_index[0] = index

    if debug:
        print(f"First largest: {largest[0]} at index: {largest_index[0]}")

    if largest_index[0] + 1 == len(bank): # if largest at the end, loop again
        org_largest = largest[0]
        largest[0] = 0
        for index, battery in enumerate(bank): # first largest
            battery = int(battery)
            if battery > largest[0] and battery != org_largest:
                largest[0] = battery
                largest_index[0] = index
        if debug:
            print(f"New first largest: {largest[0]} at index: {largest_index[0]}")


    for index, battery in enumerate(bank[largest_index[0] + 1:]): # first largest
        battery = int(battery)
        if battery > largest[1]:
            largest[1] = battery
            largest_index[1] = index

    if debug:
        print(f"Second largest: {largest[1]} at index: {largest_index[1]}")

    joltage = str(largest[0]) + str(largest[1])
    if debug:
        print(f"Joltage: {joltage}")

    answer += int(joltage)

print(answer)
