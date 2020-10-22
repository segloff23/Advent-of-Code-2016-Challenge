
import re;
import matplotlib.pyplot as plt;

def rect(grid, rows, cols):
    new_grid = grid.copy();
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = 1;
    return new_grid;
    
def rotate(grid, direction, axis, shift):
    
    new_grid = [row.copy() for row in grid];
    row_count = len(grid);
    col_count = len(grid[0]);
    if direction == 'x':
        for i in range(row_count):
            new_grid[(i+shift) % row_count][axis] = grid[i][axis];
    elif direction == 'y':
        for j in range(col_count):
            new_grid[axis][(j+shift) % col_count] = grid[axis][j];
    return new_grid;

with open('Day_8_Input.txt') as file:
    step_list = [re.findall('rect|rotate|x|y|\d+', line.strip()) for line in file];

# [rect, cols, --, rows]
# [rotate, direction, axis, --, shift]

dim = (6, 50);
#dim = (3, 7);
#step_list = [['rect', '3', 'x', '2'], ['rotate', 'x', '1', 'y', '1']];
grid = [[0 for j in range(dim[1])] for i in range(dim[0])];

for step in step_list:
    if step[0] == 'rect':
        cols = int(step[1]);
        rows = int(step[3]);
        grid = rect(grid, rows, cols);
    elif step[0] == 'rotate':
        direction = step[1];
        axis = int(step[2]);
        shift = int(step[4]);
        grid = rotate(grid, direction, axis, shift);
        
shaded_squares = sum([sum(i) for i in grid]);

print('\nPart 1:');
print('Shaded Squares: ', shaded_squares);
print('\nPart 2:');
plt.figure(figsize = (10, 10))
plt.imshow(grid, cmap = 'gray');
