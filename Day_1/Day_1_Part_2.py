def read_instructions(file_name):
    with open(file_name) as file:
        line = file.readline().split(',');
        instructions = [];
        for piece in line:
            instructions.append((piece.strip()[0], int(piece.strip()[1:])));
    return instructions;

def change_direction(direction, turn):
    if turn == 'R':
        direction *= 1j;
    elif turn == 'L':
        direction *= -1j;
    return direction;

def check_intersection(path, coordinate):
    if coordinate not in path:
        path.append(coordinate);
        intersection_found = 0;
    else:
        intersection_found = 1;
    return intersection_found;

def hamming_distance(complex_coordinate):
    return int(abs(complex_coordinate.real) + abs(complex_coordinate.imag));

def get_solution(instructions, initial_coordinate, initial_direction):
    coordinate = initial_coordinate;
    direction = initial_direction;
    path = [coordinate];
    first_intersection = 0 + 0j;
    intersection_found = 0;
    for turn, steps in instructions:
        direction = change_direction(direction, turn);
        for i in range(steps):
            coordinate += direction;
            if not intersection_found:
                intersection_found = check_intersection(path, coordinate);
                first_intersection += intersection_found * coordinate;
    return coordinate, first_intersection;

def print_solution(coordinate, intersection):
    print('\nPart 1:');
    print('Final Distance: ', hamming_distance(coordinate));
    print('\nPart 2:');
    print('Total Distance: ', hamming_distance(intersection));
    return 0;

instructions = read_instructions('Day_1_Input.txt');
final_coordinate, first_intersection = get_solution(instructions, 0+0j, 0+1j);
print_solution(final_coordinate, first_intersection);









