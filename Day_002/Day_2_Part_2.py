

def read_instructions(file_name):
    with open(file_name) as file:
        instructions = [line.strip() for line in file];
    return instructions;

direction_lookup = {'U' : -1j, 'D' : 1j, 'R' : 1, 'L': -1};
keypad = [(0, 0, 1, 0, 0), (0, 2, 3, 4, 0), (5, 6, 7, 8, 9), ('', 'A', 'B', 'C', ''), ('', '', 'D', '', '')];
instructions = read_instructions('Day_2_Input.txt');

code = [];
position = 0 + 0j;
new_position = position;

for line in instructions:
    for direction in line:
        new_position = position + direction_lookup[direction];
        if (abs(new_position.real) + abs(new_position.imag)) < 3:
            position = new_position;
    code.append(position);

print('\nPart 2:');
print('Bathroom Code: ', end = '');
for number in code:
    print(keypad[int(number.imag)+2][int(number.real)+2], end = '');
