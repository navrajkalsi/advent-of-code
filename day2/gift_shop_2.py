answer = 0
input_arr = []

with open('input.txt', 'r') as input:
    input_arr = input.readline().strip().split(',') # list of ranges

rngs = []

for index, value in enumerate(input_arr): # each range will now be a list of min and max
    splt = value.split('-')
    rng = [int(splt[0]), int(splt[1])]
    rngs.append(rng)

for rng in rngs:
    print(f"Processing range: {rng}")

    for num in range(rng[0], rng[1] + 1):
        num_str = str(num)
        num_len = len(num_str)
        if num_len % 2 == 1:
            continue

        half_len = int(num_len / 2)
        if num_str[:half_len] == num_str[half_len:]:
            answer += num

print(answer)
