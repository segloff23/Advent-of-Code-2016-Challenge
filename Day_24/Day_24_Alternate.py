from itertools import permutations;

def reconstruct_path(cameFrom, current):
    total_path = [current];
    while current in cameFrom:
        current = cameFrom[current];
        total_path.insert(0, current);
    return total_path

def h(node, goal):
    # h is the heuristic function. h(n) estimates the cost to reach goal from node n.  
    heuristic = abs(node.real - goal.real) + abs(node.imag - goal.imag);
    return heuristic;

def find_neighbors(current, grid):
    # Get valid neighbors of a given node
    neighbors = [];
    options = [1, -1, 1j, -1j];
    for move in options:
        new_node = current + move;
        if grid[int(new_node.imag)][int(new_node.real)] != '#':
            neighbors.append(new_node);
    return neighbors;

def d(current, neighbor):
    # d(current,neighbor) is the weight of the edge from current to neighbor
    distance = 1;
    return distance;

# A* finds a path from start to goal.
def A_Star(start, goal, grid):
    # The set of discovered nodes that may need to be (re-)expanded.
    # Initially, only the start node is known.
    openSet = [start];

    # For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start to n currently known.
    #cameFrom = {};

    # For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    gScore = {};
    gScore[start] = 0;

    # For node n, fScore[n] := gScore[n] + h(n).
    fScore = {};
    fScore[start] = h(start, goal);

    while len(openSet) != 0:
        current_fScore = 1000000;
        for key in openSet:
            if fScore[key] < current_fScore:
                current = key;
                current_fScore = fScore[key];
        if current == goal:
            return gScore[current] # reconstruct_path(cameFrom, current);

        openSet.pop(openSet.index(current));
        
        neighbor_of_current = find_neighbors(current, grid);
        for neighbor in neighbor_of_current:
            # tentative_gScore is the distance from start to the neighbor through current
            tentative_gScore = gScore[current] + 1; # + d(current, neighbor);
            if tentative_gScore < gScore.setdefault(neighbor, 1000000):
                # This path to neighbor is better than any previous one. Record it!
                #cameFrom[neighbor] = current;
                gScore[neighbor] = tentative_gScore;
                fScore[neighbor] = gScore[neighbor] + h(neighbor, goal);
                if neighbor not in openSet:
                    openSet.append(neighbor);

    # Open set is empty but goal was never reached
    return 0;

with open('Day_24_Input.txt') as file:
    hvac_points = [];
    grid = [];
    row_count = 0;
    for line in file:
        col_count = 0;
        for symbol in line.strip():
            try:
                hvac_id = int(symbol);
                coord = col_count + 1j * row_count;
                hvac_points.append([hvac_id, coord])
            except:
                None;
            col_count += 1;   
        grid.append(line.strip());
        row_count += 1;
        
hvac_points.sort(key = lambda x: x[0]);
num_points = len(hvac_points);
hvac_grid = [[0 for j in hvac_points] for i in hvac_points];
for i in range(len(hvac_points)):
    for j in range(i+1, len(hvac_points)):
        hvac_grid[i][j] = A_Star(hvac_points[i][1], hvac_points[j][1], grid);
        hvac_grid[j][i] = hvac_grid[i][j];
        
routes = list(permutations(range(1,len(hvac_points))));
min_distance_reg = 1000000;
min_distance_loop = 1000000;
for path in routes:
    distance = 0;
    last_point = 0;
    for i in path:
        distance += hvac_grid[i][last_point];
        last_point = i;
    
    if distance < min_distance_reg:
        best_path_reg = path;
        min_distance_reg = distance;
    if (distance + hvac_grid[0][last_point]) < min_distance_loop:
        best_path_loop = path;
        min_distance_loop = distance + hvac_grid[0][last_point];

print('\nPart 1:');
print(min_distance_reg);
print('\nPart 2:');
print(min_distance_loop);












