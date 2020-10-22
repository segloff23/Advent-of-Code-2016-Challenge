
import re;

def read(val, registers):
    try:
        return int(val);
    except:
        return registers[val];

def cpy(registers, x, y):
    try:
        registers[y] = read(x, registers);
    except:
        None;
    return 1;

def inc(registers, x):
    try:
        registers[x] += 1;
    except:
        None;
    return 1;

def dec(registers, x):
    try:
        registers[x] -= 1;
    except:
        None;
    return 1;

def jnz(registers, x, y):
    try:
        if read(x, registers) != 0:
            return read(y, registers);
    except:
        None;
    return 1;

def tgl(registers, instructions, pointer, x):
    try:
       tgl_pointer = pointer + registers[x];
       tgl_instruction = instructions[tgl_pointer];
       if tgl_instruction[0] == 'inc':
           instructions[tgl_pointer][0] = 'dec';
       elif len(tgl_instruction) == 2:
           instructions[tgl_pointer][0] = 'inc';
       elif tgl_instruction[0] == 'jnz':
           instructions[tgl_pointer][0] = 'cpy';
       elif len(tgl_instruction) == 3:
           instructions[tgl_pointer][0] = 'jnz';
    except:
        None;
    return 1;

with open('Day_23_Sample.txt') as file:
    instructions = [re.findall('cpy|inc|dec|jnz|tgl|[a-d]|\d+|-\d+', line.strip()) for line in file];

for line in instructions:
    for i in range(len(line)):
        element = line[i];
        try:
            line[i] = int(line[i]);
        except:
            None;
    #print(line);


registers = {'a': 8, 'b': 0, 'c': 0, 'd': 0}
pointer = 0;
while pointer < len(instructions):
    
    step = instructions[pointer];
    command = step[0];
    if command == 'cpy':
        pointer += cpy(registers, step[1], step[2]);
    elif command == 'inc':
        pointer += inc(registers, step[1]);
    elif command == 'dec':
        pointer += dec(registers, step[1]);
    elif command == 'jnz':
        pointer += jnz(registers, step[1], step[2]);
    elif command == 'tgl':
        pointer += tgl(registers, instructions, pointer, step[1]);
    #print(registers);
    
print(registers);







