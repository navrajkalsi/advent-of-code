answer = 0

debug = True

devices = []
start = -1

def get_device_index(name):
    for index, device in enumerate(devices):
        if device['device'] == name:
            return index

def follow_device(name, state):
    # does not create a new copy of vars
    new_state = {'dac': state['dac'], 'fft': state['fft'], 'path': [x for x in state['path']]}
    new_state['path'].append(name)

    if name == 'dac':
        new_state['dac'] = True
    elif name == 'fft':
        new_state['fft'] = True
    elif name == 'out':
        if new_state['dac'] and new_state['fft']:
            global answer
            answer += 1
            if debug: 
                path = new_state['path']
                print(f'\nFound `out`, followed path of lenght {len(path)}:')
                for step in path:
                    print(step, end=' ')
                print()
        else:
            if debug:
                print('\nFound `out`, without `dac` or `fft`')
        return
    elif name in state['path']: # loop
        return

    index = get_device_index(name)
    for output in devices[index]['outputs']:
        follow_device(output, new_state)

with open('input.txt', 'r') as input:
    devices = [line.strip() for line in input.readlines()]
    # devices = devices[:100]
    for index, device in enumerate(devices):
        device = device.split(': ')
        devices[index] = {'device': device[0], 'outputs': device[1].split()}
        if devices[index]['device'] == 'svr':
            start = index

assert start != -1
        
if debug:
    print('Input devices:')
    for device in devices:
        print(device)
    print(f'\nStart index: {start}')

state = {'dac': False, 'fft': False, 'path': ['svr']}
for output in devices[start]['outputs']:
    follow_device(output, state)

print(f'\nAnswer: {answer}')
