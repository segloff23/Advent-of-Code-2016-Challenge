

from re import findall;

with open('Day_22_Input.txt') as file:
    
    pattern = 'x\d+|y\d+|\d+T|\d+%';
    grid = [[0 for j in range(33)] for i in range(30)];
    for line in file:
        data = findall(pattern, line.strip());
        if len(data) != 0:
            
            x = int(data[0][1:]);
            y = int(data[1][1:]);
            
            size = int(data[2][:-1]);
            used = int(data[3][:-1]);
            available = int(data[4][:-1]);

            grid[y][x] = [size, used, available];
            if used == 0:
                print((x, y));

for y in range(30):
    for x in range(33):
        if (x == 0) and (y == 0):
            print('(.)', end = '');
        elif (x == 32) and (y == 0):
            print(' G ', end = '');
        elif grid[y][x][1] == 0:
            print('---', end = '');
        else:
            pair_found = 0;
            for y2 in range(30):
                for x2 in range(33):
                    if grid[y2][x2][2] >= grid[y][x][1]:
                        pair_found = 1;
            if pair_found:
                print(' . ', end = '');
            else:
                print(' # ', end = '');
    print();

# 70 to move empty space next to goal data
# 155? to move to 0,0