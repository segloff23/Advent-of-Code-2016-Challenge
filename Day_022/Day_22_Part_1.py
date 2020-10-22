

from re import findall;

with open('Day_22_Input.txt') as file:
    
    pattern = 'x\d+|y\d+|\d+T|\d+%';
    node_data = {};
    for line in file:
        data = findall(pattern, line.strip());
        if len(data) != 0:
            coordinate = int(data[0][1:]) + 1j*int(data[1][1:]);
            size = int(data[2][:-1]);
            used = int(data[3][:-1]);
            available = int(data[4][:-1]);
            used_percent = int(data[5][:-1]);
            node_data[coordinate] = [size, used, available, used_percent];

viable_pairs = 0;
for keyA in node_data:
    pair_found = 0;
    for keyB in node_data:
        if keyA != keyB:
            if node_data[keyA][1] != 0:
                if node_data[keyA][1] <= node_data[keyB][2]:
                    viable_pairs += 1;
                    pair_found = 1;
print('\nPart 1:');
print('Viable Pairs: ', viable_pairs);