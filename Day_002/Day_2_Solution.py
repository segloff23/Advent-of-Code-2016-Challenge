def read_instructions(file_name):
    with open(file_name) as file:
        instructions = [line.strip() for line in file];
    return instructions;

def check_valid_move(new_position, part):
    if part == 1:
        valid = 0;
        if (new_position.real > -1) and (new_position.imag > -1):
            if (new_position.real < 3) and (new_position.imag < 3):
                valid = 1;
    elif part == 2:
        valid = 0;
        if (abs(new_position.real) + abs(new_position.imag)) < 3:
            valid = 1;
    return valid;

def get_code(instructions, start, keypad, part):
    direction_lookup = {'U' : -1j, 'D' : 1j, 'R' : 1, 'L': -1};
    code_index = [];
    position = start;
    new_position = position;
    
    for line in instructions:
        for direction in line:
            new_position = position + direction_lookup[direction];
            if check_valid_move(new_position, part):
                position = new_position;
        code_index.append(position);
    code = '';
    for symbol in code_index:
        if part == 1:
            code += keypad[int(symbol.imag)][int(symbol.real)];
        elif part == 2:
            code += keypad[int(symbol.imag)+2][int(symbol.real)+2];
    return code;

keypad_1 = [['1', '2', '3'], ['4', '5', '6'], ['7', '8','9']];
keypad_2 = [('0', '0', '1', '0', '0'), ('0', '2', '3', '4', '0'), ('5', '6', '7', '8', '9'), ('', 'A', 'B', 'C', ''), ('', '', 'D', '', '')];
instructions = read_instructions('Day_2_Input.txt');

code_1 = get_code(instructions, 1+1j, keypad_1, 1);
code_2 = get_code(instructions, 0+0j, keypad_2, 2);

print('\nPart 1:');
print(code_1);
print('\nPart 2:');
print(code_2);