
def create_neighbor(current, moved_chip_gen_pair, direction, num_to_move, chip_or_gen_or_both):
    
    neighbor = [];
    neighbor.append(current[0] + direction);
    
    if chip_or_gen_or_both == 2: # chip/gen pair is being moved
        moved_so_far = 0;
        for chip_gen_pair in current[1:]:
            if (chip_gen_pair == moved_chip_gen_pair) and (moved_so_far != num_to_move):
                new_chip_gen_pair = (chip_gen_pair[0] + direction, chip_gen_pair[1] + direction, chip_gen_pair[2]);
                neighbor.append(new_chip_gen_pair);
                moved_so_far += 2;
            else:
                neighbor.append(chip_gen_pair);
    elif chip_or_gen_or_both == 1: # gen is being moved
        moved_so_far = 0;
        for chip_gen_pair in current[1:]:
            if (chip_gen_pair in moved_chip_gen_pair) and (moved_so_far != num_to_move):
                new_chip_gen_pair = (chip_gen_pair[0], chip_gen_pair[1] + direction, chip_gen_pair[2]);
                neighbor.append(new_chip_gen_pair);
                moved_so_far += 1;
            else:
                neighbor.append(chip_gen_pair);
    elif chip_or_gen_or_both == 0: # chip is being moved
        moved_so_far = 0;
        for chip_gen_pair in current[1:]:
            if (chip_gen_pair in moved_chip_gen_pair) and (moved_so_far != num_to_move):
                new_chip_gen_pair = (chip_gen_pair[0] + direction, chip_gen_pair[1], chip_gen_pair[2]);
                neighbor.append(new_chip_gen_pair);
                moved_so_far += 1;
            else:
                neighbor.append(chip_gen_pair);
    #if tuple(current) == (3, (3, 3), (3, 3)):
    #   print(neighbor, moved_chip_gen_pair, direction, num_to_move, chip_or_gen_or_both);
    return tuple(neighbor);

