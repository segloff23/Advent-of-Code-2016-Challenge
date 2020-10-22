

def check_wall(x, y, seed):
    product = (x * x) + (3 * x) + (2 * x * y) + y + (y * y) + seed;
    product_as_binary = bin(product);
    num_ones = 0;
    for bit in product_as_binary:
        if bit == '1':
            num_ones += 1;
    if (num_ones % 2) == 0:
        wall_found = 0;
    else:
        wall_found = 1;
    return wall_found;

def effective_min(a, b):
    if a == -1:
        min_val = b;
        arg = 1;
    elif b == -1:
        min_val = a;
        arg = 0;
    else:
        min_val = min([a,b]);
        arg = [a,b].index(min_val);
    return (min_val, arg);

def check_node(node, map_size):
    x = node[1];
    y = node[0];
    x_max = map_size[0];
    y_max = map_size[1];
    if (x < 0) or (y < 0) or (x >= x_max) or (y >= y_max):
        valid = 0;
    else:
        valid = 1;
    return valid;

i_node = [1, 1];
d_node = (31, 39);
map_size = (50, 50);
seed = 1364;

distances = [[-1 for j in range(map_size[0])] for i in range(map_size[1])];
states = [[0 for j in range(map_size[1])] for i in range(map_size[0])];
distances[i_node[1]][i_node[0]] = 0;
states[i_node[1]][i_node[0]] = 1;

c_node = i_node.copy();
while states[d_node[1]][d_node[0]] == 0:
    
    for i in range(4):
        n_node = c_node.copy();
        if i == 0:
            n_node[0] += 1;
        elif i == 1:
            n_node[0] -= 1;
        elif i == 2:
            n_node[1] += 1;
        elif i == 3:
            n_node[1] -= 1;
        
        if check_node(n_node, map_size):
            if states[n_node[1]][n_node[0]] == 0:
                wall_found = check_wall(n_node[0], n_node[1], seed);
                if wall_found:
                    temp_distance = -1;
                else:
                    temp_distance = distances[c_node[1]][c_node[0]] + 1;
                distances[n_node[1]][n_node[0]] = effective_min(temp_distance, distances[n_node[1]][n_node[0]])[0];
                
    
    states[c_node[1]][c_node[0]] = 1;

    min_distance = -1;
    assignment = 0;
    for x in range(map_size[0]):
        for y in range(map_size[1]):
            if states[y][x] == 0:
                temp_distance = distances[y][x];
                min_distance, arg = effective_min(temp_distance, min_distance);
                if arg == 0:
                    c_node = [x, y];
                    assignment = 1;
    if not assignment:
        break;
    
print('\nPart 1:');
print('Distance to Target: ', distances[d_node[1]][d_node[0]]);















