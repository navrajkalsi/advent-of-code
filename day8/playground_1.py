import math

answer = 0
final_connections = 1000

debug = False

lines = []

distances = [] # list of dicts {first, second, distance}
circuits = [] # list of [junction boxes]

def get_distance(first, second):
    return math.sqrt((int(second[0]) - int(first[0])) ** 2 + (int(second[1]) - int(first[1])) ** 2 + (int(second[2]) - int(first[2])) ** 2)

def simplify_circuits():
    for box in lines:
        found = 0
        found_indices = []
        for index, circuit in enumerate(circuits):
            if box in circuit:
                found += 1
                found_indices.append(index)

        if found > 1: # combine circuits
            org_index = found_indices[0]
            org_circuit = circuits[org_index]
            for join_index in found_indices[1:]:
                join_circuit = circuits[join_index]
                join_circuit.remove(box)
                org_circuit += join_circuit
            circuits[org_index] = org_circuit
            for pop_index in found_indices[1:]:
                circuits.pop(pop_index)

with open('demo.txt', 'r') as input:
    lines = [line.strip().split(',') for line in input.readlines()]

if debug:
    print("Junction Boxes:")
    for line in lines:
        print(line)

# calculate all distances
for index, first in enumerate(lines):
    for second in lines[(index + 1):]:
        distances.append({
            "first": first,
            "second": second,
            "distance": get_distance(first, second)
            })

# sort, with shortest distances first
distances.sort(key=lambda distance: distance['distance']);

if debug:
    print("\nShortest Distances:")
    for dist in distances:
        print(dist)

connections = 0
for dist in distances:
    if connections >= final_connections:
        break
    found = False
    
    if debug:
        print("\nChecking for dist: ", dist)

    for index, circuit in enumerate(circuits):
        if debug:
            print("Checking in circuit: ", circuit)

        if dist['first'] in circuit: # first was found in a circuit, add second to that
            if debug:
                print("Found first: ", dist['first'])
            if dist['second'] in circuit:
                if debug:
                    print("Also found second: ", dist['second'])
                # connections -= 1
            else:
                circuit += [dist['second']] # append does not seem to work here, weird
                circuits[index] = circuit
                if debug:
                    print("New circuit after appending second: ", circuit)
            found = True
            break
        elif dist['second'] in circuit: # second found, add first to circuit
            if debug:
                print("Found first: ", dist['second'])
            if dist['first'] in circuit:
                if debug:
                    print("Also found first: ", dist['first'])
                # connections -= 1
            else:
                circuit += [dist['first']]
                circuits[index] = circuit
                if debug:
                    print("New circuit after appending first: ", circuit)
            found = True
            break

    if found == False: # create new circuit
        new_circuit = [dist['first'], dist['second']]
        circuits.append(new_circuit)
        if debug:
            print("No match found, new circuit: ", new_circuit)
            print("New number of circuits: ", len(circuits))

    simplify_circuits() # if a box is found to be in two different circuits, join the circuits

    connections += 1

print(f"Connections made: {connections}")

# sort to get the largest circuits first
circuits.sort(key=len, reverse=True)

answer = len(circuits[0]) * len(circuits[1]) * len(circuits[2])

if debug:
    print("\nCircuits:")
    for circuit in circuits:
        print(circuit)

print(f"Answer: {answer}")