def find_neighbors(current):
    # Get valid neighbors of a given node
    
    neighbors = [];
    elevator = current[0];
    
    chip_gen_pair_up_found = 0;
    sole_chip_up_found = 0;
    movable_sole_chip_up = [];
    sole_gen_up_found = 0;
    movable_sole_gen_up = [];
    if elevator != 4:
        for chip_gen_pair in current[1:]:
            if (chip_gen_pair[0] == chip_gen_pair[1]) and (chip_gen_pair[0] == elevator):
                valid_up = 1;
                for alt_chip_gen_pair in current[1:]:
                    if alt_chip_gen_pair[2] != chip_gen_pair[2]:
                        if (alt_chip_gen_pair[0] != alt_chip_gen_pair[1]) and (alt_chip_gen_pair[0] == elevator + 1):
                            valid_up = 0;
                            break;
                if valid_up:
                    movable_chip_gen_pair_up = chip_gen_pair;
                    chip_gen_pair_up_found = 1;
                    break;
        
        for chip_gen_pair in current[1:]:
            if chip_gen_pair[0] == elevator:
                valid_up = 1;
                for alt_chip_gen_pair in current[1:]:
                    if alt_chip_gen_pair[2] != chip_gen_pair[2]:
                        if (alt_chip_gen_pair[1] == elevator + 1) and (chip_gen_pair[1] != (elevator + 1)):
                            valid_up = 0;
                            break;
                if valid_up:
                    movable_sole_chip_up.append(chip_gen_pair);
                    sole_chip_up_found = 1;
                    
            if chip_gen_pair[1] == elevator:
                valid_up = 1;
                for alt_chip_gen_pair in current[1:]:
                    if alt_chip_gen_pair[2] != chip_gen_pair[2]:
                        if (alt_chip_gen_pair[0] == elevator + 1) and (alt_chip_gen_pair[1] != (elevator + 1)):
                            valid_up = 0;
                            break;
                if valid_up:
                    movable_sole_gen_up.append(chip_gen_pair);
                    sole_gen_up_found = 1;

    chip_gen_pair_down_found = 0;
    sole_chip_down_found = 0;
    movable_sole_chip_down = [];
    sole_gen_down_found = 0;
    movable_sole_gen_down = [];
    if elevator != 1:
        for chip_gen_pair in current[1:]:
            if chip_gen_pair[0] == elevator:
                valid_down = 1;
                for alt_chip_gen_pair in current[1:]:
                    if alt_chip_gen_pair[2] != chip_gen_pair[2]:
                        if (alt_chip_gen_pair[1] == elevator - 1) and (chip_gen_pair[1] != (elevator - 1)):
                            valid_down = 0;
                            break;
                if valid_down:
                    movable_sole_chip_down.append(chip_gen_pair);
                    sole_chip_down_found = 1;
                    break;
                    
            if chip_gen_pair[1] == elevator:
                valid_down = 1;
                for alt_chip_gen_pair in current[1:]:
                    if alt_chip_gen_pair[2] != chip_gen_pair[2]:
                        if (alt_chip_gen_pair[0] == elevator - 1) and (alt_chip_gen_pair[1] != (elevator - 1)):
                            valid_down = 0;
                            break;
                if valid_down:
                    movable_sole_gen_down.append(chip_gen_pair);
                    sole_gen_down_found = 1;
                    break;
                    
        if (not sole_chip_down_found) and (not sole_gen_down_found):
            for chip_gen_pair in current[1:]:
                if (chip_gen_pair[0] == chip_gen_pair[1]) and (chip_gen_pair[0] == elevator):
                    valid_down = 1;
                    for alt_chip_gen_pair in current[1:]:
                        if alt_chip_gen_pair[2] != chip_gen_pair[2]:
                            if (alt_chip_gen_pair[0] != alt_chip_gen_pair[1]) and (alt_chip_gen_pair[0] == elevator - 1):
                                valid_down = 0;
                                break;
                    if valid_down:
                        movable_chip_gen_pair_down = chip_gen_pair;
                        chip_gen_pair_down_found = 1
                        break;

    if (len(movable_sole_gen_up) < 2) or (len(movable_sole_gen_down) < 2):
        for chip_gen_pair in current[1:]:
            if chip_gen_pair[1] == elevator:
                for chip_gen_pair_2 in current[1:]:
                    if (chip_gen_pair_2[1] == elevator) and (chip_gen_pair_2 != chip_gen_pair):
                        valid_up = 1;
                        valid_down = 1;
                        for alt_chip_gen_pair in current[1:]:
                            if (alt_chip_gen_pair[2] != chip_gen_pair[2]) and (alt_chip_gen_pair[2] != chip_gen_pair_2[2]):
                                if (alt_chip_gen_pair[0] == elevator + 1) and (alt_chip_gen_pair[1] != (elevator + 1)):
                                    valid_up = 0;
                                if (alt_chip_gen_pair[0] == elevator - 1) and (alt_chip_gen_pair[1] != (elevator - 1)):
                                    valid_down = 0;
                                if (not valid_up) and (not valid_down):
                                    break;
                        if valid_up and (chip_gen_pair[1] != 4):
                            movable_sole_gen_up = [chip_gen_pair, chip_gen_pair_2];
                            sole_gen_up_found = 1;
                        if valid_down and (chip_gen_pair[1] != 1):
                            movable_sole_gen_down = [chip_gen_pair, chip_gen_pair_2];
                            sole_gen_down_found = 1;
    
    pair_up_found = (chip_gen_pair_up_found) or (len(movable_sole_chip_up) >= 2) or (len(movable_sole_gen_up) >= 2);
    single_up_found = sole_gen_up_found or sole_chip_up_found
    if pair_up_found:
        if chip_gen_pair_up_found:
            neighbors.append(create_neighbor(current, movable_chip_gen_pair_up, 1, 2, 2));
        if len(movable_sole_chip_up) >= 2:
            neighbors.append(create_neighbor(current, movable_sole_chip_up, 1, 2, 0));
        if len(movable_sole_gen_up) >= 2:
            neighbors.append(create_neighbor(current, movable_sole_gen_up, 1, 2, 1)); 
    elif single_up_found:
        if sole_chip_up_found:
            neighbors.append(create_neighbor(current, movable_sole_chip_up, 1, 1, 0));
        if sole_gen_up_found:
            neighbors.append(create_neighbor(current, movable_sole_gen_up, 1, 1, 1)); 
    
    single_down_found = (sole_chip_down_found) or (sole_gen_down_found);
    pair_down_found = (chip_gen_pair_down_found) or (len(movable_sole_chip_down) >= 2) or (len(movable_sole_gen_down) >= 2);
    if single_down_found:
        if sole_chip_down_found:
            neighbors.append(create_neighbor(current, movable_sole_chip_down, -1, 1, 0));
        if sole_gen_down_found:
            neighbors.append(create_neighbor(current, movable_sole_gen_down, -1, 1, 1));
    elif pair_down_found:
        if chip_gen_pair_down_found:
            neighbors.append(create_neighbor(current, movable_chip_gen_pair_down, -1, 2, 2));
        if len(movable_sole_gen_down) >= 2:
            neighbors.append(create_neighbor(current, movable_sole_gen_down, -1, 2, 1)); 
    
    return neighbors;

