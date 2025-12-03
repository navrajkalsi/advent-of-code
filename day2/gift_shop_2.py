answer = 0
input_arr = []

debug = False

with open('input.txt', 'r') as input:
    input_arr = input.readline().strip().split(',') # list of ranges

rngs = []

for index, value in enumerate(input_arr): # each range will now be a list of min and max
    splt = value.split('-')
    rng = [int(splt[0]), int(splt[1])]
    rngs.append(rng)

for rng in rngs:
    if debug:
        print(f"Processing range: {rng}")

    for id in range(rng[0], rng[1] + 1):
        id_str = str(id)
        factors = [] # factors for len of id_str

        for factor in range(1, len(id_str)): # exclude the number itself from factors
            if len(id_str) % factor == 0:
                factors.append(factor)

        for factor in factors:
            match = True
            for seg in range(0, len(id_str), factor):

                if debug:
                    print(f"ID: {id}, First segment: {id_str[:factor]}, Match segment: {id_str[seg:seg+factor]}\n")

                if id_str[:factor] != id_str[seg:seg+factor]: # comparing new seg to first seg
                    match = False
                    break
            if match == True:
                answer += id
                break

print(answer)
