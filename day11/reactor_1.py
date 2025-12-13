answer = 0

debug = True

devices = []
start = -1

def get_device_index(name):
    for index, device in enumerate(devices):
        if device['device'] == name:
            return index

def follow_device(name, path):
    path.append(name)

    if name == 'out':
        global answer
        answer += 1
        if debug: 
            print(f'\nFound `out`, followed path of lenght {len(path)}:')
            for step in path:
                print(step)
        return

    if name == 'you': # loop
        return

    index = get_device_index(name)
    for output in devices[index]['outputs']:
        follow_device(output, path)

with open('input.txt', 'r') as input:
    devices = [line.strip() for line in input.readlines()]
    for index, device in enumerate(devices):
        device = device.split(': ')
        devices[index] = {'device': device[0], 'outputs': device[1].split()}
        if devices[index]['device'] == 'you':
            start = index

assert start != -1
        
if debug:
    print('Input devices:')
    for device in devices:
        print(device)
    print(f'\nStart index: {start}')

path = ['you']
for output in devices[start]['outputs']:
    follow_device(output, path)

print(f'\nAnswer: {answer}')