def h(node):
    # h is the heuristic function. h(n) estimates the cost to reach goal from node n.     
    heuristic = -9;
    for chip_gen_pair in node[1:]:
        for element in chip_gen_pair:
            heuristic += 2 * (4 - element);   
    return heuristic;

def reconstruct_path(cameFrom, current):
    total_path = [current];
    while current in cameFrom:
        current = cameFrom[current];
        total_path.insert(0, current);
    return total_path

def smallify(node):
    new_node = [];
    
    for element in node[1:]:
        new_node.append((element[0], element[1]));
    new_node.sort(key = lambda x: x[0]);
    new_node.insert(0, node[0]);
    
    return tuple(new_node);

# A* finds a path from start to goal.
def A_Star(start, goal):
    # The set of discovered nodes that may need to be (re-)expanded.
    # Initially, only the start node is known.
    openSet = [start];
    openSetSmall = [smallify(start)];
    nodes_explored = 1;
    # For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start to n currently known.
    cameFrom = {};
    
    # For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    gScore = {};
    gScore[start] = 0;

    # For node n, fScore[n] := gScore[n] + h(n).
    fScore = {};
    fScore[start] = h(start);

    while len(openSet) != 0:
        current_fScore = 1000000;
        for key in openSet:
            if fScore[key] < current_fScore:
                current = key;
                current_fScore = fScore[key];
        if current == goal:
            return gScore[current], nodes_explored, reconstruct_path(cameFrom, current);

        openSet.pop(openSet.index(current));
        neighbor_of_current = find_neighbors(current);
        for neighbor in neighbor_of_current:
            # tentative_gScore is the distance from start to the neighbor through current
            tentative_gScore = gScore[current] + 1;
            if tentative_gScore < gScore.setdefault(neighbor, 1000000):
                # This path to neighbor is better than any previous one. Record it!
                cameFrom[neighbor] = current;
                gScore[neighbor] = tentative_gScore;
                fScore[neighbor] = gScore[neighbor] + h(neighbor);
                if smallify(neighbor) not in openSetSmall:
                    openSet.append(neighbor);
                    openSetSmall.append(smallify(neighbor));
                    nodes_explored += 1;

    # Open set is empty but goal was never reached
    return 0;

# (elevator floor, (chip floor, generator floor), ...);
start = (1, (2, 1, 1), (1, 1, 2), (2, 1, 3), (1, 1, 4), (1, 1, 5));
goal = (4, (4, 4, 1), (4, 4, 2), (4, 4, 3), (4, 4, 4), (4, 4, 5))

distance, space, path = A_Star(start, goal);
print('\nPart 1:');
print(distance);
print(space);
    
    
start = (1, (2, 1, 1), (1, 1, 2), (2, 1, 3), (1, 1, 4), (1, 1, 5), (1, 1, 6), (1, 1, 7));
goal = (4, (4, 4, 1), (4, 4, 2), (4, 4, 3), (4, 4, 4), (4, 4, 5), (4, 4, 6), (4, 4, 7));

distance, space, path = A_Star(start, goal);
print('\nPart 2:');
print(distance);
print(space);




