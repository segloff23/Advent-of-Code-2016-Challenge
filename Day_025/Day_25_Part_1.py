

from re import findall;
from copy import deepcopy;
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

def optimize_instructions_deep(instructions):
    
    for i in range(len(instructions)):
        step = instructions[i];
        if step[0] == 'jnz':
            if step[2] == -5:
                outer_state_reg = step[1];
                inner_state_reg = instructions[i-2][1];
                if instructions[i-3][1] == inner_state_reg:
                    main_reg = instructions[i-4][1];
                    main_reg_op = instructions[i-4][0];
                else:
                    main_reg = instructions[i-3][1];
                    main_reg_op = instructions[i-3][0];
                instructions[i-4] = ['mult', outer_state_reg, inner_state_reg, main_reg, main_reg_op];
    return 0;

def out(registers, a):
    output = read(a, registers);
    print(output);
    return 1, output;

def mult(registers, outer_state_reg, inner_state_reg, main_reg, main_reg_op):
    
    if main_reg_op == 'inc':
        registers[main_reg] += abs(registers[outer_state_reg] * registers[inner_state_reg]);
    else:
        registers[main_reg] -= abs(registers[outer_state_reg] * registers[inner_state_reg]);
    registers[inner_state_reg] = 0;
    registers[outer_state_reg] = 0;
    return 5;

with open('Day_25_Input.txt') as file:
    base_instructions = [findall('cpy|inc|out|dec|jnz|tgl|[a-d]|\d+|-\d+', line.strip()) for line in file];

for line in base_instructions:
    for i in range(len(line)):
        element = line[i];
        try:
            line[i] = int(line[i]);
        except:
            None;
    #print(line);


instructions = deepcopy(base_instructions);
optimize_instructions_deep(instructions);



valid = 0;
a_reg = 1;
while not valid:
    valid = 1;
    registers = {'a': a_reg, 'b': 0, 'c': 0, 'd': 0}
    pointer = 0;
    output_generated = 0;
    last_output = -1;
    for cycles in range(1000000):
        step = instructions[pointer];
        command = step[0];
        if command == 'cpy':
            pointer += cpy(registers, step[1], step[2]);
        elif command == 'inc':
            pointer += inc(registers, step[1]);
        elif command == 'dec':
            pointer += dec(registers, step[1]);
        elif command == 'mult':
            pointer += mult(registers, step[1], step[2], step[3], step[4]);
        elif command == 'jnz':
            pointer += jnz(registers, step[1], step[2]);
        elif command == 'out':
            output_generated = 1;
            shift, output = out(registers, step[1]);
            pointer += shift;
            if (output == (1 - last_output)) or (last_output == -1):
                last_output = output;
            else:
                valid = 0;
                break;
    if (not valid) or (output_generated == 0):
        a_reg += 1;
        valid = 0;
        print('FAIL');

print(registers);






