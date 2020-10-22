

with open('Day_18_Input.txt') as file:
    first_row_string = '.' + file.readline().strip() + '.';

safe_tiles = -2;
first_row = [];
for character in first_row_string:
    if character == '.':
        first_row.append(0);
        safe_tiles += 1;
    else:
        first_row.append(1);

row_length = len(first_row);
base_row = [0 for i in range(row_length)];
total_rows = 400000;
last_row = first_row;

new_row = base_row.copy();
for i in range(total_rows - 1):
    for j in range(1, row_length-1):
        new_row[j] = last_row[j-1] ^ last_row[j+1];
        safe_tiles += new_row[j];
    last_row = new_row;

print(safe_tiles);