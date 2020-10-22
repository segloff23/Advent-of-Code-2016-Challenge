
import re;


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

    
instructions = read_instructions('Day_1_Input.txt');

coord = 0+0j;
direction = 1j;
for turn, steps in instructions:
    
    direction = change_direction(direction, turn);
    coord += direction * steps;
 
print('\nPart 1:');
print(int(abs(coord.real) + abs(coord.imag)));