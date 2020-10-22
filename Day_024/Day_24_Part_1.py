

from itertools import permutations;

def check_wall(x, y, grid):   
    if grid[y][x] == '#':
        wall_found = 1;
    else:
        wall_found = 0;
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

def get_node_distance(i_node, d_node, map_size, grid):

    distances = [[-1 for j in range(map_size[0])] for i in range(map_size[1])];
    states = [[0 for j in range(map_size[0])] for i in range(map_size[1])];
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
            
            #if check_node(n_node, map_size):
            if states[n_node[1]][n_node[0]] == 0:
                wall_found = check_wall(n_node[0], n_node[1], grid);
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
    
    return distances[d_node[1]][d_node[0]];

with open('Day_24_Input.txt') as file:
    hvac_points = [];
    grid = [];
    row_count = 0;
    for line in file:
        col_count = 0;
        for symbol in line.strip():
            try:
                hvac_id = int(symbol);
                coord = [col_count, row_count];
                hvac_points.append([hvac_id, coord])
            except:
                None;
            print(symbol, end = '');
            col_count += 1;   
        print();
        grid.append(line.strip());
        row_count += 1;
        
hvac_points.sort(key = lambda x: x[0]) 
for i in hvac_points:
    print(i);
print();

hvac_grid = [[0 for j in hvac_points] for i in hvac_points];
for i in range(len(hvac_points)):
    for j in range(i+1, len(hvac_points)):
        hvac_grid[i][j] = get_node_distance(hvac_points[i][1], hvac_points[j][1], (col_count, row_count), grid);
        hvac_grid[j][i] = hvac_grid[i][j];

for line in hvac_grid:
    print(line);

routes = list(permutations(range(1,len(hvac_points))));

min_distance = -1;
for path in routes:
    distance = 0;
    last_point = 0;
    for i in path:
        distance += hvac_grid[i][last_point];
        last_point = i;
    
    min_distance, arg = effective_min(min_distance, distance);
    if arg == 1:
        best_path = path;
        
print(min_distance);
print(best_path);





