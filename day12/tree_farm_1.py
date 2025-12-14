answer = 0

debug = True

SHAPE_SIZE = 3

shapes = []
shape_variations = [] # list of list of various shape possibilities
regions = [] # list of dicts

def get_empty_shape():
    return ['.' * SHAPE_SIZE] * SHAPE_SIZE

def replace_at(string, index, char):
    return string[:index] + char + string[(index + 1):]

def rotate(shape):
    # rotate 90
    new = get_empty_shape()
    for i in range(SHAPE_SIZE):
        for j in range(SHAPE_SIZE):
            new[i] = replace_at(new[i], j, shape[SHAPE_SIZE - j - 1][i])

    return new

def flip(shape):
    return [line[::-1] for line in shape]

def get_variations(shape):
    variations = [shape]
    
    if debug:
        print('\n\nOriginal orientation:')
        for line in shape:
            print(line)

    # rotating
    for num in range(3):
        variations.append(rotate(variations[-1]))
        if debug:
            print(f'\nRotating {(num + 1) * 90} degrees:')
            for line in variations[-1]:
                print(line)

    # flip
    variations.append(flip(shape))
    if debug:
        print('\nFlipped original orientation:')
        for line in variations[-1]:
            print(line)

    # rotate flipped
    for num in range(3):
        variations.append(rotate(variations[-1]))
        if debug:
            print(f'\nRotating flipped {(num + 1) * 90} degrees:')
            for line in variations[-1]:
                print(line)

    return variations

with open('demo.txt', 'r') as input:
    lines = [line.strip() for line in input.readlines()]
    for index, line in enumerate(lines):
        if line == '':
            continue

        if ':' in line and 'x' not in line:
            index += 1
            shapes.append(lines[index: (index + SHAPE_SIZE)])

        if 'x' in line:
            section = line.split('x')
            cols = int(section[0])
            
            section = section[1].split(': ')
            rows = int(section[0])

            presents = [int(p) for p in section[1].split()]
            regions.append({'cols': cols, 'rows': rows, 'presents': presents})
        
if debug:
    print('Input shapes:')
    for shape in shapes:
        print(shape)
    print(f'\nInput regions:')
    for region in regions:
        print(region)

for shape in shapes:
    shape_variations.append(get_variations(shape))

for var in shape_variations:
    print(var)

print(f'\nAnswer: {answer}')
