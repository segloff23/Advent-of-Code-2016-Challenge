import hashlib;

def check_doors(route, seed):
    
    message = seed + route;
    result = hashlib.md5(message.encode()).hexdigest();
    
    door_states = [];
    for i in range(4):
        if ord(result[i]) <= ord('a'):
            door_states.append(0);
        else:
            door_states.append(1);
    
    return door_states;

def check_position(position, map_size):
    return (position.real < map_size[0]) and (position.real >= 0) and (position.imag < map_size[1]) and (position.imag >= 0);

seed = 'veumntbg';
max_path_length = 1000;
destination = 3+3j;
map_size = (4, 4);
direction_letters = 'UDLR';
direction_steps = [-1j, 1j, -1, 1];

paths = [['', 0+0j]];
last_valid_path = '';
for i in range(max_path_length):
    new_paths = [];
    for route in paths:
        door_states = check_doors(route[0], seed);
        for i in range(4):
            if door_states[i]:
                new_position = route[1] + direction_steps[i];
                if check_position(new_position, map_size):
                    if new_position != destination:
                        new_paths.append([route[0] + direction_letters[i], new_position]);
                    else:
                        last_valid_path = route[0] + direction_letters[i];
    
    if len(new_paths) == 0:
        break;
    else:
        paths = new_paths.copy();

print('\nPart 2:');
print('Last Valid Path Length: ', len(last_valid_path));































