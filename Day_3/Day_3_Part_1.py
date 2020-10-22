

with open('Day_3_Input.txt') as file:
    triangles = [line.strip().split() for line in file];

pairings = [[0, 1, 2], [0, 2, 1], [1, 2, 0]];
num_possible = 0;
for side_labels in triangles:
    sides = [int(x) for x in side_labels];
    valid = 1;
    for i in pairings:
        if (sides[i[0]] + sides[i[1]]) <= sides[i[2]]:
            valid = 0;
            break;
    num_possible += valid

print('Part 1:');
print('Possible Triangles: ', num_possible);