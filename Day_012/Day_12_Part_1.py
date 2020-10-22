
import re;

def read(val, registers):
    try:
        return int(val);
    except:
        return registers[val];

with open('Day_12_Input.txt') as file:
    instructions = [re.findall('cpy|inc|dec|jnz|[a-d]|\d+|-\d+', line.strip()) for line in file];

for line in instructions:
    for i in range(len(line)):
        element = line[i];
        try:
            line[i] = int(line[i]);
        except:
            if line[i] == 'cpy':
                line[i] = 0;
            elif line[i] == 'inc':
                line[i] = 1;
            elif line[i] == 'dec':
                line[i] = 2;
            elif line[i] == 'jnz':
                line[i] = 3;

registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
pointer = 0;
while pointer < len(instructions):
    
    step = instructions[pointer];
    command = step[0];
    if command == 0:
        registers[step[2]] = read(step[1], registers);
    elif command == 1:
        registers[step[1]] += 1;
    elif command == 2:
        registers[step[1]] -= 1;
    elif command == 3:
        if read(step[1], registers) != 0:
            pointer += step[2] - 1;
    pointer += 1;
    
print(registers);
