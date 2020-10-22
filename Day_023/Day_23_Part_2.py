
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

def jnz_loop(registers, state_reg, reg_1, reg_1_op, reg_2, reg_2_op):
    
    if state_reg == reg_1:
        if reg_2_op == 'inc':
            registers[reg_2] += registers[state_reg];
        else:
            registers[reg_2] -= registers[state_reg];
    else:
        if reg_1_op == 'inc':
            registers[reg_1] += registers[state_reg];
        else:
            registers[reg_1] -= registers[state_reg];
    registers[state_reg] = 0;
    
    return 1;

def optimize_instructions(instructions):
    
    for i in range(len(instructions)):
        step = instructions[i];
        if step[0] == 'jnz':
            if step[2] == -2:
                state_reg = step[1];
                reg_1_op = instructions[i-1][0];
                reg_2_op = instructions[i-2][0];
                reg_1 = instructions[i-1][1];
                reg_2 = instructions[i-2][1];
                if (reg_1_op == 'inc') or (reg_1_op == 'dec'):
                    if (reg_2_op == 'inc') or (reg_2_op == 'dec'):
                        instructions[i] = ['jnz_loop', state_reg, reg_1, reg_1_op, reg_2, reg_2_op];
    return 0;

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

def mult(registers, outer_state_reg, inner_state_reg, main_reg, main_reg_op):
    
    if main_reg_op == 'inc':
        registers[main_reg] += abs(registers[outer_state_reg] * registers[inner_state_reg]);
    else:
        registers[main_reg] -= abs(registers[outer_state_reg] * registers[inner_state_reg]);
    registers[inner_state_reg] = 0;
    registers[outer_state_reg] = 0;
    return 5;

with open('Day_23_Sample.txt') as file:
    base_instructions = [findall('cpy|inc|dec|jnz|tgl|[a-d]|\d+|-\d+', line.strip()) for line in file];

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

registers = {'a': 12, 'b': 0, 'c': 0, 'd': 0}
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
    elif command == 'jnz_loop':
        pointer += jnz_loop(registers, step[1], step[2], step[3], step[4], step[5]);
    elif command == 'mult':
        pointer += mult(registers, step[1], step[2], step[3], step[4]);
    elif command == 'jnz':
        pointer += jnz(registers, step[1], step[2]);
    elif command == 'tgl':
        instructions = deepcopy(base_instructions);
        pointer += tgl(registers, instructions, pointer, step[1]);
        base_instructions = deepcopy(instructions);
        optimize_instructions_deep(instructions);

    #print(registers);
    
print(registers);






