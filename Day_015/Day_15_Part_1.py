
import re;

with open('Day_15_Input.txt') as file:
    raw_data = [re.findall('\d+', line.strip()) for line in file];

posits = [];
for line in raw_data:
    posits.append([int(line[0]) + int(line[3]), int(line[1])]);

valid = 0;
time = -1;
while not valid:
    time += 1;
    valid = 1;
    for disc in posits:
        if ((disc[0] + time) % disc[1]) != 0:
            valid = 0;
            break;

print('\nPart 1:');
print('First Time: ', time);

posits.append([len(posits)+1, 11]);

valid = 0;
time = -1;
while not valid:
    time += 1;
    valid = 1;
    for disc in posits:
        if ((disc[0] + time) % disc[1]) != 0:
            valid = 0;
            break;

print('\nPart 2:');
print('First Time: ', time);